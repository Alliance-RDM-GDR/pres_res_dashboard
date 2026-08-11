import dash_bootstrap_components as dbc
from dash import html, dcc

from components.cards import create_kpi_card
from components.charts import create_line_chart, create_donut_chart

# ---------------------------------------------------
# Overview Tab Layout
# ---------------------------------------------------
def layout(appraisal_metrics, appraisal_trend_df):

    return dbc.Container(
        [
          dbc.Row(
            [
                html.H2(
                    "Overview",
                    className="mb-4"
                ),

                html.P(
                  """
                  The Appraisal Dashboard includes information about the total datasets appraised. It breaks the information down by year into accepted and rejected for long-term preservation. The same information is now available for reappraisal decisions. The Preservation Question tab, outlines the responses provided by researchers when answering the long-term preservation question during the deposit process.
                  """
                ),
            ]
          ), 
          dbc.Row(
              [
                  dbc.Col(
                    create_kpi_card(
                        "Datasets Reviewed",
                        appraisal_metrics["total_reviewed"],
                      ),
                      width=3,
                  ),
                  dbc.Col(
                      create_kpi_card(
                          "Accepted", appraisal_metrics["accepted"]
                      ),
                      width=3,
                  ),
                  dbc.Col(
                      create_kpi_card(
                          "Rejected", appraisal_metrics["rejected"]
                      ),
                      width=3,
                  ),
                  dbc.Col(
                      create_kpi_card(
                          "Acceptance Rate",
                          f"{appraisal_metrics['acceptance_rate']}%",
                      ),
                      width=3,
                  ),
              ],
              className="mb-4",
          ),
          dbc.Row(
            [
              dbc.Col(
                 dbc.Card ([
                  dbc.CardHeader("Appraisal Activity Trend"),   
                  dbc.CardBody(dcc.Graph (
                        figure=create_line_chart(
                          appraisal_trend_df,
                          "Year",
                          "Count",
                          "Appraisal Activity Trend",
                          ),
                      ),
                    ),
                  ]
                ),
                  width=12,
              ),
          ]
        ),
      ],
      fluid=True,
  )
