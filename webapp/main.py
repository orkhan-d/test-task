from webapp.app import app
from db.base import db

from webapp.modules import blueprints

from dotenv import load_dotenv
import os
load_dotenv('.env')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['WTF_CSRF_ENABLED'] = False

for blueprint in blueprints:
    app.register_blueprint(blueprint)

with app.app_context():
    db.create_all()
