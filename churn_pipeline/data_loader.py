import numpy as np
import pandas as pd
from churn_pipeline.config import ChurnConfig

def generate_customer_data(config:ChurnConfig)->pd.DataFrame:
    """Simulate raw customer account record
    
    Contract_type encoding:
    0= Month to month
    1= Long_term
    
    """

    np.random.seed(config.random_seeds)
    df=pd.DataFrame({
        "age": np.random.randint(18,60,config.n_sample),
        "monthly_charge": np.random.randint(20,120,config.n_sample),
        "tenure": np.random.randint(1,60,config.n_sample),
        "contract_type": np.random.choice([0.1],config.n_sample)
    })

    return df