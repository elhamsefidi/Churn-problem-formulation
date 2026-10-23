from churn_pipeline.config import ChurnConfig
from churn_pipeline.data_loader import generate_customer_data
from churn_pipeline.label_engineering import create_churn_label, splite_feature_target
from churn_pipeline.validator import inspect_dataset, validate_ml_task
from churn_pipeline.visulizer import plot_target_distribution



if __name__=="__main__":
    cfg=ChurnConfig()
    
    df=generate_customer_data(cfg)

    df=create_churn_label(cfg,df)
    X,y=splite_feature_target(cfg,df)

    inspect_dataset(df)
    validate_ml_task(X,y)
    plot_target_distribution(y)

    
    





