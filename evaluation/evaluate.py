from evaluation.metrics import (
    calculate_metrics
)

from evaluation.strategy_comparison import (
    compare_strategies
)

from evaluation.evaluation_report import (
    generate_report
)


def run_evaluation():

    metrics = calculate_metrics(

        "dataset/sample_claims.csv",

        "output/output.csv"
    )

    strategies = compare_strategies()

    final_report = generate_report(

        metrics,

        "Gemini Vision Approach"
    )

    print(final_report)

    print("\nAvailable Strategies:\n")

    for strategy in strategies:

        print(
            strategy["name"]
        )

        print(
            "Pros:",
            strategy["pros"]
        )

        print(
            "Cons:",
            strategy["cons"]
        )

        print("-" * 30)


if __name__ == "__main__":

    run_evaluation()