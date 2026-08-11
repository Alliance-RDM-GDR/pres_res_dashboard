import dash
from dash import html, callback, Output, Input
import dash_bootstrap_components as dbc

from utils.data_loader import (
    load_appraisal_data,
    # load_appraisal_form_data,
    load_pres_question_data,
    reshape_appraisal_data,
    get_decision_data   
)

from utils.calculations import (
    calculate_appraisal_metrics,
    calculate_appraisal_trend,
)

from components.appraisal_tabs import (
    overview,
    decisions,
    preservation_question,
)

# ---------------------------------------------------
# Register Page
# ---------------------------------------------------
dash.register_page(__name__, path="/appraisal", name="Appraisal")

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
appraisal_df = load_appraisal_data()
pres_df = load_pres_question_data()
# form_df = load_appraisal_form_data()

# Create chart-ready dataframe
df_long = reshape_appraisal_data(appraisal_df)

appraisal_metrics = calculate_appraisal_metrics(
    appraisal_df
)
appraisal_trend_df = calculate_appraisal_trend(
    appraisal_df
)

# ---------------------------------------------------
# Decision Chart Data
# ---------------------------------------------------
appraisal_decisions_df = get_decision_data(
    df_long,
    "Appraisal"
  )
reappraisal_decisions_df = get_decision_data(
    df_long,
    "Reappraisal"
  )

# ---------------------------------------------------
# Tab Definitions
# ---------------------------------------------------
APPRAISAL_TABS = [
    {"label": "Overview", "value": "overview"},
    {"label": "Appraisal & Reappraisal", "value": "decisions"},
    {"label": "Preservation Question", "value": "preservation-question"},
]
# ---------------------------------------------------
# Page Layout
# ---------------------------------------------------
layout = dbc.Container(
    [
        # Page Header
        html.H1("Appraisal Dashboard", className="mb-3"),
        # Tabs
        dbc.Tabs(
            [
                dbc.Tab(label=tab["label"], tab_id=tab["value"])
                for tab in APPRAISAL_TABS
            ],
            id="appraisal-tabs",
            active_tab="overview",
        ),
        # Tab Content Placeholder
        dbc.Row([dbc.Col(html.Div(id="appraisal-tab-content", className="mt-4"))]),
    ],
    fluid=True,
)

# ---------------------------------------------------
# Callbacks
# ---------------------------------------------------
@callback(
  Output(
      "appraisal-tab-content",
      "children"
  ),

  Input(
      "appraisal-tabs",
      "active_tab"
  )
)
def render_appraisal_tab(active_tab):
  if active_tab == "overview":
    return overview.layout(
      appraisal_metrics,
      appraisal_trend_df,
  )
  elif active_tab == "decisions":
    return decisions.layout(
      appraisal_decisions_df,
      reappraisal_decisions_df,
      appraisal_df
    )

  elif active_tab == "preservation-question":
    return preservation_question.layout(
      pres_df
    )
