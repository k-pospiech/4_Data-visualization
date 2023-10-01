import pandas as pd

def load_data(filepath, file_type="csv", **kwargs):
    """
    Loads data from the given file path.

    Paramters:
    - filepath (str): Path to the data file
    - file_type (str): Type of the file ('csv', 'excel', etc.)
    - **kwargs: Additional arguments to pass to the loading function

    Returns:
    - pd.DataFrame: Loaded data
    """

    if file_type == "csv":
        return pd.read_csv(filepath, **kwargs)
    elif file_type == "excel":
        return pd.read_excel(filepath, **kwargs)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")
    
    