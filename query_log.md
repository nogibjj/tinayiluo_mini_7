```sql
SELECT a.airline, (a.incidents_85_99 + b.incidents_00_14) AS total_incidents, a.fatal_accidents_85_99 + b.fatalities_85_99 AS total_fatalities_85_99, b.fatal_accidents_00_14 + b.fatalities_00_14 AS total_fatalities_00_14 FROM default.AirlineSafety1DB AS a JOIN default.AirlineSafety2DB AS b ON a.id = b.id ORDER BY total_incidents DESC LIMIT 10;
```

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

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

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

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

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

```sql
SELECT a.airline, (a.incidents_85_99 + b.incidents_00_14) AS total_incidents, a.fatal_accidents_85_99 + b.fatalities_85_99 AS total_fatalities_85_99, b.fatal_accidents_00_14 + b.fatalities_00_14 AS total_fatalities_00_14 FROM default.AirlineSafety1DB AS a JOIN default.AirlineSafety2DB AS b ON a.id = b.id ORDER BY total_incidents DESC LIMIT 10;
```

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

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

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

```sql
SELECT a.airline, (a.incidents_85_99 + b.incidents_00_14) AS total_incidents, a.fatal_accidents_85_99 + b.fatalities_85_99 AS total_fatalities_85_99, b.fatal_accidents_00_14 + b.fatalities_00_14 AS total_fatalities_00_14 FROM default.AirlineSafety1DB AS a JOIN default.AirlineSafety2DB AS b ON a.id = b.id ORDER BY total_incidents DESC LIMIT 10;
```

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

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

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

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

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

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

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

```sql
SELECT a.airline, (a.incidents_85_99 + b.incidents_00_14) AS total_incidents, a.fatal_accidents_85_99 + b.fatalities_85_99 AS total_fatalities_85_99, b.fatal_accidents_00_14 + b.fatalities_00_14 AS total_fatalities_00_14 FROM default.AirlineSafety1DB AS a JOIN default.AirlineSafety2DB AS b ON a.id = b.id ORDER BY total_incidents DESC LIMIT 10;
```

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

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

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

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

```response from databricks
[Row(airline='Aeroflot*', total_incidents=82, total_fatalities_85_99=142, total_fatalities_00_14=89), Row(airline='Delta / Northwest*', total_incidents=48, total_fatalities_85_99=419, total_fatalities_00_14=53), Row(airline='American*', total_incidents=38, total_fatalities_85_99=106, total_fatalities_00_14=419), Row(airline='United / Continental*', total_incidents=33, total_fatalities_85_99=327, total_fatalities_00_14=111), Row(airline='Ethiopian Airlines', total_incidents=30, total_fatalities_85_99=172, total_fatalities_00_14=94), Row(airline='US Airways / America West*', total_incidents=27, total_fatalities_85_99=231, total_fatalities_00_14=25), Row(airline='Air France', total_incidents=20, total_fatalities_85_99=83, total_fatalities_00_14=339), Row(airline='Pakistan International', total_incidents=18, total_fatalities_85_99=237, total_fatalities_00_14=48), Row(airline='Saudi Arabian', total_incidents=18, total_fatalities_85_99=315, total_fatalities_00_14=0), Row(airline='Turkish Airlines', total_incidents=16, total_fatalities_85_99=67, total_fatalities_00_14=86)]
```

