# pip install "snowflake-snowpark-python[modin]" s3fs openpyxl 
# Establish connection to Snowpark
from snowflake.snowpark.session import Session
session = Session.builder.create()
# To use pandas on Snowflake, import Modin and Snowpark
import modin.pandas as pd
import snowflake.snowpark.modin.plugin

# Load CSV from a local file
df = pd.read_csv("data.csv")
df.head()

# Load CSV from a S3 bucket
df = pd.read_csv("s3://sfquickstarts/frostbyte_tastybytes/analytics/menu_item_aggregate_v.csv")

# Load Excel from S3 bucket
df = pd.read_excel("s3://sfquickstarts/frostbyte_tastybytes/excel/pricing_guac_roll_04_2023.xlsx")

# Load CSV from remote URL 
df = pd.read_csv("https://raw.githubusercontent.com/Snowflake-Labs/sf-samples/refs/heads/main/samples/ml/diamonds.csv")

# Do something cool with pandas on Snowflake!
df.describe() 