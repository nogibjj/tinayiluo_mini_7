"""
Extract a dataset from a URL. 
JSON or CSV formats tend to work well
"""
import os
import requests
import pandas as pd


def extract(
    url="https://github.com/fivethirtyeight/data/blob/master/airline-safety/airline-safety.csv?raw=true",
    file_path="data/airline-safety.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)

    # Load the CSV into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Split the DataFrame into two based on the desired columns.
    # For example, let's split it in half (you can adjust this based on your needs).
    mid_idx = len(df.columns) // 2
    df1 = df.iloc[:, :mid_idx]
    df2 = df.iloc[:, mid_idx:]

    # Save the two DataFrames into separate CSV files.
    df1.to_csv(os.path.join(directory, "airline-safety1.csv"), index=False)
    df2.to_csv(os.path.join(directory, "airline-safety2.csv"), index=False)

    return file_path


# Call the function to extract and split the dataset
# extract()
