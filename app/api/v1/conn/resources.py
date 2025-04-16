from quart import jsonify
from http import HTTPStatus


async def root():
    try:
        return jsonify({"connection": "successful"}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
