from quart import Blueprint
from app.api.v1.conn import conn_blueprint
from app.api.v1.data import data_blueprint


def register_routes(app):
    v1 = Blueprint("v1", __name__, url_prefix="/")
    v1.register_blueprint(conn_blueprint)
    v1.register_blueprint(data_blueprint)

    app.register_blueprint(v1)
