# sample_script.py

data = [
    ("Microsoft Fabric", 2025),
    ("Power BI", 2024),
    ("Synapse", 2023)
]

columns = ["Product", "Year"]

df = spark.createDataFrame(data, columns)
df.show()
