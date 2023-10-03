from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd

def convert_categorical_to_numerical(df, columns, method="label_encoding"):
    """
    Convert categorical columns in a dataframe to numerical

    Parameters:
    - df (pd.DataFrame): The dataframe to process
    - columns (list): The columns to convert
    - method (str): The method to use ("label_encoding" or "one_hot_encoding")

    Returns:
    - pd.DataFrame: DataFrame with converted columns
    """

    if method == "label_encoding":
        le = LabelEncoder()
        for col in columns:
            df[col] = le.fit_transform(df[col])
        return df
    elif method == "one_hot_encoding":
        return pd.get_dummies(df, columns=columns)
    else:
        return ValueError(f"Unsupported method: {method}")