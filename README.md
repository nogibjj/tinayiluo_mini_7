## Package a Python Script into a Command-Line Tool
[![CI](https://github.com/nogibjj/tinayiluo_mini_6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/tinayiluo_mini_6/actions/workflows/cicd.yml)

mini_7_project 

Week 7: Package a Python Script into a Command-Line Tool
Requirements
* Package a Python script with setuptools or a similar tool
* Include a user guide on how to install and use the tool
* Include communication with an external or internal database (NoSQL, SQL, etc)
Grading Criteria
* Functionality of the tool (20 points)
* User guide clarity (20 points)
Deliverables
* Python package
* User guide (PDF or markdown)

### Goal

+ Automate the interaction between the Python script and the SQL database.

+ Implement a Python script to interface with the SQL database on Azure Databricks.

+ Design a complex SQL query involving joins, aggregation, and sorting. 

The workflow includes running a Makefile to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`) with Python Black, linting (`make lint`) with Ruff, and an all-inclusive task (`make all`) using `Github Actions`. This automation streamlines the data analysis process and enhances code quality.

### Preperation

+ I forked tinayiluo_sqlite_lab.

+ I chose the Airline safety dataset `airline-safety.csv` from Github.

### Dataset Description

The dataset `airline-safety.csv` originates from the Aviation Safety Network and consolidates safety-related information for 56 airlines in a CSV file. It encompasses data on available seat kilometers flown every week and provides a detailed record of incidents, fatal accidents, and fatalities, each segregated into two time frames: 1985–1999 and 2000–2014.

#### [Resources](https://github.com/fivethirtyeight/data/tree/master/airline-safety) 

### Overview

- **Objective:** Connect a Python script to a SQL Database on Azure Databricks and perform complex SQL queries involving joins, aggregation, and sorting.
- **Key Takeaway:** Leveraging the power of the cloud with Azure for database operations.

#### Step 1: Setting Up Azure Databricks
- Create a new database warehouse in Azure Databricks.
- Generate authentication tokens for secure access.

#### Step 2: Prepare the Development Environment
- Install necessary libraries and requirements in `requirements.txt`:
  - Databricks specific requirements:
    - pandas
    - python-dotenv
    - databricks-sql-connector

#### Step 3: Configure Environment Variables
- Set up the `.env` file with the following:
  - SERVER_HOSTNAME
  - HTTP_PATH
  - ACCESS_TOKEN

#### Step 4: ETL-Query
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

<img width="748" alt="Screen Shot 2023-10-08 at 6 25 05 PM" src="https://github.com/nogibjj/tinayiluo_sqlite_lab/assets/143360909/e642c00e-7481-4ad9-b325-4fd50e338152">

#### Step 5: Implement Main Script
- Convert the `main.py` into a command-line tool that run each step independantly:
  - Extract
  - Transform and Load
  - General query execution

#### Step 6: Automated Testing
- Implement `test_main.py` to:
  - Test data extraction.
  - Test data transformation and loading.
  - Test SQL queries, especially those involving joins, aggregation, and sorting.

#### Step 7: Streamline with Makefile
- Utilize Makefile to automate tasks with Github Actions.
- add:

```bash
extract:
	python main.py extract

transform_load: 
	python main.py transform_load

query:
	python main.py general_query "SELECT a.airline, (a.incidents_85_99 + b.incidents_00_14) AS total_incidents, a.fatal_accidents_85_99 + b.fatalities_85_99 AS total_fatalities_85_99, b.fatal_accidents_00_14 + b.fatalities_00_14 AS total_fatalities_00_14 FROM default.AirlineSafety1DB AS a JOIN default.AirlineSafety2DB AS b ON a.id = b.id ORDER BY total_incidents DESC LIMIT 10;"
``` 
#### Step 8: Monitor Query Logs
- Use `query_log.md` to keep a record of every change made to the SQL queries.
- Command-line usage examples:
  - `python main.py general_query "..."`
  - `python test_main.py test_general_query`
  - `make query`

#### Step 9: CI/CD Setup with GitHub Actions
- Configure `cicd.yml` within GitHub Actions.
- Add necessary secrets from the `.env` file to GitHub:
  - SERVER_HOSTNAME
  - HTTP_PATH
  - ACCESS_TOKEN
- Explanation: Secrets facilitate the connection between GitHub Actions and the Azure data warehouse.

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

### Architectural Diagram 

Below is the Architecture Diagram showcase the connection and flow between Python scripts and the Azure Databricks Database.

![SQL Python Script and Azure Databricks drawio](https://github.com/nogibjj/tinayiluo_mini_6/assets/143360909/25ed0bb8-3c03-4937-938e-a2ee3578e8a8)

### Make Format, Test, Lint, All Approval Image

<img width="1022" alt="Screen Shot 2023-10-08 at 7 55 24 PM" src="https://github.com/nogibjj/tinayiluo_mini_6/assets/143360909/1550aa2c-9943-4c53-a508-3dbdc62921b9">
<img width="1019" alt="Screen Shot 2023-10-08 at 7 54 48 PM" src="https://github.com/nogibjj/tinayiluo_mini_6/assets/143360909/3a832449-b8b5-4d0b-a7f1-a5ae4301c48b">
