import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc

import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"

# Your dashboard colour palette

DPS_COLORS = [
    "#D6AB00",  # gold - highlight
    "#32322F",  # black - reference
    "#B3021A",  # red - risk
    "#154a4a",  # teal
    "#2F8F75",  # green - completed/success
    "#39B5B1",  # blue - secondary
    "#F67040",  # coral - warning
]
# ---------------------------------------------------
# Card Layout
# ---------------------------------------------------
def chart_card(title, figure):

  return dbc.Card(
      [
        dbc.CardHeader(
          title,
          className="dps-card-header"
        ),

        dbc.CardBody(
          [
            dcc.Graph(
                figure=figure,
                config={
                    "displayModeBar": False
                }
            )
          ]
        )
      ],
      className="dps-card h-100"
  )
# ---------------------------------------------------
# Line Chart
# ---------------------------------------------------
def create_line_chart(
    df,
    x,
    y,
    title
  ):

  fig = px.line(
      df,
      x=x,
      y=y,
      # markers=True,
      template="plotly_white",
      color_discrete_sequence=DPS_COLORS
      #  color_discrete_sequence=["#F67040"],
  )

  fig.update_layout(
      margin=dict(
          l=20,
          r=20,
          t=20,
          b=20
      )
  )
  fig.update_traces(line=dict(width=4, dash='solid'))

  return fig

# ---------------------------------------------------
# Bar Chart
# --------------------------------------------------
def create_bar_chart(
    df,
    x,
    y,
    title,
):

    fig = px.bar(
        df,
        x=x,
        y=y,
        # title=title,
        template="plotly_white",
        color_discrete_sequence=DPS_COLORS
    )

    fig.update_layout(
        height=385
    )
    fig.update_xaxes(title_text=x.replace("_", " "))
    fig.update_yaxes(title_text=y.replace("_", " "))
    fig.update_traces(
            hovertemplate="%{label}: %{value}<extra></extra>",
            width=0.4,
        )

    return fig

# ---------------------------------------------------
# Horizontal Chart
# ---------------------------------------------------
def create_ranking_chart(
  df,
  category,
  value,
  title,
  limit=20
):
  df = df.copy()
  df[category] = df[category].str.replace("_", " ")
  df = (
    df
    .sort_values(
        value,
        ascending=False
    )
    .head(limit)
  )

  fig = px.bar(
      df,
      x=value,
      y=category,
      orientation="h",
      template="plotly_white",
      color_discrete_sequence=DPS_COLORS
  )

  fig.update_layout(
      yaxis={
          "categoryorder": "total ascending"
      },
      height=550
  )
  fig.update_traces(
          hovertemplate="%{label}: %{value}<extra></extra>"
      )
  fig.update_yaxes(
    title_text=category.replace("_", " ").title()
)

  fig.update_xaxes(
    title_text=value.replace("_", " ").title()
)
  return fig
# ---------------------------------------------------
# Donut Chart
# ---------------------------------------------------
def create_donut_chart(
    df,
    names,
    values,
    title,
  ):
  df = df.copy()
  df[names] = df[names].str.replace("_", " ")
  fig = px.pie(
      df,
      names=names,
      values=values,
      hole=0.45,
      # title=title,
      color_discrete_sequence=DPS_COLORS
      # color_discrete_map=color_map
  )

  fig.update_layout(
      height=385,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
  )
  fig.update_traces(
        hovertemplate="%{label}: %{value}<extra></extra>"
    )
  
  return fig

# ---------------------------------------------------
# Stacked Bar Graph
# ---------------------------------------------------
def create_stacked_bar(
  df,
  x,
  y,
  color,
  title
  ):
  df = df.copy()
  df[x] = df[x].astype(str)

  fig = px.bar(
    df,
    x=x,
    y=y,
    color=color,
    barmode="stack",
    # title=title,
    template="plotly_white",
    color_discrete_sequence=["#32322F","#D6AB00"]
  )
  # fig.update_traces(width=0.4)

  return fig

# ---------------------------------------------------
# Sparkline
# ---------------------------------------------------
def create_sparkline(
  df,
  x,
  y
  ):

  fig = px.line(
      df,
      x=x,
      y=y
  )

  fig.update_layout(
      height=80,
      margin=dict(
          l=0,
          r=0,
          t=0,
          b=0
      ),
      showlegend=False,
      xaxis_visible=False,
      yaxis_visible=False
  )

  return fig
# ---------------------------------------------------
# Pres Question Trend Chart
# ---------------------------------------------------
def create_response_trend_chart(df, metric="percentage"):
    """
    Creates the yearly response trend line chart.

    metric:
    percentage -> Yes %, No %, Unsure %, No Response %
    count      -> Yes, No, Unsure, No Response
    """

    if metric == "percentage":

        value_columns = ["Yes_%", "No_%", "Unsure_%", "No_Response_%"]

        y_title = "Percentage (%)"

    else:

        value_columns = ["Yes", "No", "Unsure", "No_Response"]
        y_title = "Number of Responses"

    # Convert wide format to long format
    chart_df = df[["Year"] + value_columns].copy()

    chart_df = chart_df.melt(id_vars="Year", var_name="Response", value_name="Value")

    # Clean legend names
    chart_df["Response"] = chart_df["Response"].replace(
        {
            "Yes_%": "Yes",
            "No_%": "No",
            "Unsure_%": "Unsure",
            "No_Response_%": "No Response",
            "No_Response": "No Response",
        }
    )

    fig = px.line(
        chart_df,
        x="Year",
        y="Value",
        color="Response",
        markers=True,
        color_discrete_map={
            "Yes": "#006666",
            "No": "#B3021A",
            "Unsure": "#D6AB00",
            "No Response": "#32322F",
        },
    )

    fig.update_layout(
        yaxis_title=y_title,
        xaxis_title="Year",
        legend_title="Response",
        hovermode="x unified",
    )

    # Optional: format percentage axis
    if metric == "percentage":
        fig.update_yaxes(ticksuffix="%")

    return fig

# ---------------------------------------------------
# Dataset Volume Chart
# ---------------------------------------------------
def create_dataset_volume_chart(df):

  fig = px.bar(
      df,
      x="Year",
      y="Total_Datasets_for_Year",
      text="Total_Datasets_for_Year",
  )

  fig.update_layout(xaxis_title="Year", yaxis_title="Datasets")

  fig.update_traces(marker_color="#006666")

  return fig
# ---------------------------------------------------
# Selected Year Distribution Chart
# ---------------------------------------------------
def create_response_distribution_chart(df, selected_year):

  selected = df[df["Year"] == selected_year]

  if selected.empty:
    return {}

  chart_df = selected[["Yes", "No", "Unsure", "No_Response"]].melt(
    var_name="Response", value_name="Count"
  )

  chart_df["Response"] = chart_df["Response"].replace(
      {"No_Response": "No Response"}
  )

  fig = px.pie(
      chart_df,
      names="Response",
      values="Count",
      hole=0.45,
  )

  # fig.update_traces(
  #     marker=dict(colors=["#006666", "#F37D53", "#D6AB00", "#51BE9C"])
  # )

  return fig
#Processing
def create_processing_trend_chart(df, metric="count"):

    value_columns = [
        "Total AIPs",
        "Total Datasets Processed",
        "Total Datasets Reprocessed",
        "Total Datasets Completed",
    ]

    chart_df = df[
        ["Year"] + value_columns
    ].copy()

    # Only show years with processing data
    chart_df = chart_df[
        chart_df["Year"] >= 2020
    ].copy()

    # Calculate year-over-year percentage change
    if metric == "percentage":

        for column in value_columns:

            previous = chart_df[column].shift(1)

            chart_df[column] = (
                (chart_df[column] - previous)
                / previous
            ) * 100

            chart_df.loc[
                previous.isna() | (previous == 0),
                column
            ] = None

        y_title = "Year-over-Year Change (%)"

    else:

        y_title = "Number of Datasets"

    chart_df = chart_df.melt(
        id_vars="Year",
        var_name="Metric",
        value_name="Value"
    )

    chart_df["Metric"] = chart_df["Metric"].replace(
        {
            "Total AIPs": "Total AIPs",
            "Total Datasets Processed": "Datasets Processed",
            "Total Datasets Reprocessed": "Datasets Reprocessed",
            "Total Datasets Completed": "Datasets Completed",
        }
    )

    fig = px.line(
        chart_df,
        x="Year",
        y="Value",
        color="Metric",
        markers=True,
        color_discrete_map={
            "Total AIPs": "#006666",
            "Datasets Processed": "#B3021A",
            "Datasets Reprocessed": "#D6AB00",
            "Datasets Completed": "#32322F",
        },
    )

    fig.update_layout(
        yaxis_title=y_title,
        xaxis_title="Year",
        legend_title="Metric",
        hovermode="x unified",
    )

    if metric == "percentage":
        fig.update_yaxes(ticksuffix="%")

    return fig