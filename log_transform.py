import math
import pandas as pd

def log_transform(df: pd.DataFrame, columns: list, base: float = math.e) -> pd.DataFrame:
    """
    Applies log transformation to specified columns of a DataFrame.

    Parameters:
    df (DataFrame): Input dataframe
    columns (list): List of column names to apply log transform
    base (float): Logarithmic base (default natural log)

    Returns:
    DataFrame: DataFrame with log-transformed columns
    """

    for col in columns:
        if (df[col] <= 0).any():
            raise ValueError(f"All values in column {col} must be positive for log transformation.")
        df[col] = df[col].apply(lambda x: math.log(x, base))

    return df

