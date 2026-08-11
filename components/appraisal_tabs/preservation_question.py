import dash_bootstrap_components as dbc
from dash import html, dcc

from components.cards import create_kpi_card

# ---------------------------------------------------
# Preservation Question Tab
# ---------------------------------------------------
def layout(pres_df):

    return dbc.Container(
        [
           dbc.Row(
              [
                  html.H2(
                      "Long-Term Preservation Question",
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

        # -----------------------------
        # Filters
        # -----------------------------
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Year"),

                        dcc.Dropdown(
                            id="pq-year-selector",
                            options=[
                                {
                                    "label": year,
                                    "value": year
                                }
                                for year in pres_df["Year"]
                            ],
                            value=pres_df["Year"].iloc[-1],
                            clearable=False,
                        ),
                    ],
                    width=4,
                ),
            ],
            className="mb-4"
        ),

        # -----------------------------
        # KPI Cards
        # -----------------------------
        dbc.Row(
            [

                dbc.Col(
                    create_kpi_card(
                        "Total Datasets",
                        html.Span(id="pq-total-datasets")
                    ),
                    width=2,
                    className="offset-1",
                ),

                dbc.Col(
                    create_kpi_card(
                        "Yes %",
                        html.Span(id="pq-yes-percent")
                    ),
                    width=2
                ),

                dbc.Col(
                    create_kpi_card(
                        "No %",
                        html.Span(id="pq-no-percent")
                    ),
                    width=2
                ),

                dbc.Col(
                    create_kpi_card(
                        "Unsure %",
                        html.Span(id="pq-unsure-percent")
                    ),
                    width=2
                ),

                dbc.Col(
                    create_kpi_card(
                        "No Response %",
                        html.Span(id="pq-no-response-percent")
                    ),
                    width=2
                ),

            ],
            className="mb-2"
        ),

        dbc.Row(
            [
                dbc.Col(
                    html.Small(
                        "*The Unsure option was introduced in 2023.",
                        
                    )
                )
            ],
            className="mb-2"
        ),

        # -----------------------------
        # Distribution Charts
        # -----------------------------
        dbc.Row(
            [

                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                "Year Distribution",
                                id="card-header-title",
                            ),

                            dbc.CardBody(
                                dcc.Graph(
                                    id="pq-distribution-chart"
                                )
                            ),
                        ]
                    ),
                    width=6
                ),

                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                "Dataset Volume"
                            ),

                            dbc.CardBody(
                                dcc.Graph(
                                    id="pq-volume-chart"
                                )
                            ),
                        ]
                    ),
                    width=6
                ),

            ],
            className="mb-4"
        ),

        # -----------------------------
        # Trend Controls
        # -----------------------------
        dbc.Row(
            [

            dbc.Col(
                dbc.Card(
                    [
                       dbc.CardHeader(
                            "Metric"
                      ),

                    dbc.CardBody(
                        dcc.RadioItems(
                            id="pq-metric-selector",

                            options=[
                                {
                                    "label": "Percentages",
                                    "value": "percentage"
                                },
                                {
                                    "label": "Counts",
                                    "value": "count"
                                }
                            ],

                            value="percentage",
                            inline=True,
                        )
                        ),
                    ]
                    ),
                    width=2
                ),

                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                "Annual Response Trend"
                            ),

                            dbc.CardBody(
                                dcc.Graph(
                                    id="pq-trend-chart"
                                )
                            ),
                        ]
                    ),
                    width=10
                ),

            ]
        )

      ],
      fluid=True
    )