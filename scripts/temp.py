from databricks.connect import DatabricksSession
spark = DatabricksSession.builder.remote(cluster_id="0911-102016-o9ta6yzm").getOrCreate()
spark.sql("select 1").show()