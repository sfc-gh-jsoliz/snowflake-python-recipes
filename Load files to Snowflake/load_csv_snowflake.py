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
df = pd.read_csv("s3://sfquickstarts/intro-to-machine-learning-with-snowpark-ml-for-python/diamonds.csv")

# Do something cool with pandas on Snowflake!
df.describe() 