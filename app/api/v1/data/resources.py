from quart import jsonify
from http import HTTPStatus
from datetime import timedelta

from couchbase.options import GetOptions, UpsertOptions
from app.db.couchbase import get_collection


async def main_handler():
    try:
        collection = await get_collection()
        timeout = timedelta(seconds=2)

        keys = [
            "user::loadtest::trans::txn123",
            "user::loadtest::trans::txn2",
            "user::loadtest::trans::txn3",
            "user::loadtest::trans::txn4"
        ]

        reads = []
        for key in keys:
            try:
                result = await collection.get(key, GetOptions(timeout=timeout))
                reads.append(result.content_as[dict])
            except Exception as e:
                reads.append({"error": f"{key}: {str(e)}"})

        post_doc_id = "user::loadtest::trans::txn999"
        payload = {"result": "combined", "success": True}
        await collection.upsert(post_doc_id, payload, UpsertOptions(timeout=timeout))

        return jsonify({
            "reads": reads,
            "write": {
                "doc_id": post_doc_id,
                "status": "upserted"
            }
        }), HTTPStatus.OK

    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
