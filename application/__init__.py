"""Top-level package for Sample Project."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

# Globally accessible libraries
# All libraries will be initialized in the create app method
db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    with app.app_context():

        # Register Blueprints
        from .dashboard import views as dashboard_views
        app.register_blueprint(dashboard_views.dashboard_bp)

        from .auth import views as auth_views
        app.register_blueprint(auth_views.auth_bp)

        db.create_all()

        return app
