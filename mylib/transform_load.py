"""
Transforms and Loads data into Azure databricks
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into databricks
def load(dataset="data/airline-safety1.csv", dataset2="data/airline-safety2.csv"):
    """Transforms and Loads data into Azure databricks"""
    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    print(server_h, access_token, http_path)
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()

        # INSERT TAKES TOO LONG
        # c.execute("DROP TABLE IF EXISTS AirlineSafety1DB")
        c.execute("SHOW TABLES FROM default LIKE 'AirlineSafety1*'")
        result = c.fetchall()
        # result = False
        # takes too long so not dropping anymore
        # c.execute("DROP TABLE IF EXISTS AirlineSafety1DB")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS AirlineSafety1DB (
                    id int,
                    airline string,
                    avail_seat_km_per_week bigint,
                    incidents_85_99 int,
                    fatal_accidents_85_99 int
                )
            """
            )
            # insert
            for _, row in df.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO AirlineSafety1DB VALUES {convert}")

        c.execute("SHOW TABLES FROM default LIKE 'AirlineSafety2*'")
        result = c.fetchall()
        # result = False

        # c.execute("DROP TABLE IF EXISTS AirlineSafety2DB")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS AirlineSafety2DB (
                    id int,
                    fatalities_85_99 int,
                    incidents_00_14 int,
                    fatal_accidents_00_14 int,
                    fatalities_00_14 int
                )
                """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO AirlineSafety2DB VALUES {convert}")
        c.close()

    return "success"
