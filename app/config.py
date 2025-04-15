import os

COUCHBASE_HOST = os.getenv("COUCHBASE_HOST", "localhost")
COUCHBASE_BUCKET = os.getenv("COUCHBASE_BUCKET", "Fin")
COUCHBASE_SCOPE = os.getenv("COUCHBASE_SCOPE", "money")
COUCHBASE_COLLECTION = os.getenv("COUCHBASE_COLLECTION", "transactions")
COUCHBASE_USER = os.getenv("COUCHBASE_USER", "Administrator")
COUCHBASE_PASSWORD = os.getenv("COUCHBASE_PASSWORD", "password")
