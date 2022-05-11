import pandas as pd

df = pd.read_csv(
    "data/opa_properties_public.csv",
    dtype={"suffix": "str", "year_built": "str"},
    usecols=[
        "objectid",
        "assessment_date",
        "census_tract",
        "exempt_building",
        "exempt_land",
        "geographic_ward",
        "house_number",
        "state_code",
        "street_code",
        "street_designation",
        "street_direction",
        "street_name",
        "suffix",
        "taxable_building",
        "taxable_land",
        "total_area",
        "total_livable_area",
        "year_built",
        "year_built_estimate",
        "zip_code",
        "lat",
        "lng",
    ],
)

# Derive the block number from the house number, e.g. 1107 is 1100 block, etc.
df["block"] = df["house_number"] // 100 * 100

# Ignore properties with empty taxable land, in-kind values, and zero values
df = df[
    (pd.notnull(df["taxable_land"]))
    & (df["taxable_land"] > 1)
    & (df["total_area"] != 0)
]

# Compute the value per square foot for both the exempt and taxable land area
df["value_sqft"] = (df["taxable_land"] + df["exempt_land"]) / df["total_area"]

# Remove rows with empty `value_sqft`. They are meaningless.
df = df[pd.notnull(df["value_sqft"])]

# Calcluate the aggregate count, mean, standard deviation, and range for each
# block
dfg = df.groupby(
    ["street_direction", "street_name", "street_designation", "block"], dropna=False
)[["value_sqft"]].agg(
    count=("value_sqft", "count"),
    value_sqft_mean=("value_sqft", "mean"),
    value_sqft_std=("value_sqft", "std"),
    value_sqft_range=("value_sqft", lambda x: x.max() - x.min()),
)
dfg = dfg.reset_index()
dfg.to_csv("data/output_groups.csv", index=None)

# Merge the data back into the original dataframe
df = pd.merge(
    df,
    dfg,
    on=["street_direction", "street_name", "street_designation", "block"],
    how="left",
)

# Calculate the difference from the mean
df["value_sqft_diff_mean"] = df["value_sqft"] - df["value_sqft_mean"]

df.to_csv("data/output.csv", index=None)
