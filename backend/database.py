import pandas as pd
import os


class Database:

    def __init__(self):

        self.claims_file = (
            "dataset/claims.csv"
        )

        self.user_history_file = (
            "dataset/user_history.csv"
        )

    def get_claims(self):

        if os.path.exists(
            self.claims_file
        ):
            return pd.read_csv(
                self.claims_file
            )

        return pd.DataFrame()

    def get_user_history(self):

        if os.path.exists(
            self.user_history_file
        ):
            return pd.read_csv(
                self.user_history_file
            )

        return pd.DataFrame()