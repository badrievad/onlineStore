from flask import Flask
from flask_cors import CORS


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    CORS(app)
    app.debug = debug
    app.config.from_pyfile("config.py")

    from .site import web_bp as web_blueprint
    from .warehouse import warehouse_bp as warehouse_blueprint

    app.register_blueprint(web_blueprint)
    app.register_blueprint(warehouse_blueprint)

    return app
