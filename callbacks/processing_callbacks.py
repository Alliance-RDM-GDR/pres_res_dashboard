import pandas as pd

from dash import callback, Output, Input

from utils.calculations import (
    calculate_processing_metrics
)

from components.charts import (
    create_processing_trend_chart,
    create_bar_chart,
)


# ---------------------------------------------------
# Dataset Processing Callbacks
# ---------------------------------------------------

def register_processing_callbacks(df):

    # -----------------------------
    # Dataset Processing Volume
    # -----------------------------

    @callback(
        Output(
            "dp-volume-chart",
            "figure"
        ),
        Input(
            "dp-year-selector",
            "value"
        ),
    )
    def update_volume(year):

        fig = create_bar_chart(
            df,
            "Year",
            "Total Datasets Processed",
            "Dataset Processing Volume"
        )

        return fig

    # -----------------------------
    # Distribution Card Header
    # -----------------------------

    @callback(
        Output(
            "dp-card-header-title",
            "children"
        ),
        Input(
            "dp-year-selector",
            "value"
        ),
    )
    def update_card_title(selected_year):

        if not selected_year:
            return "Processing Distribution"

        return f"Processing Distribution - {selected_year}"

    # -----------------------------
    # Processing Distribution
    # -----------------------------

    @callback(
        Output(
            "dp-distribution-chart",
            "figure"
        ),
        Input(
            "dp-year-selector",
            "value"
        ),
    )
    def update_distribution(year):

        selected = df[
            df["Year"] == year
        ]

        if selected.empty:
            return create_bar_chart(
                pd.DataFrame(
                    columns=["Metric", "Count"]
                ),
                "Metric",
                "Count",
                f"Processing Distribution - {year}"
            )

        row = selected.iloc[0]

        chart_df = pd.DataFrame(
            {
                "Metric": [
                    "Total AIPs",
                    "Datasets Processed",
                    "Datasets Reprocessed",
                    "Datasets Completed"
                ],

                "Count": [
                    row["Total AIPs"],
                    row["Total Datasets Processed"],
                    row["Total Datasets Reprocessed"],
                    row["Total Datasets Completed"],
                ]
            }
        )

        return create_bar_chart(
            chart_df,
            "Metric",
            "Count",
            f"Processing Distribution - {year}"
        )

    # -----------------------------
    # Annual Processing Trend
    # -----------------------------

    @callback(
        Output(
            "dp-trend-chart",
            "figure"
        ),
        Input(
            "dp-metric-selector",
            "value"
        ),
    )
    def update_trend(metric):

        return create_processing_trend_chart(
            df,
            metric,
        )

    # -----------------------------
    # KPI Cards
    # -----------------------------

    @callback(
        Output(
            "dp-total-aips",
            "children"
        ),
        Output(
            "dp-datasets-processed",
            "children"
        ),
        Output(
            "dp-datasets-reprocessed",
            "children"
        ),
        Output(
            "dp-datasets-completed",
            "children"
        ),
        Input(
            "dp-year-selector",
            "value"
        ),
    )
    def update_processing_cards(year):

      # Default to the latest year
      if year is None:
          year = df["Year"].iloc[-1]

      print("Selected year:", year)

      metrics = calculate_processing_metrics(
          df,
          year
      )

      return (
          metrics["total_aips"],
          metrics["datasets_processed"],
          metrics["datasets_reprocessed"],
          metrics["datasets_completed"],
      )