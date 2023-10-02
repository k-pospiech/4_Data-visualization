def handle_missing_values(df, method='drop', fill_value=None):
    """
    Handle missing values in a dataframe

    Parameters:
    - df (pd.DataFrame): The dataframe to process
    - method (str): The method to handle missing values ("drop" or "fill")
    - fill_value (scalar or dict): The value to fill missing values with if method="fill"
      Can be a scalar or a dict specifying values for each column

    Retruns:
    - pd.DataFrame: DataFrame with handled missing values
    """

    if method == "drop":
        return df.dropna()
    elif method == "fill":
        return df.fillna(fill_value)
    else:
        raise ValueError(f"Unsupported method: {method}")