import dash_bootstrap_components as dbc
from dash import html, dcc

from components.cards import create_kpi_card

from components.charts import create_donut_chart

# ---------------------------------------------------
# Dataset Metrics Tab Layout
# ---------------------------------------------------
def layout(geo_df, size_range_df):
  filtered_df = geo_df[geo_df["Canadian Province"].notnull()]

  geo_fig = create_donut_chart (
    filtered_df,
    "Canadian Province",
    "Total Datasets",
    "Canadian Geographic Distribution"
  )

  size_summary = (
      size_range_df["size_range"]
      .value_counts()
      .sort_index()
      .reset_index()
  )

  size_summary.columns = ["size_range", "total"]

  size_fig = create_donut_chart(
      size_summary,
      "size_range",
      "total",
      "Dataset Size Range"
  )

  size_summary = (
        size_range_df["size_range"]
        .value_counts()
        .sort_index()
        .reset_index()
    )
  
  size_summary.columns = ["size_range", "total"]
  
  aip_fig = create_donut_chart(
        size_summary,
        "size_range",
        "total",
        "AIP Size Range"
    )
  
  file_summary = (
    size_range_df["file_count_range"]
    .value_counts()
    .sort_index()
    .reset_index()
    )

  file_summary.columns = ["file_count_range", "total"]
  file_fig = create_donut_chart(
        file_summary,
        "file_count_range",
        "total",
        "Datasets by Number of Files"
    )






  return dbc.Container(
    [
      dbc.Row(
        [
            html.H2(
              "Dataset Metrics Overview",
            ),
        ],
      className="mb-4"
      ),  
        dbc.Row(
          [
            dbc.Col([
              dbc.Row([
                 dbc.Col(create_kpi_card("Published Datasets", geo_df["total_published_datasets"]), width=12,className="mb-4"),
              ]),
              dbc.Row([
                dbc.Col(create_kpi_card("Total Versioned Datasets", geo_df["versioned"]), width=12,className="mb-4"),
                ]),
              ], width=4),

            dbc.Col(
              dbc.Card (
                [
                  dbc.CardHeader("Canadian Geographic Distributions"),  
                  dbc.CardBody(dcc.Graph(figure=geo_fig),
                  ),
                ]
              ),
              width=8,
            ),
          ],
          className="mb-4"
        ),
        dbc.Row ([
           html.P("Dataset size and number of files are all calculated based on the extracted content."),

        ]),
        dbc.Row(
          [
            
            dbc.Col(
                dbc.Card (
                  [
                    dbc.CardHeader("Dataset Size Distribution"),  
                    dbc.CardBody(
                      dcc.Graph(figure=size_fig),
                  ),
                  ]
                ),
                width=6,
              ),
               dbc.Col(
                dbc.Card (
                  [
                    dbc.CardHeader("Dataset File Count Distribution"),  
                    dbc.CardBody(
                      dcc.Graph(figure=file_fig),
                  ),
                  ]
                ),
                width=6,
              ),
              
            ],
            className="mb-4"
          ), 
      ],
    fluid=True,
  )