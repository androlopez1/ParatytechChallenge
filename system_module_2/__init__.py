from flask import Flask

def create_app(config_object="config"):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Configure datastore connection
    from . import datastore
    datastore.init_app(app)

    # Register Blueprints
    from .routes import bp
    app.register_blueprint(bp)

    return app