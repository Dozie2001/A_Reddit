from .base import BaseService
from api.extensions import bcrypt
from api.models import User
from werkzeug.exceptions import Unauthorized, Conflict
class UserService(BaseService):
    def create_user(self, username: str, email: str, password: str):
        hashed_password = bcrypt.generate_password_hash(password)
        existing_user = User.query.filter((User.email == email) | 
                                           (User.username == username)).first() is not None
        if existing_user:
            raise Conflict('User with the same email or username already exists')
        
        new_user =  User(username=username, email=email, password=hashed_password)
        self.db.session.add(new_user)
        self.db.session.commit()
        return True
    
    def authenticate_user(self, email: str, password: str):
        existing_user = User.query.filter_by(email=email).first()

        if not existing_user:
            raise Unauthorized('Invalid credentials')

        if bcrypt.check_password_hash(existing_user.password, password):
            raise Unauthorized('Invalid credentials')
        
        return existing_user.id
