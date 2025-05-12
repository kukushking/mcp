import pandas as pd


def format_pandas(df: pd.DataFrame) -> str:
    """Format Pandas DataFrame."""
    return df.astype('str').to_markdown()
