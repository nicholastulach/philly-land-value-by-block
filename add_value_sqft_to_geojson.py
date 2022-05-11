import geopandas
import pandas as pd

gdf = geopandas.read_file("data/opa_properties_public.geojson")
df = pd.read_csv("data/output_metrics_only.csv")

gdf = gdf.merge(df, on="objectid")

gdf.to_file("data/output.geojson", driver="GeoJSON")
