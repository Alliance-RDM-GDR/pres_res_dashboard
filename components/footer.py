from datetime import datetime
import dash_bootstrap_components as dbc
from dash import html

def create_footer():
    """
    Generates a standardized, responsive footer component 
    for use across multiple application dashboard pages.
    """
    return html.Footer(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        html.P(
                            f"© {datetime.now().year} Digital Preservation Services Analytics Portal",
                            className="text-muted mb-0 small"
                        ),
                        xs=12, md=6,
                        className="text-center text-md-start"
                    ),
                    dbc.Col(
                        html.P(
                            "Providing access to data over time.",
                            className="text-muted mb-0 small text-md-end"
                        ),
                        xs=12, md=6,
                        className="text-center text-md-end"
                    )
                ],
                className="align-items-center"
            ),
            fluid=True,
        ),
        className="footer py-3 mt-auto bg-light border-top"
    )
