import dash_bootstrap_components as dbc
from dash import html, dcc

from components.cards import create_kpi_card
from components.charts import create_ranking_chart
from utils.calculations import group_totals

# ---------------------------------------------------
# Field of Research Tab Layout
# ---------------------------------------------------
def layout(for_df):
  for_fig = create_ranking_chart (
    for_df,
    "crdc_group",
    "group_total",
    "Top 20 CRDC Groups"
  )
  class_fig = create_ranking_chart (
      for_df,
      "crdc_class",
      "class_total",
      "Top 20 CRDC Class"
    )
  field_fig = create_ranking_chart (
        for_df,
        "crdc_field",
        "field_total",
        "Top 20 CRDC Field"
      )
  totals = group_totals(for_df)

  return dbc.Container(
        [
          dbc.Row(
            [
              html.H2(
                "Field of Research Metrics",
              ),
            ],
          className="mb-4"
        ), 
        dbc.Row (
          [
           dbc.Col(
            create_kpi_card(
              "Natural sciences", totals.get("Natural sciences", 0)
            ),
              width=2,
           ),  
           dbc.Col(
            create_kpi_card(
              "Eng. and tech", totals.get("Engineering and technology", 0)
            ),
              width=2,
          ),  
          dbc.Col(
            create_kpi_card(
              "Med. and health", totals.get("Medical and health sciences", 0)
            ),
              width=2,
            ), 
            dbc.Col(
              create_kpi_card(
              "Agri. and Vet", totals.get("Agricultural and veterinary sciences", 0)
              ),
              width=2,
            ), 
            dbc.Col(
              create_kpi_card(
                "Social sciences", totals.get("Social sciences", 0)
              ),
               width=2,
            ), 
            dbc.Col(
              create_kpi_card(
                "Humanities/Arts", totals.get("Humanities and the arts", 0)
              ),
                width=2,
            ), 
          ], className="mb-4"
        ), 
        dbc.Row(
          [
            dbc.Col(
              dbc.Card (
                [
                  dbc.CardHeader("CRDC Group Overview"),  
                  dbc.CardBody(dcc.Graph(figure=for_fig),
                  ),
                ]
              ),
              width=12,
            ),
          ],
          className="mb-4"
        ),
        dbc.Row(
          [
            dbc.Col(
              dbc.Card (
                [
                  dbc.CardHeader("CRDC Class Overview"),  
                  dbc.CardBody(dcc.Graph(figure=class_fig),
                  ),
                ]
              ),
              width=12,
            ),
          ],
          className="mb-4"
        ), 
      dbc.Row(
        [
          dbc.Col(
            dbc.Card (
              [
                dbc.CardHeader("CRDC Field Overview"),  
                dbc.CardBody(dcc.Graph(figure=field_fig),
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