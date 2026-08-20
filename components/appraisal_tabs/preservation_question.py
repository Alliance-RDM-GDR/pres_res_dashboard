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
                    All datasets submitted to FRDR will be publicly available for at least 10 years. Some datasets with long-term value (more than 10 years) will be preserved for long-term access. If you think your dataset should be retained for the long-term, you are welcome to participate in the appraisal process. Please leave a comment here indicating, for example, potential ongoing social, scientific, or historical value.
                    """
                  ),

                  html.P(
                      """
                      Do you intend for this dataset to be preserved longer than 10 years?
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
                        "Yes",
                        html.Span(id="pq-yes-percent")
                    ),
                    width=2
                ),

                dbc.Col(
                    create_kpi_card(
                        "No",
                        html.Span(id="pq-no-percent")
                    ),
                    width=2
                ),

                dbc.Col(
                    create_kpi_card(
                        "Unsure",
                        html.Span(id="pq-unsure-percent")
                    ),
                    width=2
                ),

                dbc.Col(
                    create_kpi_card(
                        "No Response",
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