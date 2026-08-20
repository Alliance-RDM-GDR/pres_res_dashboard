import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------
# Load Google Sheets
# ---------------------------------------------------
SHEET_ID = os.getenv("SHEET_ID")

SHEET_TABS = {
    "processing_storage": "1331834181",
    "status_backlog": "317804893",
    "appraisal_reappraisal": "1491793398",
    "pres_question": "1634534066",
    "format_levels": "1020252192",
    "format_calc": "899935805",
    "dataset_metrics": "426469201",
    "size_range": "1248493435",
    "collection_stats": "365592660"
}

def load_sheet(tab_name):

    gid = SHEET_TABS[tab_name]

    url = (
        f"https://docs.google.com/spreadsheets/d/"
        f"{SHEET_ID}/export"
        f"?format=csv&gid={gid}"
    )

    df = pd.read_csv(url)

    df.columns = (
        df.columns
        .str.strip()
    )

    return df
# ---------------------------------------------------
# Processing Stats
# ---------------------------------------------------
def load_processing_storage():

    df = load_sheet("processing_storage")

    numeric_cols = [
        "Total AIPs",
        "Total Datasets Processed",
        "Total Datasets Reprocessed",
        "Total Datasets Completed",
        "Total Dataset FPRES",
        "Total Storage (TB)"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    return df

# ---------------------------------------------------
# Status and Backlog
# ---------------------------------------------------
def load_status_backlog_data():

    df = load_sheet("status_backlog")
  
    return df
# ---------------------------------------------------
# Appraisal Page Stats
# ---------------------------------------------------
def load_appraisal_data():

  df = load_sheet("appraisal_reappraisal")

  return df

# ---------------------------------------------------
# Load Pres Question Data
# ---------------------------------------------------
def load_pres_question_data():

    df = load_sheet("pres_question")

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
    )

    response_columns = [
        "Yes",
        "No",
        "Unsure",
        "No_Response"
    ]

    # Keep blanks as missing values (NaN)
    for col in response_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )
    #####Move to calculations.py???
    # Calculate totals if missing
    if "Total_Datasets_for_Year" not in df.columns:

        df["Total_Datasets_for_Year"] = (
            df[response_columns]
            .sum(
                axis=1,
                min_count=1
            )
        )

    # Keep totals as integers where data exists
    df["Total_Datasets_for_Year"] = (
        df["Total_Datasets_for_Year"]
        .apply(
            lambda x: int(x) if pd.notna(x) else x
        )
    )
    # Calculate percentages
    total = df["Total_Datasets_for_Year"]

    df["Yes_%"] = (
        df["Yes"] / total * 100
    ).round(2)

    df["No_%"] = (
        df["No"] / total * 100
    ).round(2)

    df["Unsure_%"] = (
        df["Unsure"] / total * 100
    ).round(2)

    df["No_Response_%"] = (
        df["No_Response"] / total * 100
    ).round(2)

    return df

# ---------------------------------------------------
# Appraisal and Reappraisal Decisions
# ---------------------------------------------------
def reshape_appraisal_data(df):
  """
  Convert the appraisal/reappraisal data from wide to long format.
  """

  df = (
      df.melt(
          id_vars="Year",
          var_name="Category",
          value_name="Count"
      )
      .dropna(subset=["Count"])
  )

  df["Category"] = (
      df["Category"]
      .str.replace(r"\s*-\s*", "-", regex=True)
      .str.strip()
  )

  df[["Assessment", "Decision"]] = (
      df["Category"]
      .str.split("-", n=1, expand=True)
  )

  df["Assessment"] = df["Assessment"].str.strip()
  df["Decision"] = df["Decision"].str.strip()

  return df

def get_decision_data(df, assessment):

    return df[
        df["Assessment"] == assessment
    ]

# ---------------------------------------------------
# Load Format Levels Data
# ---------------------------------------------------
def load_format_level_data():
  df = load_sheet("format_levels")

  return df

def load_format_id_data():
  df = load_sheet("format_calc")

  return df
# ---------------------------------------------------
# Load Dataet Metrics Data
# ---------------------------------------------------
def load_dataset_metrics_data():
    df = load_sheet("dataset_metrics")
    return df

# ---------------------------------------------------
# Load Size Data
# ---------------------------------------------------
def load_dataset_size_data():
    df = load_sheet("size_range")
    # Extract numeric value and unit
    df[["size_value", "size_unit"]] = (
        df["Dataset size - FRDR"]
        .str.extract(r"([\d.]+)\s*([KMGT]?B)?")
    )

    # Convert to numeric
    df["size_value"] = pd.to_numeric(
        df["size_value"],
        errors="coerce"
    )

    # Convert everything to GB
    multipliers = {
        "KB": 1 / 1024**2,
        "MB": 1 / 1024,
        "GB": 1,
        "TB": 1024,
    }

    df["size_gb"] = (
        df["size_value"] *
        df["size_unit"].map(multipliers)
    )

    # Create ranges
    bins = [-float("inf"), 0.001, 0.1, 1, 10, 100, 1024, float("inf")]

    labels = [
        "< 1 MB",
        "1 MB – 100 MB",
        "100 MB – 1 GB",
        "1 GB – 10 GB",
        "10 GB – 100 GB",
        "100 GB – 1 TB",
        "1 TB+"
    ]

    df["size_range"] = pd.cut(
        df["size_gb"],
        bins=bins,
        labels=labels,
        right=False
    )

    df["file_count"] = pd.to_numeric(
    df["Number of Files"],
    errors="coerce"
    )
    bins = [
      -1,
      10,
      100,
      1000,
      10000,
      100000,
      float("inf")
  ]

    labels = [
      "1–10",
      "11–100",
      "101–1K",
      "1K–10K",
      "10K–100K",
      "100K+"
  ]

    df["file_count_range"] = pd.cut(
      df["file_count"],
      bins=bins,
      labels=labels
  )
    df[["size_value", "size_unit"]] = (
        df["AIP Size"]
        .str.extract(r"([\d.]+)\s*([KMGT]?B)?")
    )

    # Convert to numeric
    df["size_value"] = pd.to_numeric(
        df["size_value"],
        errors="coerce"
    )

        # Convert everything to GB
    multipliers = {
            "KB": 1 / 1024**2,
            "MB": 1 / 1024,
            "GB": 1,
            "TB": 1024,
        }

    df["size_gb"] = (
        df["size_value"] *
        df["size_unit"].map(multipliers)
    )

          # Create ranges
    bins = [-float("inf"), 0.001, 0.1, 1, 10, 100, 1024, float("inf")]

    labels = [
        "< 1 MB",
        "1 MB – 100 MB",
        "100 MB – 1 GB",
        "1 GB – 10 GB",
        "10 GB – 100 GB",
        "100 GB – 1 TB",
        "1 TB+"
    ]

    df["size_range"] = pd.cut(
        df["size_gb"],
        bins=bins,
        labels=labels,
        right=False
    )    
    return df

# ---------------------------------------------------
# Collection Stats
# ---------------------------------------------------
def load_collection_stats_data():

    df = load_sheet("collection_stats")

    return df
# ---------------------------------------------------
# CRDC - Format Mapping Stats
# ---------------------------------------------------
def load_crdc_format_stats_data():
    df = pd.read_csv("data/Format - CRDC Mapping - Cross Tab.csv")

    return df