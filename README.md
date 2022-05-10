# philly-land-value-by-block

## Description
Generates some basic statistics (normalized land values) for property assessments in Philadelphia by aggregating at the block level, e.g. 100 block of Market Street. Normalizes the data based on the `(total land value + exempt land value) / total area`.

## Requirements
1. [Python 3](https://www.python.org)
2. [Poetry](https://python-poetry.org)
3. [Pandas](https://pandas.pydata.org)
4. [OPA data](https://www.opendataphilly.org/dataset/opa-property-assessments) – Properties CSV

## Instructions
1. Clone this repo to your local machine.
2. Run `poetry shell` from the project folder.
3. Download the OPA properties CSV from Open Data Philly.
4. Execute the script: `python calcluate_value_sqft_by_block.py`
5. Open the results file: `land_value_sqft_by_block.csv`
6. Play around with the data!
