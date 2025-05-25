import pandas as pd

def load_and_clean_data(filepath):
    # Load data
    df = pd.read_csv(filepath, names=["userId", "productId", "rating"], header=None)

    # Drop duplicates
    df = df.drop_duplicates()

    # Check and drop missing values
    df = df.dropna()

    # Convert data types if needed
    df['rating'] = df['rating'].astype(float)

    return df
