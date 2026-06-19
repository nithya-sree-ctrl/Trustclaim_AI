from datetime import datetime


def generate_report(
    metrics,
    strategy
):

    report = f"""
======================================
TrustClaim AI Evaluation Report
======================================

Generated:
{datetime.now()}

Strategy Used:
{strategy}

Metrics
-------
Total Samples:
{metrics['total_samples']}

Correct Predictions:
{metrics['correct_predictions']}

Accuracy:
{metrics['accuracy']} %

Operational Analysis
--------------------

Model:
Gemini 2.5 Flash

Image Analysis:
Enabled

Fraud Detection:
Enabled

Explainable AI:
Enabled

Multi-Agent Architecture:
Enabled

======================================
"""

    return report