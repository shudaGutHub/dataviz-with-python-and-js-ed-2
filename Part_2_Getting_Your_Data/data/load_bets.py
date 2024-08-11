import pandas as pd
import os
from GPSData import (
    add_gps_columns,
    count_DNF,
    count_entries,
    count_runners,
    replace_underscore_headers,
)

def get_historical_data():
    historical_filename = "gpsbethistory.csv"
    print(f"Checking if file {historical_filename} exists...")
    if os.path.exists(historical_filename):
        try:
            print(f"File {historical_filename} found. Attempting to read...")
            historical_data = pd.read_csv(historical_filename)
            print(f"File {historical_filename} read successfully.")
            return historical_data
        except Exception as e:
            print(f"Error reading {historical_filename}: {e}")
            return None
    else:
        print(f"File {historical_filename} does not exist.")
        return None

# Example usage
if __name__ == "__main__":
    data = get_historical_data()
    if data is not None:
        print("Historical data loaded successfully.")
    else:
        print("Failed to load historical data.")