import dash_bootstrap_components as dbc

from dash import html, dcc

from components.cards import create_kpi_card
from components.charts import create_donut_chart

# ---------------------------------------------------
# Dataset Processing Tab
# ---------------------------------------------------

def layout(processing_df, size_range_df):
    size_summary = (
          size_range_df["size_range"]
          .value_counts()
          .sort_index()
          .reset_index()
      )
    
    size_summary.columns = ["size_range", "total"]
    
    aip_fig = create_donut_chart(
          size_summary,
          "size_range",
          "total",
          "AIP Size Range"
      )

    return dbc.Container(
        [

# -----------------------------
# Header
# -----------------------------

    dbc.Row(
        [
            html.H2(
                "Dataset Processing",
                className="mb-4"
            ),

            html.P(
                """
                This dashboard provides an overview of annual
                dataset processing activity, including AIPs generated,
                datasets processed, datasets reprocessed,
                and datasets reviewed.
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
            id="dp-year-selector",
        options=[
        {
            "label": str(int(year)),
            "value": int(year)
        }
        for year in processing_df["Year"]
        if year >= 2020
    ],

    value=int(
        processing_df.loc[
            processing_df["Year"] >= 2020,
            "Year"
        ].max()
    ),

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
                            "Total AIPs",
                            html.Span(
                                id="dp-total-aips"
                            )
                        ),
                        width=3,
                    ),

                    dbc.Col(
                        create_kpi_card(
                            "Datasets Processed",
                            html.Span(
                                id="dp-datasets-processed"
                            )
                        ),
                        width=3,
                    ),

                    dbc.Col(
                        create_kpi_card(
                            "Datasets Reprocessed",
                            html.Span(
                                id="dp-datasets-reprocessed"
                            )
                        ),
                        width=3,
                    ),

                    dbc.Col(
                        create_kpi_card(
                            "Datasets Completed",
                            html.Span(
                                id="dp-datasets-completed"
                            )
                        ),
                        width=3,
                    ),

                ],
                className="mb-4"
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
                                  "Processing Distribution",
                                  id="dp-card-header-title",
                              ),

                              dbc.CardBody(
                                  dcc.Graph(
                                      id="dp-distribution-chart"
                                  )
                              ),
                            ]
                        ),
                        width=6
                    ),

                    dbc.Col(
                      dbc.Card (
                        [
                          dbc.CardHeader("AIP Size Distribution"),  
                          dbc.CardBody(
                            dcc.Graph(figure=aip_fig),
                        ),
                        ]
                      ),
                      width=6,
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
                                  id="dp-metric-selector",

                                  options=[
                                    {
                                      "label": "Counts",
                                      "value": "count"
                                    },
                                    {
                                      "label": "Percentage",
                                      "value": "percentage"
                                    }
                                  ],

                                  value="count",
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
                                    "Annual Processing Trend"
                                ),

                                dbc.CardBody(
                                    dcc.Graph(
                                        id="dp-trend-chart"
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
# import dash_bootstrap_components as dbc

# from dash import html, dcc

# from components.cards import create_kpi_card

# # ---------------------------------------------------
# # Processing Tab Layout
# # ---------------------------------------------------
# def layout(processing_df):

#     return dbc.Container(
#         [

#             # ---------------------------------------------------
#             # Dataset Processing Tab
#             # ---------------------------------------------------

#             dbc.Row(
#                 [
#                     html.H2(
#                         "Dataset Processing",
#                         className="mb-4"
#                     ),

#                     html.P(
#                         """
#                         This dashboard provides an overview of dataset
#                         processing activity, including AIPs, datasets
#                         processed, reprocessed, completed datasets,
#                         FPRES, and storage volume.
#                         """
#                     ),
#                 ]
#             ),

#             # -----------------------------
#             # Filters
#             # -----------------------------

#             dbc.Row(
#                 [
#                     dbc.Col(
#                         [
#                             html.Label("Year"),

#                             dcc.Dropdown(
#                                 id="dp-year-selector",
#                                 options=[
#                                     {
#                                         "label": year,
#                                         "value": year
#                                     }
#                                     for year in processing_df["Year"]
#                                 ],
#                                 value=processing_df["Year"].iloc[-1],
#                                 clearable=False,
#                             ),
#                         ],
#                         width=4,
#                     ),
#                 ],
#                 className="mb-4"
#             ),

#             # -----------------------------
#             # KPI Cards
#             # -----------------------------

#             dbc.Row(
#                 [

#                     dbc.Col(
#                         create_kpi_card(
#                             "Total AIPs",
#                             html.Span(id="dp-total-aips")
#                         ),
#                         width=2,
#                     ),

#                     dbc.Col(
#                         create_kpi_card(
#                             "Datasets Processed",
#                             html.Span(id="dp-datasets-processed")
#                         ),
#                         width=2,
#                     ),

#                     dbc.Col(
#                         create_kpi_card(
#                             "Datasets Reprocessed",
#                             html.Span(id="dp-datasets-reprocessed")
#                         ),
#                         width=2,
#                     ),

#                     dbc.Col(
#                         create_kpi_card(
#                             "Datasets Completed",
#                             html.Span(id="dp-datasets-completed")
#                         ),
#                         width=2,
#                     ),

#                     dbc.Col(
#                         create_kpi_card(
#                             "Dataset FPRES",
#                             html.Span(id="dp-dataset-fpres")
#                         ),
#                         width=2,
#                     ),

#                     dbc.Col(
#                         create_kpi_card(
#                             "Storage (TB)",
#                             html.Span(id="dp-total-storage")
#                         ),
#                         width=2,
#                     ),

#                 ],
#                 className="mb-4"
#             ),

#             # -----------------------------
#             # Distribution Charts
#             # -----------------------------

#             dbc.Row(
#                 [

#                     dbc.Col(
#                         dbc.Card(
#                             [
#                                 dbc.CardHeader(
#                                     "Year Distribution",
#                                     id="dp-card-header-title",
#                                 ),

#                                 dbc.CardBody(
#                                     dcc.Graph(
#                                         id="dp-distribution-chart"
#                                     )
#                                 ),
#                             ]
#                         ),
#                         width=6
#                     ),

#                     dbc.Col(
#                         dbc.Card(
#                             [
#                                 dbc.CardHeader(
#                                     "Dataset Volume"
#                                 ),

#                                 dbc.CardBody(
#                                     dcc.Graph(
#                                         id="dp-volume-chart"
#                                     )
#                                 ),
#                             ]
#                         ),
#                         width=6
#                     ),

#                 ],
#                 className="mb-4"
#             ),

#             # -----------------------------
#             # Trend Controls
#             # -----------------------------

#             dbc.Row(
#                 [

#                     dbc.Col(
#                         dbc.Card(
#                             [
#                                 dbc.CardHeader(
#                                     "Metric"
#                                 ),

#                                 dbc.CardBody(
#                                     dcc.RadioItems(
#                                         id="dp-metric-selector",

#                                         options=[
#                                             {
#                                                 "label": "Counts",
#                                                 "value": "count"
#                                             },
#                                             {
#                                                 "label": "Percentage Change",
#                                                 "value": "percentage"
#                                             }
#                                         ],

#                                         value="count",
#                                         inline=True,
#                                     )
#                                 ),
#                             ]
#                         ),
#                         width=2
#                     ),

#                     dbc.Col(
#                         dbc.Card(
#                             [
#                                 dbc.CardHeader(
#                                     "Annual Processing Trend"
#                                 ),

#                                 dbc.CardBody(
#                                     dcc.Graph(
#                                         id="dp-trend-chart"
#                                     )
#                                 ),
#                             ]
#                         ),
#                         width=10
#                     ),

#                 ]
#             )

#         ],
#         fluid=True
#     )
