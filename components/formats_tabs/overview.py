import dash_bootstrap_components as dbc
from dash import html, dcc

from components.charts import create_ranking_chart
# ---------------------------------------------------
# Format Levels Layout
# ---------------------------------------------------
def layout(id_df):
  
  id_fig = create_ranking_chart(
    id_df,
    "formats_frdr",
    "total_frdr",
    "Top 20 Formats in FRDR",
    limit=20
  )
  borealis_fig = create_ranking_chart(
      id_df,
      "formats_borealis",
      "total_borealis",
      "Top 20 Formats in Borealis",
      limit=20
    )

  return dbc.Container(
        [

        dbc.Row(
            [
                html.H2(
                    "Format Overview",
                    className="mb-4"
                ),

                html.P(
                  """
                  This tab provides an overview of the top 20 formats found in the Federated Research Data Repository (FRDR) and Borealis.
                  """
                ),
            ]
        ),
        dbc.Row(
          [
            dbc.Col(
              dbc.Card (
                [
                dbc.CardHeader("Top 20 Formats - FRDR"),
                dbc.CardBody(dcc.Graph(
                    figure=id_fig
                    ),
                  ),
                  ]
              ),
                width=12,
            ),
          ], className="mb-4",
      ),
      dbc.Row(
                [
                  dbc.Col(
                    dbc.Card (
                      [
                      dbc.CardHeader("Top 20 Formats - Borealis"),
                      dbc.CardBody(dcc.Graph(
                          figure=borealis_fig
                          ),
                        ),
                        ]
                    ),
                      width=12,
                  ),
                ]
            ),
  ],
  fluid=True,
)
