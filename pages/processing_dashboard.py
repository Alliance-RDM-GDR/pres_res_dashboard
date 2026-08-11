import dash
from dash import html, callback, Output, Input
import dash_bootstrap_components as dbc

from utils.data_loader import load_processing_storage, load_status_backlog_data, load_dataset_size_data

from utils.calculations import processing_metrics

from components.processing_storage_tabs import (
    overview,
    processing,
    storage,
)

# ---------------------------------------------------
# Register Page
# ---------------------------------------------------
dash.register_page(
    __name__,
    path="/processing-storage",
    name="Processing and Storage"
)

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
df = load_processing_storage()
status_df = load_status_backlog_data()

metrics = processing_metrics(df)
size_range_df = load_dataset_size_data()

# ---------------------------------------------------
# Tab Definitions
# ---------------------------------------------------
PROCESSING_TABS = [
    {"label": "Overview", "value": "overview"},
    {"label": "Processing", "value": "processing"},
    {"label": "Storage", "value": "storage"},
]

# ---------------------------------------------------
# Page Layout
# ---------------------------------------------------
layout = dbc.Container(
    [
        html.H1(
            "Processing and Storage Dashboard",
            className="mb-3"
        ),

        dbc.Tabs(
            [
                dbc.Tab(
                    label=tab["label"],
                    tab_id=tab["value"]
                )
                for tab in PROCESSING_TABS
            ],
            id="processing-tabs",
            active_tab="overview",
        ),

        dbc.Row(
          [
            dbc.Col(
                html.Div(
                    id="processing-tab-content",
                    className="mt-4"
                )
            )
          ]
        ),

    ],
    fluid=True,
)


# ---------------------------------------------------
# Tab Callback
# ---------------------------------------------------
@callback(
    Output(
        "processing-tab-content",
        "children"
    ),
    Input(
        "processing-tabs",
        "active_tab"
    )
)
def render_processing_tab(active_tab):

    if active_tab == "overview":
        return overview.layout(df, status_df)

    elif active_tab == "processing":
        return processing.layout(df, size_range_df)

    elif active_tab == "storage":
        return storage.layout(df, metrics)