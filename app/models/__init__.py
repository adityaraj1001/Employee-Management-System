from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.models.employee import Employee
from app.models.department import Department