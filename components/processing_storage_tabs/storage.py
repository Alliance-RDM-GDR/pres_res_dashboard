import dash_bootstrap_components as dbc
from dash import html, dcc

from components.charts import create_line_chart
from components.cards import create_kpi_card

# ---------------------------------------------------
# Storage Tab Layout
# ---------------------------------------------------
def layout(df, metrics):
    
    storage_fig = create_line_chart(
        df,
        "Year",
        "Total Storage (TB)",
        "Storage Growth Over Time"
    )

    aip_fig = create_line_chart(
        df,
        "Year",
        "Total AIPs",
        "AIP Growth Over Time"
    )

    return dbc.Container(
        [
           dbc.Row(
            [
              html.H2(
                  "Storage and AIPs Overview",
                  className="mb-4"
              ),
              html.P("The graphs provide storage and AIP creation trends. The KPI cards provide information related to the percentage of AIPs created in relation to the total number of published datasets. The storage KPI cards provides the total storage used against the total storage allocation at SciNet (500 TB).")
  
            ]
          ), 

          dbc.Row(
            [
              dbc.Col(create_kpi_card("Total Storage", f'{metrics["total_storage"]} TB'), width=3),
              dbc.Col(create_kpi_card("Percentage of Storage", f'{metrics["total_storage_percentage"]} %'), width=3),
              dbc.Col(create_kpi_card("Total AIPs", metrics["total_aips"]), width=3),
              dbc.Col(create_kpi_card("Percentage of Datasets", f'{metrics["total_aips_percentage"]} %'), width=3),
            ],
            className="mb-4",
        ),  
         
          dbc.Row(
            [
              dbc.Col(
                dbc.Card (
                  [
                  dbc.CardHeader("Storage Trend (TB)"),
                  dbc.CardBody(dcc.Graph(
                      figure=storage_fig
                      ),
                    ),
                   ]
                ),
                 width=6,
              ),
              dbc.Col(
                dbc.Card ([  
                dbc.CardHeader("AIP Growth"),
                dbc.CardBody(dcc.Graph(
                  figure=aip_fig
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
