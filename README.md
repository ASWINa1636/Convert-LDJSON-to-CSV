--->> Convert LDJSON to CSV

A simple Python script to convert "Line-Delimited JSON (LDJSON)" files into "CSV format" using `pandas`.
This script processes large datasets efficiently, making it useful for web scraping, job data processing, and API responses.

--->> Features
✅ Reads "LDJSON" files line by line  
✅ Handles "JSON decoding errors gracefully"
✅ Converts data into a structured "Pandas DataFrame" 
✅ Exports the result as "CSV" for easy analysis  

 --->> Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ASWINa1636/Convert-LDJSON-to-CSV.git
   cd Convert-LDJSON-to-CSV
   ```

2. Install required dependencies:
   ```bash
   pip install pandas
   ```

--->> Usage

1. Place your `.ldjson` file in the same directory as `LDjson_to_csv.py`.
2. Open the script and update the **file path** if needed.
3. Run the script:
   ```bash
   python LDjson_to_csv.py
   ```
4. The converted CSV file (`output.csv`) will be generated in the same directory.

--->> License
This project is licensed under the MIT License.

--->> Contributing
Feel free to fork the repository and submit pull requests to improve the script!

