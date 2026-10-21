from dataclasses import dataclass,field
from typing import List


@dataclass
class ChurnConfig:
    """Configurations holding hyperparameters,thresholds, and column definitions."""

    
    n_sample:int =100
    random_seeds=42

    monthly_charge_threshold:float=80.0
    tenure_threshold:int=20


    target_column:str="churn"
    feature_column:List[str]=field(
        default_factory=lambda:["age","monthly_charge","tenure","contract_type"]
    )