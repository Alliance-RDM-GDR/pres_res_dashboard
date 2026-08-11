import dash
from dash import html, callback, Output, Input
import dash_bootstrap_components as dbc

from utils.data_loader import load_dataset_metrics_data,load_dataset_size_data

from components.dataset_metrics_tabs import (
    overview,
    field_of_research,
    funder_information,
    licenses,
)

# ---------------------------------------------------
# Register Page
# ---------------------------------------------------
dash.register_page(__name__, path="/dataset-metrics", name="Dataset Metrics")

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
for_df = load_dataset_metrics_data()
funder_df = load_dataset_metrics_data()
license_df = load_dataset_metrics_data()
geo_df = load_dataset_metrics_data()
size_range_df = load_dataset_size_data()

# ---------------------------------------------------
# Tab Definitions
# ---------------------------------------------------
DATASET_METRICS_TABS = [
    {"label": "Overview", "value": "overview"},
    {"label": "Field of Research", "value": "field_of_research"},
    {"label": "Funder Information", "value": "funder_information"},
    {"label": "Licenses", "value": "licenses"}
]
# ---------------------------------------------------
# Page Layout
# ---------------------------------------------------
layout = dbc.Container(
    [
        # Page Header
        html.H1("Dataset Metrics Dashboard", className="mb-3"),
        # Tabs
        dbc.Tabs(
            [
                dbc.Tab(label=tab["label"], tab_id=tab["value"])
                for tab in DATASET_METRICS_TABS
            ],
            id="dataset-metrics-tabs",
            active_tab="overview",
        ),
        # Tab Content Placeholder
        dbc.Row([dbc.Col(html.Div(id="dataset-metrics-tab-content", className="mt-4"))]),
    ],
    fluid=True,
)

# ---------------------------------------------------
# Callbacks
# ---------------------------------------------------
@callback(
  Output(
      "dataset-metrics-tab-content",
      "children"
  ),

  Input(
      "dataset-metrics-tabs",
      "active_tab"
  )
)
def render_dataset_metrics_tab(active_tab):
  if active_tab == "overview":
    return overview.layout(
    geo_df, size_range_df
  )

  elif active_tab == "field_of_research":
    return field_of_research.layout(
      for_df
  )
  elif active_tab == "funder_information":
    return funder_information.layout(
      funder_df,
  )
  elif active_tab == "licenses":
    return licenses.layout(
      license_df,
  )


