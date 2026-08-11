import dash_bootstrap_components as dbc
from dash import html, dcc

from components.cards import create_kpi_card

from components.charts import create_line_chart

# ---------------------------------------------------
# Processing Tab Layout
# ---------------------------------------------------

def layout(df, status_df):

    fpres_fig = create_line_chart(
            df,
            "Year",
            "Total Dataset FPRES",
            "Transferred to DPS"
        )

    return dbc.Container(
        [
          dbc.Row(
            [
              html.H2(
                  "Processing and Status Overview",
              ),
            ],
          className="mb-4"
        ),
       dbc.Row(
        [                   
          dbc.Col(
            dbc.Card( 
              [
              dbc.CardHeader("Transfers to DPS") , 
              dbc.CardBody(dcc.Graph(figure=fpres_fig))
              ],
              className="h-100"
            ),
            width=8,
          ),
          dbc.Col(
            [
            dbc.Row(
            [
              dbc.Col(
                create_kpi_card(
                "File Listing", status_df["file_listing"]
              ),
                width=6,
            ),
            dbc.Col(
              create_kpi_card(
              "Appraisal", status_df["appraisal"]
            ),
              width=6,
          ),
          ],
          className="mb-2"
        ),
          dbc.Row(
          [
          dbc.Col(
              create_kpi_card(
              "Queued", status_df["queued"]
            ),
              width=6,
          ),
          dbc.Col(
            create_kpi_card(
            "Processing", status_df["processing"]
            ),
            width=6,
          ),
        ],
        className="mb-2",
        ),
          
        dbc.Row(
          [
              dbc.Col(
                create_kpi_card(
                "Archival Storage", status_df["storage"]
              ),
                width=6,
            ),
            dbc.Col(
              create_kpi_card(
              "Reappraisal", status_df["reappraisal"]
            ),
              width=6,
            ),
          ],className="mb-2",
        ),
        dbc.Row(
          [
              dbc.Col(
                create_kpi_card(
                "Reprocess", status_df["reprocess"]
              ),
                width=6,
            ),
            dbc.Col(
              create_kpi_card(
              "Backlog", status_df["backlog"]
            ),
              width=6,
            ),
          ],
        ),
        ],
        width=4,
        className="d-flex flex-column h-100",
      ),
                     
      ],
      className="mb-4 align-items-stretch"
      ),   
      ],
    fluid=True,
  )