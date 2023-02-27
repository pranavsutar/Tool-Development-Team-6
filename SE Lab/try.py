import pandas as pd # Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
import dataprep.eda as dp # DataPrep is a Python library for data preparation and data analysis.

# Load the dataset
df = pd.read_csv("data.csv") # Read a comma-separated values (csv) file into DataFrame.

# Analyze the dataset 
report = dp.analyze(df) 

# Print the report
print(report)

