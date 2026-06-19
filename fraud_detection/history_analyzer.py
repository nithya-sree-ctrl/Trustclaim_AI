import pandas as pd

def get_user_risk(user_id):

    df = pd.read_csv(
        "dataset/user_history.csv"
    )

    user = df[df["user_id"] == user_id]

    if len(user) == 0:
        return "low"

    claims = int(
        user.iloc[0]["previous_claims"]
    )

    if claims > 10:
        return "high"

    if claims > 5:
        return "medium"

    return "low"