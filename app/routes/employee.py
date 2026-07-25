from flask import Blueprint, request, redirect, url_for, render_template, flash, Response
from sqlalchemy import or_, asc, desc
from werkzeug.security import generate_password_hash
import csv
import io

from app.models import db
from app.models.employee import Employee

employee_bp = Blueprint("employee", __name__)


@employee_bp.route("/employee/list")
def employee_list():
    search = request.args.get("search", "").strip()
    department = request.args.get("department", "").strip()
    min_salary = request.args.get("min_salary", "").strip()
    max_salary = request.args.get("max_salary", "").strip()
    sort_by = request.args.get("sort_by", "id")
    order = request.args.get("order", "asc")
    page = request.args.get("page", 1, type=int)
    per_page = 5

    query = Employee.query

    if search:
        query = query.filter(
            or_(
                Employee.name.ilike(f"%{search}%"),
                Employee.email.ilike(f"%{search}%"),
                Employee.department.ilike(f"%{search}%")
            )
        )

    if department:
        query = query.filter(Employee.department == department)

    if min_salary:
        try:
            query = query.filter(Employee.salary >= float(min_salary))
        except ValueError:
            flash("Minimum salary must be a number.", "warning")

    if max_salary:
        try:
            query = query.filter(Employee.salary <= float(max_salary))
        except ValueError:
            flash("Maximum salary must be a number.", "warning")

    columns = {
        "name": Employee.name,
        "email": Employee.email,
        "department": Employee.department,
        "salary": Employee.salary,
        "id": Employee.id
    }
    column = columns.get(sort_by, Employee.id)
    query = query.order_by(desc(column) if order == "desc" else asc(column))

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    employees = pagination.items
    departments = db.session.query(Employee.department).distinct().order_by(Employee.department).all()

    return render_template(
        "employee.html",
        employees=employees,
        pagination=pagination,
        search=search,
        department=department,
        min_salary=min_salary,
        max_salary=max_salary,
        sort_by=sort_by,
        order=order,
        departments=departments,
        total=pagination.total
    )


@employee_bp.route("/employee/add", methods=["GET", "POST"])
def employeeAdd():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        salary = request.form.get("salary", "")
        department = request.form.get("department", "").strip()

        if not all([name, email, password, salary, department]):
            flash("All fields are required.", "danger")
            return render_template("add_employee.html", form=request.form)

        try:
            salary_value = float(salary)
            if salary_value < 0:
                raise ValueError
        except ValueError:
            flash("Salary must be a valid positive number.", "danger")
            return render_template("add_employee.html", form=request.form)

        if Employee.query.filter_by(email=email).first():
            flash("An employee with this email already exists.", "danger")
            return render_template("add_employee.html", form=request.form)

        employee = Employee(
            name=name,
            email=email,
            password=generate_password_hash(password),
            salary=salary_value,
            department=department
        )

        db.session.add(employee)
        db.session.commit()

        flash(f"Employee '{name}' added successfully.", "success")
        return redirect(url_for("employee.employee_list"))

    return render_template("add_employee.html")


@employee_bp.route("/employee/employeeDetail/<int:id>", methods=["GET"])
def employeeDetail(id):
    employee = Employee.query.get_or_404(id)
    return render_template("employee_detail.html", employee=employee)


@employee_bp.route("/employee/employeeUpdate/<int:id>", methods=["GET", "POST"])
def employeeUpdate(id):
    employee = Employee.query.get_or_404(id)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        salary = request.form.get("salary", "")
        department = request.form.get("department", "").strip()

        if not all([name, email, salary, department]):
            flash("Name, email, salary and department are required.", "danger")
            return render_template("update_employee.html", employee=employee)

        try:
            salary_value = float(salary)
            if salary_value < 0:
                raise ValueError
        except ValueError:
            flash("Salary must be a valid positive number.", "danger")
            return render_template("update_employee.html", employee=employee)

        existing = Employee.query.filter(Employee.email == email, Employee.id != id).first()
        if existing:
            flash("Another employee already uses this email.", "danger")
            return render_template("update_employee.html", employee=employee)

        employee.name = name
        employee.email = email
        employee.salary = salary_value
        employee.department = department

        if password:
            employee.password = generate_password_hash(password)

        db.session.commit()

        flash(f"Employee '{name}' updated successfully.", "success")
        return redirect(url_for("employee.employeeDetail", id=employee.id))

    return render_template("update_employee.html", employee=employee)


@employee_bp.route("/employee/employeeDelete/<int:id>", methods=["POST", "GET"])
def employeeDelete(id):
    employee = Employee.query.get_or_404(id)
    name = employee.name

    db.session.delete(employee)
    db.session.commit()

    flash(f"Employee '{name}' deleted successfully.", "success")
    return redirect(url_for("employee.employee_list"))


@employee_bp.route("/employee/export")
def employeeExport():
    employees = Employee.query.order_by(Employee.id).all()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Name", "Email", "Department", "Salary"])

    for emp in employees:
        writer.writerow([emp.id, emp.name, emp.email, emp.department, emp.salary])

    response = Response(output.getvalue(), mimetype="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=employees.csv"
    return response