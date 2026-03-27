from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import TimestampType
from pyspark.sql.window import Window

def code_quality(df, name):
    '''
    Displays a basic quality report for the data frame:
    - number of records
    - number of columns
    - number and percentage of missing values ​​in each column
    - number of duplicates
    '''
    print(f"Data quality for: {name}")

    n_rows = df.count()
    n_cols = len(df.columns)
    print(f"Number of records: {n_rows}, number of columns: {n_cols}")

    # Missing values - for each column if null or "" -> 1, else 0, return sum
    missing_exprs = [
        F.sum(
            F.when(
                F.col(c).isNull() | (F.col(c) == ""), 1
            ).otherwise(0)
        ).alias(c)
        for c in df.columns
    ]

    missing_df = df.select(missing_exprs)
    print("Missing df:", missing_df.collect())
    for row in missing_df.collect():
        for col_name in df.columns:
            nulls = row[col_name]
            if nulls > 0:
                pct = 100 * nulls / n_rows
                print(f"{col_name:<25} {nulls:>8,} ({pct:.2f}%)")

    # Duplicates
    n_distinct = df.dropDuplicates().count()
    n_dup = n_rows - n_distinct

    print(f"\nDuplicates: {n_dup:,} ({100*n_dup/n_rows:.2f}%)")

    return {
        "rows": n_rows,
        "columns": n_cols,
        "duplicates": n_dup,
        "missing": missing_df
    }


def parse_date(df, column="date"):
    """
    Converts date type columns to Timestamp
    Format that CERT uses: MM/DD/YYYY HH:MM:SS
    Returns timestamp column and datetime slices as year, month, day, hour, day_of_the_week
    """
    df = df.withColumn(
        "timestamp",
        F.to_timestamp(F.col(column), "MM/dd/yyyy HH:mm:ss")
    )
    df = df.withColumn("year", F.year("timestamp"))
    df = df.withColumn("month", F.month("timestamp"))
    df = df.withColumn("day", F.day("timestamp"))
    df = df.withColumn("hour", F.hour("timestamp"))
    # day of week: 1 - Sunday 
    df = df.withColumn("day_of_the_week", F.dayofweek("timestamp"))
    # Flag - whether the incident happened during of after business hours
    df = df.withColumn("not_working_hours", (F.col("hour") < 8) | (F.col("hour") > 18 ))
    return df


def letters_cleaning(df):
    # Convert column names to lower case
    new_columns = [c.lower() for c in df.columns]
    return df.toDF(*new_columns)