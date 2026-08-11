import dash_bootstrap_components as dbc
from dash import html


def create_dashboard_tabs(
    tabs,
    tab_id,
    content_id,
    default_tab
):
    """
    Creates reusable Bootstrap tabs.

    Parameters
    ----------
    tabs : list
        List of dictionaries:
        [
            {
                "label": "Overview",
                "value": "overview"
            }
        ]

    tab_id : str
        ID for the Tabs component

    content_id : str
        ID for the content container

    default_tab : str
        Default selected tab
    """


    return html.Div(
        [

            dbc.Tabs(
                [
                    dbc.Tab(
                        label=tab["label"],
                        tab_id=tab["value"]
                    )

                    for tab in tabs
                ],

                id=tab_id,

                active_tab=default_tab

            ),


            html.Div(
                id=content_id,
                className="mt-4"
            )

        ]
    )