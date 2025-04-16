# import asyncio
# import sys

from quart import Quart
from app.api.v1.routes import register_routes
from app.db.couchbase import get_collection
from dotenv import load_dotenv


load_dotenv()

app = Quart(__name__)
register_routes(app)


@app.before_serving
async def startup():
    await get_collection()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
