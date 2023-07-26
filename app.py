from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

#for new project, change f1_app to database name
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/f1_app"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers.drivers_controller import drivers_blueprint

app.register_blueprint(drivers_blueprint)


