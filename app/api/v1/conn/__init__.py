from quart import Blueprint
from . import resources

conn_blueprint = Blueprint('conn', __name__, url_prefix='/conn')

conn_blueprint.add_url_rule('/', view_func=resources.root)
