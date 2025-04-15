from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions
from acouchbase.cluster import Cluster  # async client
from .config import *

cluster = None
collection = None


async def init_db():
    global cluster, collection
    cluster = await Cluster.connect(
        f"couchbase://{COUCHBASE_HOST}",
        ClusterOptions(PasswordAuthenticator(COUCHBASE_USER, COUCHBASE_PASSWORD))
    )
    bucket = cluster.bucket(COUCHBASE_BUCKET)
    await bucket.on_connect()
    scope = bucket.scope(COUCHBASE_SCOPE)
    collection = scope.collection(COUCHBASE_COLLECTION)
