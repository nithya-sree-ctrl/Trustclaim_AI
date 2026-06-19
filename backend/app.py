from flask import Flask
import os

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.config["UPLOAD_FOLDER"] = "frontend/uploads"

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

from backend.routes import *