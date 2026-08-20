import dash_bootstrap_components as dbc
from dash import html

from components.tables import create_crosstab

# ---------------------------------------------------
# CRDC Mapping Tab Layout
# ---------------------------------------------------
def layout(df):
    mapping_df = df  
    mapping_table = create_crosstab(
        mapping_df,
        table_id="CRDC-Format Mapping",
        # height="750px",
    )

    return dbc.Container(
        [
          dbc.Row(
            [
              html.H2(
                  "CRDC-Format Mapping",
              ),
              html.P("The crosstab table maps formats to CRDC Classes.")
            ],
        ), 
        dbc.Row(
          [
            dbc.Col(
              dbc.Card (
                [
                dbc.CardHeader("Format to CRDC Class"),
                dbc.CardBody(mapping_table),
                  ]
              ),
                width=12,
            ),

            ],

            ),  
      ],
    fluid=True,
  )