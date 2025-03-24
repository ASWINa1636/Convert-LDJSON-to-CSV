import json
import pandas as pd

# Define the file path correctly
file_path = r"D:\your_path_location.ldjson"

# Read the LDJSON file line by line
data_list = []
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        try:
            data_list.append(json.loads(line))  # Load each line as a separate JSON object
        except json.JSONDecodeError as e:
            print(f"Skipping invalid JSON line: {e}")

# Convert list of JSON objects to DataFrame
df = pd.DataFrame(data_list)

# Save DataFrame as CSV
df.to_csv("output.csv", index=False, encoding="utf-8")

print("Conversion complete: output.csv")
