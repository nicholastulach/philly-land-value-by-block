import pandas as pd

df = pd.read_csv(
    "opa_properties_public.csv",
    usecols=[
        "exempt_land",
        "house_number",
        "objectid",
        "street_designation",
        "street_direction",
        "street_name",
        "taxable_land",
        "total_area",
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
df["value_per_sqft"] = (df["taxable_land"] + df["exempt_land"]) / df["total_area"]

# Calcluate the aggregate count, mean, standard deviation, and range for each
# block
df = df.groupby(
    ["street_direction", "street_name", "street_designation", "block"], dropna=False
)[["value_per_sqft"]].agg(
    count=("value_per_sqft", "count"),
    value_sqft_mean=("value_per_sqft", "mean"),
    value_sqft_std=("value_per_sqft", "std"),
    value_sqft_range=("value_per_sqft", lambda x: x.max() - x.min()),
)

df.reset_index().to_csv("land_value_sqft_by_block.csv", index=None)
