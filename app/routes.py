from quart import Blueprint, jsonify
from .db import collection
from couchbase.exceptions import CouchbaseException

bp = Blueprint("main", __name__)


@bp.route("/api/v1/transaction/<user>/<txn>")
async def handle_transaction(user, txn):
    try:
        prefix = f"user::{user}::trans::{txn}"
        txn_data = await collection.get(prefix)
        return jsonify(txn_data.content_as[dict]), 200
    except CouchbaseException as e:
        return jsonify({"error": str(e)}), 500
