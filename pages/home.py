import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from utils.data_loader import load_processing_storage, load_format_level_data, load_appraisal_data

from utils.calculations import processing_metrics, risk_levels, preservation_levels, get_recommendation_kpis

from components.cards import create_kpi_card

from components.charts import create_ranking_chart, create_donut_chart

# ------------------------------------
# Register page
# ------------------------------------
dash.register_page(__name__, path="/", name="Home")

# ------------------------------------
# Load Data
# ------------------------------------
df = load_processing_storage()
levels_df = load_format_level_data()
appraisal_df = load_appraisal_data()

risk_counts = risk_levels(levels_df)
preservation_counts = preservation_levels(levels_df)
metrics = processing_metrics(df)
recommendation_kpis = get_recommendation_kpis(appraisal_df)

# ------------------------------------
# Layout
# ------------------------------------
recommendation_fig = create_donut_chart(
      appraisal_df,
      "preservation_recommendation",
      "recommendation_totals",
      "Preservation Recommendations Breakdown",
    )
risk_fig = create_ranking_chart(
    risk_counts, "Risk Level", "Number of Files", "Risk Levels"
)

risk_colors = {"Low": "#154a4a", "Medium": "#D6AB00", "High": "#B3021A"}

risk_fig.update_traces(
    width=0.4,
    marker_color=[
        risk_colors.get(level, "#D6AB00") for level in risk_counts["Risk Level"]
    ],
)

pres_fig = create_ranking_chart(
    preservation_counts, "Preservation Level", "Number of Files", "Preservation Levels"
)

pres_colors = {"Full": "#154a4a", "Watch": "#D6AB00", "Basic": "#B3021A"}

pres_fig.update_traces(
    width=0.4,
    marker_color=[
        pres_colors.get(level, "#D6AB00")
        for level in preservation_counts["Preservation Level"]
    ],
)

layout = dbc.Container(
    [
        html.H1("Digital Preservation Services Analytics Portal"),
        # KPI ROW
        dbc.Row(
            [
                html.P("Last updated: 2026-08-04 | Next update: 2026-10-06", className="mb-4"),
                html.H2("Highlights"),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    create_kpi_card(
                        "Total Datasets Completed", metrics["total_completed"]
                    ),
                    width=3,
                ),
                dbc.Col(
                    create_kpi_card(
                        "Total Datasets Processed", metrics["total_processed"]
                    ),
                    width=3,
                ),
                dbc.Col(create_kpi_card("Total AIPs", metrics["total_aips"]), width=3),
                dbc.Col(
                    create_kpi_card("Total Storage", f'{metrics["total_storage"]} TB'),
                    width=3,
                ),
            ],
            className="mb-4",
        ),
        # CHART ROW 1
        dbc.Row(
            [
                dbc.Col(
                    html.H3("Risk Overview"),
                    width=12,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader("Risk Levels"),
                            dbc.CardBody(
                                dcc.Graph(figure=risk_fig, style={"height": "400px"}),
                            ),
                        ]
                    ),
                    width=6,
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader("Preservation Levels"),
                            dbc.CardBody(
                                dcc.Graph(figure=pres_fig, style={"height": "400px"}),
                            ),
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
                    html.H3("Preservation Recommendations"),
                    width=12,
                ),
            ]
        ),
        dbc.Row(
            [                   
              dbc.Col(
                dbc.Card( 
                  [
                  dbc.CardHeader("Preservation Recommendations") , 
                  dbc.CardBody(dcc.Graph(figure=recommendation_fig), style={"height": "400px"})
                  ],
                  className="h-100"
                ),
                width=6,
              ),
              dbc.Col(
                [
                dbc.Row(
                [
                  dbc.Col(
                    create_kpi_card(
                    "Prioritize preservation", recommendation_kpis["Prioritize preservation"]
                  ),
                    width=6,
                ),
                dbc.Col(
                  create_kpi_card(
                  "Preserve - Resources", recommendation_kpis["Preserve - plan resources"]
                ),
                  width=6,
              ),
              ],
              className="mb-4"
            ),
                  dbc.Row(
                  [
                    dbc.Col(
                      create_kpi_card(
                      "Consider Preservation", recommendation_kpis["Consider preservation"]
                    ),
                      width=6,
                  ),
                  dbc.Col(
                    create_kpi_card(
                    "Review", recommendation_kpis["Review"]
                    ),
                    width=6,
                  ),
                ],
                className="mb-4",
              ),
              
              dbc.Row(
                [
                  dbc.Col(
                    create_kpi_card(
                    "Low Priority", recommendation_kpis["Low priority"]
                  ),
                    width=6,
                ),
                dbc.Col(
                  create_kpi_card(
                  "Do Not Prioritize", recommendation_kpis["Do not prioritize"]
                ),
                  width=6,
                ),
              ],
            ),
            ],
            width=6,
            className="d-flex flex-column h-100",
            ),
            
          ],
          className="mb-4 align-items-stretch"
        ),
    ],
    fluid=True,
)
