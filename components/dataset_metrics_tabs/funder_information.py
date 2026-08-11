import dash_bootstrap_components as dbc
from dash import html, dcc

from components.cards import create_kpi_card
from components.tables import create_data_table

# ---------------------------------------------------
# Funder Tab Layout
# ---------------------------------------------------
def layout(funder_df):
  funder_columns = funder_df[["funders", "funder_total"]]

  funder_table = create_data_table(
    funder_columns,
    table_id="funders",
    page_size=40
  )

  return dbc.Container(
    [
      dbc.Row(
        [
          html.H2(
            "Funder Metrics",
          ),
        ],
        className="mb-4"
        ),  
        dbc.Row(
          [
            dbc.Col(
              dbc.Card (
                [
                  dbc.CardHeader("Funder Overview"),  
                  dbc.CardBody(funder_table),
                ]
              ),width=12,
            ),
          ]
        ), 
  
      ],
    fluid=True,
  )