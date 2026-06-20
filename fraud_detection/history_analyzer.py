import pandas as pd
import os


def get_user_risk(user_id):

    file_path = "dataset/user_history.csv"


    # if file missing or empty
    if not os.path.exists(file_path):
        return "low"


    if os.path.getsize(file_path) == 0:
        return "low"


    df = pd.read_csv(file_path)


    if "user_id" not in df.columns:
        return "low"


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