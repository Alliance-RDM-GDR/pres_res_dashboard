import dash_bootstrap_components as dbc
from dash import html, dcc

from components.cards import create_kpi_card

from components.charts import create_bar_chart

# ---------------------------------------------------
# License Tab Layout
# ---------------------------------------------------
def layout(license_df):
  licenses_fig = create_bar_chart (
    license_df,
    "license",
    "license_total",
    "Licenses Overview"
  )

  return dbc.Container(
        [
          dbc.Row(
            [
                html.H2(
                  "Licenses Breakdown",
                ),
            ],
          className="mb-4"
        ),  
        dbc.Row(
          [
            dbc.Col(
              dbc.Card (
                [
                  dbc.CardHeader("Licences Breakdown"),  
                  dbc.CardBody(dcc.Graph(figure=licenses_fig),
                  ),
                ]
              ),
              width=12,
            ),
          ],
          className="mb-4"
        ),  
  
      ],
    fluid=True,
  )