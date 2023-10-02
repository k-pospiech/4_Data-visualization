from sklearn.preprocessing import MinMaxScaler

def normalize_data(df, columns=None):
    """
    Normalized specified columns in a dataframe to the range [0,  1].

    Parameters:
    - df (pd.DataFrame): The dataframe to normalize
    - columns (list): The columns to normalize. If None, all columns are normalized
    
    Returns:
    - pd.DataFrame: DataFrame with normalized columns
    """

    scaler = MinMaxScaler()
    if columns is None:
        columns = df.columns

    df[columns] = scaler.fit_transform(df[columns])

    return df