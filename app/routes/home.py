from flask import Blueprint, render_template
from sqlalchemy import func
from datetime import datetime, timedelta

from app.models import db
from app.models.employee import Employee

home_bp = Blueprint("home", __name__)


@home_bp.route("/home")
def home():
    total_employees = Employee.query.count()

    dept_rows = (
        db.session.query(Employee.department, func.count(Employee.id))
        .group_by(Employee.department)
        .order_by(Employee.department)
        .all()
    )

    dept_labels = [row[0] for row in dept_rows]
    dept_counts = [row[1] for row in dept_rows]
    total_departments = len(dept_rows)

    total_payroll = db.session.query(func.coalesce(func.sum(Employee.salary), 0)).scalar()
    avg_salary = db.session.query(func.coalesce(func.avg(Employee.salary), 0)).scalar()
    max_salary_row = db.session.query(func.coalesce(func.max(Employee.salary), 0)).scalar()
    min_salary_row = db.session.query(func.coalesce(func.min(Employee.salary), 0)).scalar()

    recent_employees = Employee.query.order_by(Employee.id.desc()).limit(5).all()
    top_earners = Employee.query.order_by(Employee.salary.desc()).limit(5).all()

    largest_department = None
    largest_department_count = 0
    if dept_rows:
        largest_row = max(dept_rows, key=lambda row: row[1])
        largest_department = largest_row[0]
        largest_department_count = largest_row[1]

    buckets = [0, 0, 0, 0]
    for emp in Employee.query.all():
        salary = emp.salary or 0
        if salary < 30000:
            buckets[0] += 1
        elif salary < 60000:
            buckets[1] += 1
        elif salary < 100000:
            buckets[2] += 1
        else:
            buckets[3] += 1

    new_hires = 0
    if hasattr(Employee, "created_at"):
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)
        new_hires = Employee.query.filter(Employee.created_at >= thirty_days_ago).count()

    return render_template(
        "home.html",
        total_employees=total_employees,
        total_departments=total_departments,
        total_payroll=total_payroll,
        avg_salary=avg_salary,
        max_salary=max_salary_row,
        min_salary=min_salary_row,
        new_hires=new_hires,
        recent_employees=recent_employees,
        top_earners=top_earners,
        largest_department=largest_department,
        largest_department_count=largest_department_count,
        dept_labels=dept_labels,
        dept_counts=dept_counts,
        salary_buckets=buckets
    )