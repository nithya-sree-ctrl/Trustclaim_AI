from flask import Flask


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../templates/static"
)


app.config["UPLOAD_FOLDER"] = "templates/uploads"


from backend import routes