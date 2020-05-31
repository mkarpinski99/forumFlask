from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from datetime import date

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models


# x = models.Thread(subject="flask nie działa", date=date.today(), visits=0, category=1)
# db.session.add(x)
# db.session.commit()
#
# users = models.Thread.query.all()
#
# for u in users:
#     print(u.id, u.subject)

