
# delete_date_columns.py
from utils.date_columns import date_columns
import pandas as pd     


def delete_date_columns(df):
    """
    Delete all the dates columns.

    Args:
    df (pandas.DataFrame): The DataFrame to convert.
    """
    columns = date_columns(df)

    for column in columns:
        df = df.drop(column, axis=1)
    
    return df
