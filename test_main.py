"""
Tests for the main.py script.
"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transform_load()"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


# Write a test query mainly creating a complex SQL query
# involving joins, aggregation, and sorting
# Joining the two tables on the id column.
# alculating the total incidents for each airline
# from both periods (1985-1999 and 2000-2014).
# Finding out the total fatalities for each period.
# Sorting the results by total incidents in descending order
# to see which airlines had the most incidents over the combined period.


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


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_general_query()
