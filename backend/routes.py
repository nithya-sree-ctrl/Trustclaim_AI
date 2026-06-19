from flask import render_template, request
from backend.app import app
from agents.orchestrator import process_claim
import os
from analytics.dashboard_metrics import (
    calculate_metrics
)

@app.route("/analytics")
def analytics():

    metrics = calculate_metrics()

    return render_template(
        "analytics.html",
        metrics=metrics
    )

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    claim = request.form["claim"]

    files = request.files.getlist("images")

    image_paths = []

    for file in files:

        path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(path)

        image_paths.append(path)

    result = process_claim(
        claim,
        image_paths
    )

    return render_template(
        "results.html",
        result=result
    )