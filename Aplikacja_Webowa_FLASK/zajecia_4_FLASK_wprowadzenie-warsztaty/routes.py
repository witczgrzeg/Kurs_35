from flask import Blueprint

my_blueprint =Blueprint('my_blueprint', __name__)

@my_blueprint.route('/')
def root_route():
    return "Hello form the root route"