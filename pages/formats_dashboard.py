import dash
from dash import html, callback, Output, Input
import dash_bootstrap_components as dbc

from utils.data_loader import load_format_level_data, load_format_id_data, load_crdc_format_stats_data

from utils.calculations import (
    risk_levels,
    preservation_levels,
)

from components.formats_tabs import (
    overview,
    levels,
    mapping,
)

# ---------------------------------------------------
# Register Page
# ---------------------------------------------------
dash.register_page(__name__, path="/formats", name="Formats")

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
df = load_format_level_data()
id_df = load_format_id_data()

risk_counts = risk_levels(df)
preservation_counts = preservation_levels(df)
mapping_df = load_crdc_format_stats_data()

# ---------------------------------------------------
# Tab Definitions
# ---------------------------------------------------
FORMAT_TABS = [
    {"label": "Overview", "value": "overview"},
    {"label": "Format Levels", "value": "levels"},
    {"label": "Mapping", "value": "mapping"},
]
# ---------------------------------------------------
# Page Layout
# ---------------------------------------------------
layout = dbc.Container(
    [
        # Page Header
        html.H1("Format Dashboard", className="mb-3"),
        # Tabs
        dbc.Tabs(
            [
                dbc.Tab(label=tab["label"], tab_id=tab["value"])
                for tab in FORMAT_TABS
            ],
            id="format-tabs",
            active_tab="overview",
        ),
        # Tab Content Placeholder
        dbc.Row([dbc.Col(html.Div(id="format-tab-content", className="mt-4"))]),
    ],
    fluid=True,
)

# ---------------------------------------------------
# Callbacks
# ---------------------------------------------------
@callback(
  Output(
      "format-tab-content",
      "children"
  ),

  Input(
      "format-tabs",
      "active_tab"
  )
)
def render_formats_tab(active_tab):
  if active_tab == "overview":
    return overview.layout(
    id_df
  )

  elif active_tab == "levels":
    return levels.layout(
      df
    )
  elif active_tab == "mapping":
      return mapping.layout(
        mapping_df
      )
