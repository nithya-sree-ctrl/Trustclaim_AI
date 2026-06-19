import pandas as pd


def calculate_metrics():

    try:

        df = pd.read_csv(
            "output/output.csv"
        )

        total_claims = len(df)

        supported = len(
            df[
                df["claim_status"]
                == "supported"
            ]
        )

        contradicted = len(
            df[
                df["claim_status"]
                == "contradicted"
            ]
        )

        insufficient = len(
            df[
                df["claim_status"]
                ==
                "not_enough_information"
            ]
        )

        avg_risk = 0

        return {
            "total_claims":
                total_claims,

            "supported":
                supported,

            "contradicted":
                contradicted,

            "insufficient":
                insufficient,

            "avg_risk":
                avg_risk
        }

    except:

        return {
            "total_claims": 0,
            "supported": 0,
            "contradicted": 0,
            "insufficient": 0,
            "avg_risk": 0
        }