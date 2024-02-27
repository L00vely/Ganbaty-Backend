# date_columns.py
import pandas as pd

def date_columns(df, sample_size=10):
    """
    Returns a list of column names that can be interpreted as dates.

    Args:
    df (pandas.DataFrame): The DataFrame to check for date columns.
    sample_size (int): Number of rows to sample from each column.

    Returns:
    list: A list of column names that can be interpreted as dates.
    """
    date_columns_list = []
    
    for column in df.columns:
        try:
            pd.to_datetime(df[column], format='%d-%m-%Y', errors='raise')
            date_columns_list.append(column)
        except ValueError:
            pass
            # print(f"Columna '{column}' contiene valores no convertibles a fecha.")

    return date_columns_list