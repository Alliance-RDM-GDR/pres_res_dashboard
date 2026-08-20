import pandas as pd

from dash import callback, Output, Input


from utils.calculations import (
    calculate_preservation_question_metrics
)

from components.charts import (
    create_response_trend_chart,
    create_donut_chart,
    create_bar_chart,
)

def register_preservation_callbacks(pres_df):
# Pres Question
  @callback(
      Output("pq-volume-chart", "figure"),
      Input("pq-year-selector", "value"),
  )
  def update_volume(year):

      fig = create_bar_chart(
          pres_df,
          "Year",
          "Total_Datasets_for_Year",
          "Dataset Volume"
      )

      return fig

  @callback(
      Output("card-header-title", "children"),
      Input("pq-year-selector", "value"),  # Replace with your actual dropdown ID
  )
  def update_card_title(selected_year):
      # Prevent errors if the dropdown is initially empty
      if not selected_year:
          return "Year Distribution"

      return f"Year Distribution - {selected_year}"

  @callback(
      Output("pq-distribution-chart", "figure"),
      Input("pq-year-selector", "value"),
  )
  def update_distribution(year):

      selected = pres_df[
          pres_df["Year"] == year
      ]

      chart_df = pd.DataFrame(
          {
              "Response": [
                  "Yes",
                  "No",
                  "Unsure",
                  "No Response"
              ],

              "Count": [
                  selected["Yes"].iloc[0],
                  selected["No"].iloc[0],
                  selected["Unsure"].iloc[0],
                  selected["No_Response"].iloc[0],
              ]
          }
      )


      return create_donut_chart(
          chart_df,
          "Response",
          "Count",
          f"Preservation Response - {year}"
      )


  @callback(
      Output("pq-trend-chart", "figure"),
      Input("pq-metric-selector", "value"),
  )
  def update_trend(metric):

      return create_response_trend_chart(
          pres_df,
          metric,
      )

  @callback(
      Output("pq-total-datasets", "children"),
      Output("pq-yes-percent", "children"),
      Output("pq-no-percent", "children"),
      Output("pq-unsure-percent", "children"),
      Output("pq-no-response-percent", "children"),
      Input("pq-year-selector", "value"),
  )
  def update_pres_question_cards(year):

      metrics = calculate_preservation_question_metrics(
          pres_df,
          year
      )

      return (
          f"{int(metrics['total_datasets']):,}",
          f"{metrics['yes_percent']}%",
          f"{metrics['no_percent']}%",
          f"{metrics['unsure_percent']}%",
          f"{metrics['no_response_percent']}%",
      )

  