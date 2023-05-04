from flask import Blueprint

user_router = Blueprint('user', __name__, url_prefix='/users')

@user_router.get('/@me')
def get_current_user():
    return 'This is me'
