import dash
from dash import callback, Output, Input

from components.appraisal_tabs import decisions
from components.charts import create_stacked_bar

from utils.data_loader import (
    load_appraisal_data,
    reshape_appraisal_data,
)
# ---------------------------------------------------
# Load appraisal decision data
# ---------------------------------------------------

appraisal_df = load_appraisal_data()

df_long = reshape_appraisal_data(
    appraisal_df
)

# ---------------------------------------------------
# Create figures
# ---------------------------------------------------
appraisal_decisions_fig = create_stacked_bar(
    df_long[
        df_long["Assessment"] == "Appraisal"
    ],
    "Year",
    "Count",
    "Decision",
    "Appraisal Decisions"
)


reappraisal_decisions_fig = create_stacked_bar(
    df_long[
        df_long["Assessment"] == "Reappraisal"
    ],
    "Year",
    "Count",
    "Decision",
    "Reappraisal Decisions"
)


# ---------------------------------------------------
# Decisions Tab Callback
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
def render_decisions_tab(active_tab):

    if active_tab == "decisions":

        return decisions.layout(
            appraisal_decisions_fig,
            reappraisal_decisions_fig
        )

    return dash.no_update