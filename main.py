from quart import Quart
from app.routes import bp
from app.db import init_db

app = Quart(__name__)
app.register_blueprint(bp)

@app.before_serving
async def startup():
    await init_db()

@app.after_serving
async def shutdown():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
