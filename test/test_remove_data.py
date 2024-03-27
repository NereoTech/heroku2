import pandas as pd
from src.process_data import fic_export_data

def remove_data(df: pd.DataFrame, last_n_samples: int = 4*3):

    # df: pd.DataFrame = pd.read_csv(fic_export_data)
    return df.iloc[:-last_n_samples]
    # df.to_csv(fic_export_data, index=False)

