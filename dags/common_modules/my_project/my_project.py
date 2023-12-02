import os
import pandas as pd


def create_dataset(path: str = '/tmp/uva/dataset.csv'):
    """Create a pandas dataframe and store in the provided path."""
    os.makedirs(os.path.dirname(path), exist_ok=True)

    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    df.to_csv(path, index=False)

    print(f"Dataset stored at: {path}")

if __name__ == '__main__':
    create_dataset()
