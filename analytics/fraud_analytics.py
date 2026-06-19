import pandas as pd


def get_fraud_analytics(
    output_file="output/output.csv"
):

    try:

        df = pd.read_csv(output_file)

        fraud_flags = {}

        if "risk_flags" in df.columns:

            for row in df["risk_flags"]:

                for flag in str(row).split(";"):

                    fraud_flags[flag] = (
                        fraud_flags.get(flag, 0) + 1
                    )

        return {

            "total_records": len(df),

            "fraud_flag_distribution":
                fraud_flags
        }

    except Exception as e:

        return {
            "error": str(e)
        }