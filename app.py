import dash
from dash import html
import dash_bootstrap_components as dbc

from callbacks.preservation_callbacks import register_preservation_callbacks
from callbacks.processing_callbacks import register_processing_callbacks

from utils.data_loader import (
    load_pres_question_data,
    load_processing_storage,
)

from components.footer import create_footer

# ===================================================
# Create Dash Application
# ===================================================

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

app.title = "Digital Preservation Services Dashboard"


# ===================================================
# Navigation Configuration
# ===================================================

# Pages that appear inside Processing & Storage
# processing_dropdown_pages = [
#     "Processing and Storage",
#     "Appraisal",
# ]

# # Pages that appear inside Preservation
# preservation_dropdown_pages = [
#     "Formats",
# ]
# Processing and storage is a direct navbar link
processing_storage_page = "Processing and Storage"

# Appraisal is a direct navbar link
appraisal_page = "Appraisal"

# Formats is a direct navbar link
formats_page = "Formats"

# Research Metrics is a direct navbar link
dataset_metrics_page = "Dataset Metrics"

# Metrics Info is a direct navbar link
metrics_info_page = "Metrics Info"


# ===================================================
# Get Registered Pages
# ===================================================

pages = {
    page["name"]: page
    for page in dash.page_registry.values()
}


# Optional debugging
print("\nRegistered Dash pages:")
for name, page in pages.items():
    print(f"  {name} -> {page['path']}")


# ===================================================
# Helper Function
# ===================================================

def build_dropdown_items(page_names):

    items = []

    for name in page_names:

        page = pages.get(name)

        if page:

            items.append(
                dbc.DropdownMenuItem(
                    name,
                    href=page["path"],
                )
            )

        else:

            print(
                f"WARNING: Navigation page not found: {name}"
            )

    return items


# ===================================================
# Build Processing & Storage Items
# ===================================================

# processing_items = build_dropdown_items(
#     processing_dropdown_pages
# )


# ===================================================
# Build Preservation Items
# ===================================================

# preservation_items = build_dropdown_items(
#     preservation_dropdown_pages
# )


# ===================================================
# Build Navbar Items
# ===================================================

nav_items = []


# ---------------------------------------------------
# Processing & Storage
# ---------------------------------------------------

# if processing_items:

#     nav_items.append(
#         dbc.DropdownMenu(
#             children=processing_items,
#             nav=True,
#             in_navbar=True,
#             label="Processing & Storage",
#         )
#     )


# ---------------------------------------------------
# Preservation
# ---------------------------------------------------

# if preservation_items:

#     nav_items.append(
#         dbc.DropdownMenu(
#             children=preservation_items,
#             nav=True,
#             in_navbar=True,
#             label="Preservation",
#         )
#     )



appraisal_page = pages.get(
   appraisal_page
)

if appraisal_page:

    nav_items.append(
        dbc.NavItem(
            dbc.NavLink(
                "Appraisal & Reappraisal",
                href=appraisal_page["path"],
            )
        )
    )

processing_storage_page = pages.get(
processing_storage_page
)

if processing_storage_page:

    nav_items.append(
        dbc.NavItem(
            dbc.NavLink(
                "Processing & Storage",
                href=processing_storage_page["path"],
            )
        )
    )

# if processing_storage_page:

#     nav_items.append(
#         dbc.NavItem(
#             dbc.NavLink(
#                 "Formats",
#                 href=research_page["path"],
#             )
#         )
#     )

# ---------------------------------------------------
# Formats
# ---------------------------------------------------

formats_page = pages.get(
    formats_page
)

if formats_page:

    nav_items.append(
        dbc.NavItem(
            dbc.NavLink(
                "Formats",
                href=formats_page["path"],
            )
        )
    )

# ---------------------------------------------------
# Dataset Metrics
# ---------------------------------------------------

dataset_metrics_page = pages.get(
    dataset_metrics_page
)

if dataset_metrics_page:

    nav_items.append(
        dbc.NavItem(
            dbc.NavLink(
                "Dataset Metrics",
                href=dataset_metrics_page["path"],
            )
        )
    )

metrics_info_page = pages.get(
    metrics_info_page
)

if metrics_info_page:

    nav_items.append(
        dbc.NavItem(
            dbc.NavLink(
                "Metrics Info",
                href=metrics_info_page["path"],
            )
        )
    )

else:

    print(
        "WARNING: Research Metrics page was not found "
        "in dash.page_registry"
    )


# ===================================================
# Navbar
# ===================================================

navbar = dbc.Navbar(
    dbc.Container(
        [

            dbc.NavbarBrand(
                "DPS Dashboard",
                href="/",
            ),

            dbc.NavbarToggler(
                id="navbar-toggler",
                n_clicks=0,
            ),

            dbc.Collapse(
                dbc.Nav(
                    nav_items,
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse",
                navbar=True,
            ),

        ],
        fluid=True,
    ),

    color="transparent",
    dark=False,
    className="mb-4",
)


# ===================================================
# Main Layout
# ===================================================

app.layout = html.Div(
    [

        navbar,

        dbc.Container(
            [
                dash.page_container,
            ],
            fluid=True,
            className="flex-shrink-0 mb-5",
        ),

        create_footer(),

    ],

    style={
        "display": "flex",
        "flexDirection": "column",
        "minHeight": "100vh",
    },
)


# ===================================================
# Register Callbacks
# ===================================================

pres_df = load_pres_question_data()

register_preservation_callbacks(
    pres_df
)


processing_df = load_processing_storage()

register_processing_callbacks(
    processing_df
)


# ===================================================
# Run Application
# ===================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        use_reloader=True,
    )