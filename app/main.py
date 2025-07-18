from flask import Flask
from app.api.endpoints import api_bp
from app.config import Config
from app.api.swagger import swagger_bp

# Initialize the Flask app
app = Flask(__name__, static_folder="static", static_url_path="/static")

# Load configuration from Config class
app.config.from_object(Config)

# Register API blueprints
app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(swagger_bp, url_prefix="/docs")


# Only run app here if script is executed directly (not via 'flask run')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
