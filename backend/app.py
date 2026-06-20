from flask import Flask
import os


BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)


app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "templates", "static")
)



# upload folder
app.config["UPLOAD_FOLDER"] = os.path.join(
    BASE_DIR,
    "templates",
    "uploads"
)



# create uploads folder automatically
os.makedirs(
    app.config["UPLOAD_FOLDER"],
    exist_ok=True
)



from backend import routes