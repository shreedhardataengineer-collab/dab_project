import sys
import os
import pytest

# Run the tests from the root directory
sys.path.append(os.getcwd())

#returning spark session
@pytest.fixture()
def spark():
    try:
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.getOrCreate()
    except ImportError:
        try:
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
        except:
            raise ImportError("Neither Databricks Session or Spark Session are available")
    return spark