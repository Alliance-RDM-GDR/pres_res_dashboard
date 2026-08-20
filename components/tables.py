from dash.dash_table import DataTable
import re
import dash_ag_grid as dag


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

def create_crosstab(
    df,
    table_id="cross-tab",
    height="750px",
    pinned_column="Format",
    default_column_width=180,
):
    """
    Create a reusable Dash AG Grid cross-tab table.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the cross-tab data.

    table_id : str
        Dash component ID.

    height : str
        Height of the table.

    pinned_column : str
        Column to keep pinned on the left.

    default_column_width : int
        Width of the RDF columns.

    Returns
    -------
    dag.AgGrid
        Configured Dash AG Grid component.
    """

    column_defs = []

    for col in df.columns:

        # First column / row identifier
        if col == pinned_column:
            column_defs.append({
                "field": col,
                "headerName": col,
                "pinned": "left",
                "width": 180,
                "resizable": True,
            })
            continue

        # Extract RDF code from:
        # "Artificial intelligence (AI) (RDF10201)"
        match = re.match(r"^(.*?)\s*\((RDF\d+)\)$", str(col))

        if match:
            header_name = match.group(1)
            rdf_code = match.group(2)
        else:
            header_name = str(col)
            rdf_code = ""

        column_defs.append({
            "field": col,
            "headerName": header_name,
            "headerTooltip": rdf_code,
            "width": default_column_width,
            "type": "numericColumn",
            "resizable": True,
            "sortable": True,
            "filter": True,
        })

    return dag.AgGrid(
        id=table_id,
        columnDefs=column_defs,
        rowData=df.to_dict("records"),

        defaultColDef={
            "resizable": True,
            "sortable": True,
            "filter": True,
        },

        dashGridOptions={
            "animateRows": False,
            "rowBuffer": 20,
        },

        style={
            "height": height,
            "width": "100%",
        },
    )