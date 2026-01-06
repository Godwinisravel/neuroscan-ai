from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    from routes.auth import auth_bp
    from routes.patient import patient_bp
    from routes.doctor import doctor_bp
    from routes.admin import admin_bp
    from routes.reports import report_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(report_bp)

    return app

app = create_app()
