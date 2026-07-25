from flask import Blueprint, render_template, request, redirect, url_for, flash

from app.models import db
from app.models.department import Department
from app.models.employee import Employee

department_bp = Blueprint("department", __name__)


@department_bp.route("/department")
def departmentHome():
    departments = Department.query.all()

    dept_data = []
    for dept in departments:
        employee_count = Employee.query.filter_by(department=dept.name).count()
        dept_data.append({
            "id": dept.id,
            "name": dept.name,
            "head": dept.head,
            "employee_count": employee_count
        })

    total_employees = Employee.query.count()
    largest_department = max(dept_data, key=lambda d: d["employee_count"])["name"] if dept_data else None

    return render_template(
        "department.html",
        departments=dept_data,
        total_employees=total_employees,
        largest_department=largest_department
    )


@department_bp.route("/department/add", methods=["POST"])
def departmentAdd():
    name = request.form.get("name", "").strip()
    head = request.form.get("head", "").strip()

    if not name:
        flash("Department name is required.", "danger")
        return redirect(url_for("department.departmentHome"))

    if Department.query.filter_by(name=name).first():
        flash("A department with this name already exists.", "danger")
        return redirect(url_for("department.departmentHome"))

    new_dept = Department(name=name, head=head)
    db.session.add(new_dept)
    db.session.commit()

    flash("Department added successfully.", "success")
    return redirect(url_for("department.departmentHome"))


@department_bp.route("/department/edit/<int:dept_id>", methods=["GET", "POST"])
def departmentEdit(dept_id):
    dept = Department.query.get_or_404(dept_id)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        head = request.form.get("head", "").strip()

        if not name:
            flash("Department name is required.", "danger")
            return render_template("department_edit.html", dept=dept)

        dept.name = name
        dept.head = head
        db.session.commit()

        flash("Department updated successfully.", "success")
        return redirect(url_for("department.departmentHome"))

    return render_template("department_edit.html", dept=dept)


@department_bp.route("/department/delete/<int:dept_id>", methods=["POST"])
def departmentDelete(dept_id):
    dept = Department.query.get_or_404(dept_id)
    db.session.delete(dept)
    db.session.commit()

    flash("Department deleted successfully.", "success")
    return redirect(url_for("department.departmentHome"))