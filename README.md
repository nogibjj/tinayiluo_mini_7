## Package a Python Script into a Command-Line Tool
[![CI](https://github.com/nogibjj/tinayiluo_mini_6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/tinayiluo_mini_6/actions/workflows/cicd.yml)

### Goal

The goal of this project is to create a python package ETL-Query pipeline utilizing a cloud service like Databricks. This pipeline will involve tasks such as extracting data from FiveThirtyEight's public datasets, cleaning and transforming the data, then loading it into Databricks SQL Warehouse. Once the data is in place, we'll be able to run complex queries that may involve tasks like joining tables, aggregating data, and sorting results. This will be accomplished by establishing a database connection to Databricks. 

The workflow includes running a Makefile to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`) with Python Black, linting (`make lint`) with Ruff, and an all-inclusive task (`make all`) using `Github Actions`. This automation streamlines the data analysis process and enhances code quality.

The ETL-Query script is a command-line interface (CLI) tool that performs Extract, Transform, Load (ETL) operations and executes general queries. You can find the user guide here [] 

### Architectural Diagram 

Below is the Architecture Diagram showcase the connection and flow between Python scripts and the Azure Databricks Database.

![SQL Python Script and Azure Databricks drawio](https://github.com/nogibjj/tinayiluo_mini_6/assets/143360909/25ed0bb8-3c03-4937-938e-a2ee3578e8a8)

### Preperation

+ I forked tinayiluo_mini_6.

+ I chose the Airline safety dataset `airline-safety.csv` from Github.

### Dataset Description

The dataset `airline-safety.csv` originates from the Aviation Safety Network and consolidates safety-related information for 56 airlines in a CSV file. It encompasses data on available seat kilometers flown every week and provides a detailed record of incidents, fatal accidents, and fatalities, each segregated into two time frames: 1985–1999 and 2000–2014.

#### [Resources](https://github.com/fivethirtyeight/data/tree/master/airline-safety) 

### Overview

#### - Setting Up Azure Databricks
- Create a new database warehouse in Azure Databricks.
- Generate authentication tokens for secure access.

#### - Prepare the Development Environment
- Install necessary libraries and requirements in `requirements.txt`:
  - Databricks specific requirements:
    - pandas
    - python-dotenv
    - databricks-sql-connector
  - Packaging Python projects:
    - setuptools

#### - Configure Environment Variables
- Set up the `.env` file with the following:
  - SERVER_HOSTNAME
  - HTTP_PATH
  - ACCESS_TOKEN

#### - Package python script in setup.py
- Setup.py
  - Packages the script into a named package, "ETLpipelineTinaYi".
  - The entire package includes components such as "mylib" and "main.py".
  - "mylib" is a sub-package inside the main "ETLpipelineTinaYi" package.
- Setup Function's Roles
  - First Part: Package creation
    - Creates the package and defines its metadata.
  - Second Part: Installation requirements
    - Specifies dependencies required for the package to run.
  - Third Part: Entry point creation
    - Establishes a command line interface, making the package executable.
    - Allows running the package by using the command ETL_query in place of python main.py.
- Overall Purpose of the Script
  - The script turns a Python module or library into a distributable package named "ETLpipelineTinaYi".
  - Once installed, users can invoke the etl_query command from their terminal.
  - This command executes an ETL process, which is represented by the main function in the main module.

```
from setuptools import setup, find_packages

# make sure the etl script outputs properly
setup(
    name="ETLpipelineTinaYi",
    version="0.1.0",
    description="ETLpipline",
    author="Tina Yi",
    author_email="tina.yi@duke.edu",
    packages=find_packages(),
    install_requires=[
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:main",
        ],
    },
)
```

#### - ETL-Query
- In my.lib, add extract.py, transform_load.py and query.py that perform:

      * ETL-Query:  [E] Extract a dataset from URL, [T] Transform, [L] Load into SQLite Database and [Q] Query

      * [E] Extract dataset from the URL to `airline-safety.csv` from Github.
      In the `extract` function:
      - Download `airline-safety.csv`
      - Split `airline-safety.csv` into two CSV files:
      - `Airline-safety1.csv`
      - `Airline-safety2.csv`
      - Saves both CSV files as separate files in the data folder.

      * [T] [L] Transform the data to get it ready for analysis and load the transformed data into Azure databricks.
      In the `load` function:
      - Set up default paths for two airline safety datasets `Airline-safety1.csv` and `Airline-safety2.csv`.
      - Read both datasets into Pandas DataFrames, `df` and `df2`.
      - Connect to Azure Databricks using the retrieved environment variables.
      - Check if 'AirlineSafety1*' exists; if not, create `AirlineSafety1DB` and populate it using `df`. Transform the dataset by adding necessary index column.
      - Check if 'AirlineSafety2*' exists; if not, create `AirlineSafety2DB` and populate it using `df2`. Transform the dataset by adding necessary index column.
      - Close the database cursor.
      - Return "success" upon completion.

      * [Q] Write and execute SQL queries to analyze and retrieve insights from the data.
      - Set a global variable LOG_FILE for logging queries in `query_log.md`.
      In the `log_query` function:
      - Logs both the SQL query and its result into `query_log.md`.
      In the `general_query` function:
      - Loads environment variables to get connection details.
      - Connects to Azure Databricks using these details.
      - Executes the provided SQL query and fetches results.
      - Logs the query and its results.
      - Closes the database connection.

#### - Implement Main Script
- Convert the `main.py` into a command-line tool that run each step independantly:
  - Extract
  - Transform and Load
  - General query execution
- Add help line to user who uses it (etl_query —help)

#### - Automated Testing
- Implement `test_main.py` to:
  - Test data extraction.
  - Test data transformation and loading.
  - Test SQL queries, especially those involving joins, aggregation, and sorting.
    ```
    def test_general_query():
    """tests general_query()"""
    query = """
    SELECT
        a.airline,
        (a.incidents_85_99 + b.incidents_00_14) AS total_incidents,
        a.fatal_accidents_85_99 + b.fatalities_85_99 AS total_fatalities_85_99,
        b.fatal_accidents_00_14 + b.fatalities_00_14 AS total_fatalities_00_14
    FROM 
        default.AirlineSafety1DB AS a
    JOIN 
        default.AirlineSafety2DB AS b
    ON 
        a.id = b.id
    ORDER BY 
        total_incidents DESC LIMIT 10;
    """
    result = subprocess.run(
        ["python", "main.py", "general_query", query],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    ```
#### - Streamline with Makefile
- Utilize Makefile to automate tasks with Github Actions.
- Make everything using etl_query command line
- add:

```bash
extract:
	etl_query extract

transform_load: 
	etl_query transform_load

query:
	etl_query general_query "SELECT a.airline, (a.incidents_85_99 + b.incidents_00_14) AS total_incidents, a.fatal_accidents_85_99 + b.fatalities_85_99 AS total_fatalities_85_99, b.fatal_accidents_00_14 + b.fatalities_00_14 AS total_fatalities_00_14 FROM default.AirlineSafety1DB AS a JOIN default.AirlineSafety2DB AS b ON a.id = b.id ORDER BY total_incidents DESC LIMIT 10;"

setup_package: 
	python setup.py develop --user
``` 
#### - Monitor Query Logs
- Use `query_log.md` to keep a record of every change made to the SQL queries.
- Command-line usage examples:
  - `etl_query general_query "..."`
  - `python test_main.py test_general_query`
  - `make query`

#### - CI/CD Setup with GitHub Actions
- Configure `cicd.yml` within GitHub Actions.
- Add necessary secrets from the `.env` file to GitHub (Secrets facilitate the connection between GitHub Actions and the Azure data warehouse.):
  - SERVER_HOSTNAME
  - HTTP_PATH
  - ACCESS_TOKEN
- The step named "install packages" uses the make install command, installs dependencies listed in a requirements.txt file.
- The "install local package" step runs the make setup_package command, which is used for installing the script itself. 
- Subsequent steps include linting the code, extracting data, transforming and loading data, querying data, running tests, formatting the code, generating output and pushing it, and finally deploying the code or application.
```
name: CI
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Environment Variables
        run: |
          echo "SERVER_HOSTNAME=${{ secrets.SERVER_HOSTNAME }}" >> $GITHUB_ENV
          echo "HTTP_PATH=${{ secrets.HTTP_PATH }}" >> $GITHUB_ENV
          echo "ACCESS_TOKEN=${{ secrets.ACCESS_TOKEN }}" >> $GITHUB_ENV
      - name: install packages
        run: make install
      - name: install local package
        run: make setup_package
      - name: lint
        run: make lint
      - name: extract 
        run: make extract 
      - name: transform_load
        run: make transform_load 
      - name: query
        run: make query
      - name: test
        run: make test
      - name: format
        run: make format
      - name: generate_and_push
        run: make generate_and_push
      - name: deploy
        run: make deploy
```
### Query Functionality

My SQL query performs several operations that highlight the use of joins, aggregation, and sorting:
* Joining the two tables `AirlineSafety1DB` and `AirlineSafety2DB` on the id column.
* Calculating the total incidents for each airline from both periods (1985-1999 and 2000-2014).
* Finding out the total fatal accidents and fatalities for each period.
* Sorting the results by total incidents in descending order to see which airlines had the most incidents over the combined period,limiting the output to the top 10 rows.

```sql
SELECT
    a.airline,
    (a.incidents_85_99 + b.incidents_00_14) AS total_incidents,
    a.fatal_accidents_85_99 + b.fatalities_85_99 AS total_fatalities_85_99,
    b.fatal_accidents_00_14 + b.fatalities_00_14 AS total_fatalities_00_14
FROM 
    default.AirlineSafety1DB AS a
JOIN 
    default.AirlineSafety2DB AS b
ON 
    a.id = b.id
ORDER BY 
    total_incidents DESC LIMIT 10;
```

1. **Join**: 
    - The query uses the `JOIN` clause to combine rows from two tables (`AirlineSafety1DB` and `AirlineSafety2DB`) based on a related column between them, which is the `id` column. This is specified in the `ON` clause (`a.id = b.id`). Thus, for each airline in the first table (`a`), it fetches the corresponding details from the second table (`b`) if there's a matching `id`.
  
2. **Aggregation**: 
    - The query aggregates or sums up data across the two periods (1985-1999 and 2000-2014) for several metrics:
        - `(a.incidents_85_99 + b.incidents_00_14) AS total_incidents`: This calculates the combined incidents for each airline over both time periods.
        - `a.fatal_accidents_85_99 + b.fatalities_85_99 AS total_fatalities_85_99`: This gives the sum of fatal accidents and fatalities from 1985 to 1999.
        - `b.fatal_accidents_00_14 + b.fatalities_00_14 AS total_fatalities_00_14`: This computes the sum of fatal accidents and fatalities from 2000 to 2014.
    - These aggregated columns are then added to the result set.

3. **Sorting**:
    - The `ORDER BY` clause sorts the combined results. In this case, it sorts by the `total_incidents` column in descending order (`DESC`). This ensures that the airlines with the most incidents over the entire period (1985-2014) appear first in the result.

4. **Limiting Results**:
    - The `LIMIT 10` at the end of the query restricts the output to only the top 10 airlines (after sorting). This is useful to view, for instance, the 10 airlines with the highest number of incidents over the studied period.

In summary, this query joins two datasets, aggregates certain metrics across two time frames, sorts the aggregated results, and then limits the output to a top 10 list.

### Query Result

[log of successful database operations](./query_log.md)

<img width="834" alt="Screen Shot 2023-10-08 at 5 05 10 PM" src="https://github.com/nogibjj/tinayiluo_mini_6/assets/143360909/e3b8864c-d463-4ccf-9b3e-e195f27c815a">


### Make Format, Test, Lint, All Approval Image

<img width="1166" alt="Screen Shot 2023-10-21 at 12 46 55 PM" src="https://github.com/nogibjj/tinayiluo_mini_7/assets/143360909/d912b3cb-8578-4cda-9163-798e04f8e928">

<img width="1142" alt="Screen Shot 2023-10-21 at 12 47 26 PM" src="https://github.com/nogibjj/tinayiluo_mini_7/assets/143360909/2c28fef7-7432-4d5c-8517-135c70dd2067">

