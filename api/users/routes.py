from flask import Blueprint
from api.users.views import UsersAPI

users = Blueprint("users", __name__, url_prefix='/users')

users.add_url_rule('/create', view_func=UsersAPI.as_view('create_users'))
users.add_url_rule('/<int:user_id>', view_func=UsersAPI.as_view('get_users'))

