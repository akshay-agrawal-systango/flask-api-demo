from app import app
from api.users.routes import users

app.register_blueprint(users)
