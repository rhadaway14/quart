from quart import Blueprint
from app.api.v1.data import resources

data_blueprint = Blueprint('data', __name__, url_prefix="/data")

data_blueprint.add_url_rule("/", view_func=resources.main_handler)
