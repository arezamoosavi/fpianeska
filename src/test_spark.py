from pyspark.sql import SparkSession
from pyspark.sql.types import StringType

# Spark session
spark = SparkSession.builder.master("local").getOrCreate()
sc = spark.sparkContext

# Sum of the first 100 whole numbers
rdd = sc.parallelize(range(100000))
result = rdd.sum()
print(result)

# write in hadoop
# spark.createDataFrame(spark.sparkContext\
#     .parallelize([result]), StringType()).coalesce(1).write.format("text")\
#     .mode("overwrite").save("hdfs://namenode:8020/test")
