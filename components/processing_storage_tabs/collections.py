import dash_bootstrap_components as dbc
from dash import html, dcc

from components.cards import create_kpi_card

from components.charts import create_100_percent_stacked_bar

# ---------------------------------------------------
# Processing Tab Layout
# ---------------------------------------------------

def layout(collection_df):
    collection_fig= create_100_percent_stacked_bar(
      collection_df,
      category="Collection",
      value="Percentage Processed",
      processed_label="Processed",
      remaining_label="Remaining",
)

    return dbc.Container(
        [
          dbc.Row(
            [
              html.H2(
                  "Collections Processing Status",
              ),
              html.P("The graph provides a breakdown of the number of datasets in each collection that have gone through preservation processing.")
            ],
        ), 
        dbc.Row(
          [
            dbc.Col(
              dbc.Card (
                [
                dbc.CardHeader("Processing by Collections"),
                dbc.CardBody(dcc.Graph(
                    figure=collection_fig
                    ),
                  ),
                  ]
              ),
                width=12,
            ),

            ],

            ),  
      ],
    fluid=True,
  )