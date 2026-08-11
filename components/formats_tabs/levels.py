import dash_bootstrap_components as dbc
from dash import html, dcc

from utils.calculations import (
    risk_levels,
    preservation_levels,
)

from components.charts import create_bar_chart
from components.cards import create_kpi_card
# ---------------------------------------------------
# Format Levels Layout
# ---------------------------------------------------
def layout(df):

  risk_counts = risk_levels(df)
  preservation_counts = preservation_levels(df)

  risk_fig = create_bar_chart(
  risk_counts, "Risk Level", "Number of Files", "Risk Levels"
)

  risk_colors = {"Low": "#154a4a", "Medium": "#D6AB00", "High": "#B3021A"}

  risk_fig.update_traces(
    width=0.4,
    marker_color=[
        risk_colors.get(level, "#D6AB00") for level in risk_counts["Risk Level"]
    ],
)

  pres_fig = create_bar_chart(
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
    
  return dbc.Container(
    [

      dbc.Row(
        [
            html.H2(
                "Formats Levels",
                className="mb-4"
            ),

              html.P(
                """
                This tab includes the total number of identified files, the total number of files in the Digital Preservation Action Plan, the total unknown formats and the total number of files without an extension. The graphs provide and overview of how many formats are assigned a high, moderate, or low risk level and how many formats are in each preservation level.
                """
              ),
          ]
            ),
          dbc.Row(
            [
              dbc.Col(create_kpi_card("Total Identified", df["Total Identified"]), width=3),
              dbc.Col(create_kpi_card("Total in Action Plan", df["Total in Action Plan"]), width=3),
              dbc.Col(create_kpi_card("Total Unknown (extension)", df["Total Unknown (extension)"]), width=3),
               dbc.Col(create_kpi_card("Total No Extensions (files)", df["Total No Extensions (files)"]), width=3),
            ],
            className="mb-4",
        ),  
         
          dbc.Row(
            [
              dbc.Col(
                dbc.Card (
                  [
                  dbc.CardHeader("Risk Levels"),
                  dbc.CardBody(dcc.Graph(
                      figure=risk_fig
                      ),
                    ),
                   ]
                ),
                 width=6,
              ),
              dbc.Col(
                dbc.Card ([  
                dbc.CardHeader("Preservation Levels"),
                dbc.CardBody(dcc.Graph(
                  figure=pres_fig
                  ),
                ),
              ]
            ),
            width=6, 
            ),
          ]
        ),
      ],
      fluid=True,
  )
