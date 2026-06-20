from flask import render_template, request, send_from_directory
from backend.app import app
from agents.orchestrator import process_claim
from analytics.dashboard_metrics import calculate_metrics
import os


@app.route("/analytics")
def analytics():

    metrics = calculate_metrics()

    return render_template(
        "analytics.html",
        metrics=metrics
    )


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )

@app.route("/analyze", methods=["POST"])
def analyze():

    claim = request.form["claim"]

    files = request.files.getlist("images")

    image_paths = []

    for file in files:

        filename = file.filename

        save_path = os.path.join(
    app.config["UPLOAD_FOLDER"],
    filename
)

        file.save(save_path)

        image_paths.append(
    "uploads/" + filename
)

        file.save(save_path)


        # browser path
        image_paths.append(
            "uploads/" + filename
        )


    result = process_claim(
        claim,
        image_paths
    )


    return render_template(
        "results.html",
        result=result
    )
