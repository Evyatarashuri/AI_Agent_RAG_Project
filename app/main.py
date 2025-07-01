from flask import Flask
from app.api.endpoints import api_bp
from app.config import Config
from app.api.swagger import swagger_bp

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static")
    app.config.from_object(Config)

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(swagger_bp, url_prefix="/docs")


    @app.route("/")
    def home():
        return "Welcome to AI Agent RAG Project API"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
