from acouchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions
from couchbase.exceptions import CouchbaseException
from app.core.config import settings

_cluster = None
_collection = None


async def get_collection():
    global _cluster, _collection
    if _collection is not None:
        return _collection

    try:
        _cluster = await Cluster.connect(
            f"couchbase://{settings.COUCHBASE_HOST}",
            ClusterOptions(PasswordAuthenticator(
                settings.COUCHBASE_USER,
                settings.COUCHBASE_PASSWORD
            ))
        )
        bucket = _cluster.bucket(settings.COUCHBASE_BUCKET)
        await bucket.on_connect()
        scope = bucket.scope(settings.COUCHBASE_SCOPE)
        _collection = scope.collection(settings.COUCHBASE_COLLECTION)
        return _collection

    except CouchbaseException as e:
        raise RuntimeError(f"Could not connect to Couchbase: {e}")
