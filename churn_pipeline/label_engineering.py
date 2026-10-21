import pandas as pd
from churn_pipeline.config import ChurnConfig


def create_churn_label(config:ChurnConfig, df:pd.DataFrame)->pd.DataFrame:
    """
    Customers with high monthly charges (> threshold) and low tenure (< threshold)
    are flagged as churned (1), otherwise retained (0).
    """

    df=df.copy()
    
    df[config.target_column]=(
        (df["monthly_charge"] > config.monthly_charge_threshold) &
    (df["tenure"]< config.tenure_threshold)).astype(int)
    return df


def splite_feature_target(config:ChurnConfig, df:pd.DataFrame)-> tuple[pd.DataFrame, pd.Series]:
    """ Seperate the feature matrix X from targer vector Y """
    x=df[config.feature_column].copy()
    y=df[config.target_column].copy()
    return x,y



