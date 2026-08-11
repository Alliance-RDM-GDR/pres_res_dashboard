import dash_bootstrap_components as dbc
from dash import html

def create_kpi_card(title, value):
  return dbc.Card(
    [
      dbc.CardHeader(
          title
      ),

      dbc.CardBody(
          [
              html.P(
                  value,
              )
          ]
      )
    ],
    inverse=True,
    className="h-100"
  )