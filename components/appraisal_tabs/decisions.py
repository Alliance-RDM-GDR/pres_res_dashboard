import dash_bootstrap_components as dbc
from dash import html, dcc

from components.charts import create_stacked_bar, create_donut_chart
# from utils.calculations import get_recommendation_kpis
# from components.cards import create_kpi_card

# ---------------------------------------------------
# Appraisal & Reappraisal Tab Layout
# ---------------------------------------------------
def layout(
    appraisal_decisions_df,
    reappraisal_decisions_df,
    appraisal_df
    # appraisal_df,
  ):
    # recommendation_kpis = get_recommendation_kpis(appraisal_df)

    appraisal_fig = create_stacked_bar(
        appraisal_decisions_df,
        "Year",
        "Count",
        "Decision",
        "Appraisal Decisions"
    )
    reappraisal_fig = create_stacked_bar(
        reappraisal_decisions_df,
        "Year",
        "Count",
        "Decision",
        "Reappraisal Decisions"
    )
    
    appraisal_score_fig = create_donut_chart(
      appraisal_df,
      "appraisal_score_range",
      "appraisal_score_count",
      "Appraisal Categories"
    )
    cost_index_fig = create_donut_chart(
      appraisal_df,
      "cost_index",
      "cost_count",
      "Cost Index Breakdown",
    )

    return dbc.Container(
        [
            dbc.Row(
                [
                    html.H2(
                        "Appraisal and Reappraisal Decisions",
                        className="mb-4"
                    ),

                    html.P(
                      """
                      “Appraisal for preservation is the process of determining whether a dataset has sufficient long-term archival value to merit the work of monitoring, managing, storing and sustaining access to that data, as well as related systems and workflows, persistently over time.”
                      Reappraisal of research data occurs after a retention period is complete. It is used to determine if the data should be kept for a longer period of time.
                      """
                    ),

                    html.P(
                        """
                        Reappraisal occurs after a retention period
                        to determine whether data should continue
                        to be kept.
                        """
                    ),
                ]
            ),
            dbc.Row(
                [                  
                  dbc.Col(
                    dbc.Card (
                      [
                        dbc.CardHeader("Appraisal"),  
                        dbc.CardBody(dcc.Graph(figure=appraisal_fig),
                        ),
                      ]
                    ),
                    width=6,
                  ),
                dbc.Col(
                  dbc.Card (
                    [
                    dbc.CardHeader("Reappraisal") , 
                    dbc.CardBody(dcc.Graph(
                    figure=reappraisal_fig.update_traces(width=0.3)))
                    ]
                  ),
                  width=6,
                ),  
              ],
              className="mb-4",
            ),
             dbc.Row(
              [                  
                dbc.Col(
                  dbc.Card (
                    [
                      dbc.CardHeader("Appraisal Score Breakdown"),  
                      dbc.CardBody(dcc.Graph(figure=appraisal_score_fig),
                      ),
                    ]
                  ),
                  width=6,
                ),
                dbc.Col(
                  dbc.Card( 
                    [
                    dbc.CardHeader("Cost Index Breakdown") , 
                    dbc.CardBody(dcc.Graph(
                    figure=cost_index_fig))
                      ]
                  ),
                width=6,
              ),
            ]
          ),
        ],
      fluid=True,
    )