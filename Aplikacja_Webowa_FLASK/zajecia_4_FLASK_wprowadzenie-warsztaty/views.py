from flask import Blueprint
from flask.views import MethodView

users_blueprint = Blueprint('users',__name__)

class UsersView(MethodView):
    def get(self):
        return "List of Users"
    def post(self):
        return "Add a new User"
    def put(self):
        return "Update an existing User"
    def delete(self):
        return "Delete a User"

users_view = UsersView.as_view('users')
users_blueprint.add_url_rule('/users', view_func=users_view, methods=['GET', 'POST', 'PUT', 'DELETE'])