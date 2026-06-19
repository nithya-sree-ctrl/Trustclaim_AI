import pandas as pd


def calculate_metrics(
    ground_truth_file,
    prediction_file
):

    truth_df = pd.read_csv(
        ground_truth_file
    )

    pred_df = pd.read_csv(
        prediction_file
    )

    total = len(truth_df)

    correct = 0

    for i in range(total):

        if (
            truth_df.iloc[i]["claim_status"]
            ==
            pred_df.iloc[i]["claim_status"]
        ):
            correct += 1

    accuracy = (
        correct / total
        if total > 0 else 0
    )

    return {
        "total_samples": total,
        "correct_predictions": correct,
        "accuracy": round(
            accuracy * 100,
            2
        )
    }