import pandas as pd


def get_claim_statistics(
    output_file="output/output.csv"
):

    try:

        df = pd.read_csv(output_file)

        return {

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
                    ==
                    "not_enough_information"
                ]
            ),

            "high_severity": len(
                df[df["severity"] == "high"]
            )
        }

    except Exception as e:

        return {
            "error": str(e)
        }