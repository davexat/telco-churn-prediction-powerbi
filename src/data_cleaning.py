import pandas as pd
from src.utils import get_data_path

def get_raw_dataset() -> pd.DataFrame:
    subfolder = 'raw'
    filename = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
    return pd.read_csv(get_data_path(subfolder, filename))