# hello-world
```python
import org.apache.spark.sql.SparkSession

// Create a SparkSession
val spark = SparkSession.builder()
  .appName("Z-compressed File Loading")
  .getOrCreate()

// Set the path to the Z-compressed file
val filePath = "/path/to/compressed_file.z"

// Read the compressed file using Spark
val df = spark.read
  .format("csv") // Assuming the compressed file is in CSV format
  .option("header", "true") // Specify if the file has a header
  .option("inferSchema", "true") // Infer column types automatically
  .option("compression", "org.apache.hadoop.io.compress.DefaultCodec") // Specify the compression codec
  .load(filePath)

// Process and display the loaded data
df.show()
```
# PySpark
```python
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Z-compressed File Loading") \
    .getOrCreate()

# Set the path to the Z-compressed file
file_path = "/path/to/compressed_file.z"

# Read the compressed file using Spark
df = spark.read \
    .format("csv")  # Assuming the compressed file is in CSV format
    .option("header", "true")  # Specify if the file has a header
    .option("inferSchema", "true")  # Infer column types automatically
    .option("compression", "org.apache.hadoop.io.compress.DefaultCodec")  # Specify the compression codec
    .load(file_path)

# Process and display the loaded data
df.show()
```
