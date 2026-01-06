from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from routes.auth import auth_bp
    from routes.patient import patient_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(patient_bp)

    return app

app = create_app()
