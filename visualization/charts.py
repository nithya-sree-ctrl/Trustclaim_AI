import plotly.express as px


def claim_status_chart(df):

    counts = (
        df["claim_status"]
        .value_counts()
        .reset_index()
    )

    counts.columns = [
        "status",
        "count"
    ]

    fig = px.pie(
        counts,
        names="status",
        values="count",
        title="Claim Status Distribution"
    )

    return fig.to_html(
        full_html=False
    )