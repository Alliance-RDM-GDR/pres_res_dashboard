from dash.dash_table import DataTable

def create_data_table(
    df,
    table_id="data-table",
    page_size=40
):
    """
    Creates a reusable Dash DataTable.

    Parameters:
        df:
            Pandas dataframe to display

        table_id:
            Unique ID for Dash callbacks if needed later

        page_size:
            Number of rows displayed per page
    """

    return DataTable(
        id=table_id,

        columns=[
            {
                "name": column.replace("_", " "),
                "id": column
            }
            for column in df.columns
        ],

        data=df.to_dict("records"),

        page_size=page_size,

        sort_action="native",

        filter_action="native",

        style_table={
            "overflowX": "auto"
        },

        style_cell={
            "textAlign": "left",
            "padding": "8px"
        },

        style_header={
            "fontWeight": "bold"
        }
    )