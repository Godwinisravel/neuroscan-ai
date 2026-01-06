from flask import Blueprint, render_template, session, redirect, url_for

patient_bp = Blueprint("patient", __name__, url_prefix="/patient")

@patient_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template("patient/dashboard.html")
