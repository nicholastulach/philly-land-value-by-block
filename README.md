# philly-land-value-by-block

## Description
Generates some basic statistics (normalized land values) for property assessments in Philadelphia by aggregating at the block level, e.g. 100 block of Market Street. Normalizes the data based on the `(total land value + exempt land value) / total area`.

Also contains a second script to update the GeoJSON version of the properties file with the compute metrics (`value_sqft`, `value_sqft_mean`, and `value_sqft_diff_mean`).

## Requirements
1. [Python 3](https://www.python.org)
2. [Poetry](https://python-poetry.org)
3. [Pandas](https://pandas.pydata.org)
4. [GeoPandas](https://geopandas.org)
4. [OPA data](https://www.opendataphilly.org/dataset/opa-property-assessments) – Properties CSV

## Instructions - Basic Metrics
1. Clone this repo to your local machine.
2. Run `poetry shell` from the project folder.
3. Download the OPA properties CSV from Open Data Philly. Put the source file in the `data` directory.
4. Execute the script: `python calcluate_value_sqft_by_block.py`
5. Generates three results files: `output.csv`, `output_groups.csv`, and `output_metrics_only.csv`
6. Play around with the data!

## Instructions – GeoJSON
1. Run the basic metrics procedure to generate `output_metrics_only.csv`.
2. Execute the script: `python add_value_sqft_to_geojson.py`
3. Generates results file: `output.geojson`
4. Start mapping!
