import pandas as pd
import os


def save_results(
    results,
    output_path="output/output.csv"
):

    os.makedirs(
        "output",
        exist_ok=True
    )

    df = pd.DataFrame(results)

    required_columns = [

        "evidence_standard_met",

        "evidence_standard_met_reason",

        "risk_flags",

        "issue_type",

        "object_part",

        "claim_status",

        "claim_status_justification",

        "supporting_image_ids",

        "valid_image",

        "severity"
    ]

    for col in required_columns:

        if col not in df.columns:

            df[col] = ""

    df = df[
        required_columns
    ]

    df.to_csv(
        output_path,
        index=False
    )

    return output_path