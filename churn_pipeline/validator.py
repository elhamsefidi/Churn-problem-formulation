import pandas as pd
from churn_pipeline.config import ChurnConfig

def inspect_dataset(df:pd.DataFrame)->None:
    """Print straucrural metadata and summery statistics"""
    print("--Dataset Information")
    df.info()

    print("--Summery Statistic--")
    print(df.describe())


def validate_ml_task(X:pd.DataFrame, y:pd.Series)->None:
    """ Validate tensor shape and print class distribution"""
    print("\n-- ML Task Formulation--")
    print("--Task Type: Binary Classification--")
    print(f" Feature Matrix shape (X):{X.shape}")
    print(f"Target vectore shape (y):{y.shape}")

    print("--Target Class Balance--")
    balance_df=pd.DataFrame({"count":y.value_counts(), "percentage": y.value_counts(normalize=True)*100})
    print(balance_df)