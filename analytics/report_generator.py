import pandas as pd
from datetime import datetime


def generate_report(output_file="output/output.csv"):

    try:
        df = pd.read_csv(output_file)

        report = {
            "generated_at": str(datetime.now()),
            "total_claims": len(df),
            "supported": len(
                df[df["claim_status"] == "supported"]
            ),
            "contradicted": len(
                df[df["claim_status"] == "contradicted"]
            ),
            "not_enough_information": len(
                df[
                    df["claim_status"]
                    == "not_enough_information"
                ]
            )
        }

        return report

    except Exception as e:

        return {
            "error": str(e)
        }