import pandas as pd

def processing_metrics(df):

    def display_value(value):
        if pd.isna(value) or value == 0:
            return "-"
        return value
    #calculate sums to be used later
    raw_storage = df["Total Storage (TB)"].sum()
    raw_aips = df["Total AIPs"].sum()
    raw_completed = df["Total Datasets Completed"].sum()

    return {
      "total_aips": display_value(int(raw_aips)),
      "total_processed": display_value(
          int(df["Total Datasets Processed"].sum())
      ),
      "total_reprocessed": display_value(
        round(df["Total Datasets Reprocessed"].sum(), 2)
      ),
      "total_completed": display_value(int(raw_completed)),
      "total_storage": display_value(
          round(raw_storage, 2)
      ),
      "total_fpres": display_value(
          round(df["Total Dataset FPRES"].sum(), 2)
      ),
      "total_storage_percentage": display_value(
          round(raw_storage / 500 * 100, 2)
      ), 
      "total_aips_percentage":display_value(round(raw_aips/raw_completed * 100, 2)
      ),   
    }
# ---------------------------------------------------
# Storage Trend
# ---------------------------------------------------
def calculate_storage_trend(df):

    trend_df = df.copy()

    trend_df["Count"] = (
        trend_df["Total Storage (TB)"].fillna(0)
    )

    return trend_df[
        [
            "Year",
            "Count"
        ]
    ]
# ---------------------------------------------------
# Status 
# ---------------------------------------------------
def status_backlog (df):
    return {
      "Consider preservation": df.loc[
          df["preservation_recommendation"] == "Consider preservation",
          "recommendation_totals"
      ].iloc[0],
    }
    
# ---------------------------------------------------
# Appraisal Metrics
# ---------------------------------------------------
def calculate_appraisal_metrics(df):

    appraisal_accept = (
        df["Appraisal - Accept"]
        .fillna(0)
        .sum()
    )

    appraisal_reject = (
        df["Appraisal - Reject"]
        .fillna(0)
        .sum()
    )

    reappraisal_accept = (
        df["Reappraisal- Accept"]
        .fillna(0)
        .sum()
    )

    reappraisal_reject = (
        df["Reappraisal - Reject"]
        .fillna(0)
        .sum()
    )

    total_reviewed = (
        appraisal_accept
        + appraisal_reject
        # + reappraisal_accept
        # + reappraisal_reject
    )

    total_accepted = (
        appraisal_accept
        + reappraisal_accept
    )

    total_rejected = (
        appraisal_reject
        + reappraisal_reject
    )

    acceptance_rate = (
        (total_accepted / total_reviewed) * 100
        if total_reviewed > 0
        else 0
    )

    return {
        "total_reviewed": int(total_reviewed),
        "accepted": int(total_accepted),
        "rejected": int(total_rejected),
        "acceptance_rate": round(
            acceptance_rate,
            1
        )
    }

# ---------------------------------------------------
# Appraisal Trend Data
# ---------------------------------------------------
def calculate_appraisal_trend(df):

    trend_df = df.copy()

    trend_df["Count"] = (
        trend_df["Appraisal - Accept"].fillna(0)
        +
        trend_df["Appraisal - Reject"].fillna(0)
        +
        trend_df["Reappraisal- Accept"].fillna(0)
        +
        trend_df["Reappraisal - Reject"].fillna(0)
    )

    return trend_df[
        [
            "Year",
            "Count"
        ]
    ]

# ---------------------------------------------------
# Preservation Question Year Filter
# ---------------------------------------------------
def filter_pres_question_year(df, year):

    return df[
        df["Year"] == year
    ].iloc[0]

def display_value(value):

    if pd.isna(value):
        return "-"

    return value


def calculate_preservation_question_metrics(df, year):

    selected = filter_pres_question_year(
        df,
        year
    )

    return {
        "total_datasets": display_value(
            selected["Total_Datasets_for_Year"]
        ),

        "yes_percent": display_value(
            selected["Yes"]
        ),

        "no_percent": display_value(
            selected["No"]
        ),

        "unsure_percent": display_value(
            selected["Unsure"]
        ),

        "no_response_percent": display_value(
            selected["No_Response"]
        ),
    }
# ---------------------------------------------------
# Appraisal and Reappraisal
# ---------------------------------------------------
def prepare_appraisal_decision_data(df):

    appraisal = df[
        [
            "Year",
            "Appraisal - Accept",
            "Appraisal - Reject"
        ]
    ].copy()

    appraisal = appraisal.melt(
        id_vars="Year",
        var_name="Decision",
        value_name="Count"
    )

    appraisal["Decision"] = appraisal["Decision"].replace(
        {
            "Appraisal - Accept": "Accept",
            "Appraisal - Reject": "Reject",
        }
    )
    return appraisal

def prepare_reappraisal_decision_data(df):
    reappraisal = df[
        [
            "Year",
            "Reappraisal- Accept",
            "Reappraisal - Reject"
        ]
    ].copy()

    reappraisal = reappraisal.melt(
        id_vars="Year",
        var_name="Decision",
        value_name="Count"
    )

    reappraisal["Decision"] = reappraisal["Decision"].replace(
        {
            "Reappraisal- Accept": "Accept",
            "Reappraisal - Reject": "Reject",
        }
    )
    return reappraisal

# ---------------------------------------------------
# Format Levels
# ---------------------------------------------------
def risk_levels(df):

    risk_counts = (
      df["Risk Level"]
      .str.split(";")
      .explode()
      .str.strip()
      .value_counts()
      .reset_index()
    )
    
    risk_counts.columns = [
        "Risk Level",
        "Number of Files"
    ]

    # return risk_counts
    # print(df)
    return risk_counts[
      [
        "Risk Level",
        "Number of Files"
      ]
    ]

def preservation_levels(df):

  preservation_counts = (
    df["Preservation Level"]
    .str.split(";")
    .explode()
    .str.strip()
    .value_counts()
    .reset_index()
)
  
  preservation_counts.columns = [
      "Preservation Level",
      "Number of Files"
  ]

  return preservation_counts

# ---------------------------------------------------
# Appraisal Form
# ---------------------------------------------------
def get_recommendation_kpis(form_df):
    return {
        "Consider preservation": form_df.loc[
            form_df["preservation_recommendation"] == "Consider preservation",
            "recommendation_totals"
        ].iloc[0],
        
        "Review": form_df.loc[
            form_df["preservation_recommendation"] == "Review",
            "recommendation_totals"
        ].iloc[0],

        "Prioritize preservation": form_df.loc[
            form_df["preservation_recommendation"] == "Prioritize preservation",
            "recommendation_totals"
        ].iloc[0],

        "Preserve - plan resources": form_df.loc[
            form_df["preservation_recommendation"] == "Preserve - plan resources",
            "recommendation_totals"
        ].iloc[0],
        #  "Preserve - resource intensive": form_df.loc[
        #     form_df["preservation_recommendation"] == "Preserve - resource intensive",
        #     "recommendation_totals"
        # ].iloc[0],

        "Low priority": form_df.loc[
            form_df["preservation_recommendation"] == "Low priority",
            "recommendation_totals"
        ].iloc[0],

        "Do not prioritize": form_df.loc[
            form_df["preservation_recommendation"] == "Do not prioritize",
            "recommendation_totals"
        ].iloc[0],
    }

def group_totals(for_df):
    for_df = for_df.dropna(subset=["crdc_group", "group_total"]).copy()

    for_df["group_total"] = pd.to_numeric(for_df["group_total"])

    for_df["rdf_group"] = (
        "RDF"
        + for_df["crdc_group"].str.extract(r"\(RDF(\d)")[0]
        + "0"
    )

    return (
        for_df.groupby("rdf_group")["group_total"]
        .sum()
        .rename({
            "RDF10": "Natural sciences",
            "RDF20": "Engineering and technology",
            "RDF30": "Medical and health sciences",
            "RDF40": "Agricultural and veterinary sciences",
            "RDF50": "Social sciences",
            "RDF60": "Humanities and the arts",
        })
    )


# ---------------------------------------------------
# Dataset Processing Metrics
# ---------------------------------------------------

def calculate_processing_metrics(
    processing_df,
    year
):

    if year is None:
        return {
            "total_aips": "N/A",
            "datasets_processed": "N/A",
            "datasets_reprocessed": "N/A",
            "datasets_completed": "N/A",
        }

    selected = processing_df[
        processing_df["Year"] == year
    ]

    if selected.empty:
        return {
            "total_aips": "N/A",
            "datasets_processed": "N/A",
            "datasets_reprocessed": "N/A",
            "datasets_completed": "N/A",
        }

    row = selected.iloc[0]

    def format_count(value):

        if pd.isna(value):
            return "N/A"

        return f"{int(value):,}"

    return {
        "total_aips": format_count(
            row["Total AIPs"]
        ),
        "datasets_processed": format_count(
            row["Total Datasets Processed"]
        ),
        "datasets_reprocessed": format_count(
            row["Total Datasets Reprocessed"]
        ),
        "datasets_completed": format_count(
            row["Total Datasets Completed"]
        ),
    }