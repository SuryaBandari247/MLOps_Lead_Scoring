DB_PATH = '/home/airflow/dags/Lead_scoring_data_pipeline/'
DB_FILE_NAME = 'lead_scoring_data_cleaning.db'

DB_FILE_MLFLOW = 'Lead_scoring_mlflow_production.db'

TRACKING_URI = 'http://0.0.0.0:6006'
EXPERIMENT = 'Lead_scoring_mlflow_production'


# model config imported from pycaret experimentation
model_config = {'actual_estimator__reg_lambda': 0.7, 'actual_estimator__reg_alpha': 0.0005, 'actual_estimator__num_leaves': 40, 'actual_estimator__n_estimators': 90, 'actual_estimator__min_split_gain': 0.1, 'actual_estimator__min_child_samples': 81, 'actual_estimator__learning_rate': 0.2, 'actual_estimator__feature_fraction': 0.7, 'actual_estimator__bagging_freq': 3, 'actual_estimator__bagging_fraction': 0.6}

# list of the features that needs to be there in the final encoded dataframe
ONE_HOT_ENCODED_FEATURES = ['created_date', 'first_platform_c_Level0', 'first_platform_c_Level3', 'first_platform_c_Level7', 'first_platform_c_Level1', 'first_platform_c_Level2', 'first_platform_c_Level8','first_platform_c_others', 'first_utm_medium_c_Level0', 'first_utm_medium_c_Level2', 'first_utm_medium_c_Level6', 'first_utm_medium_c_Level3', 'first_utm_medium_c_Level4', 'first_utm_medium_c_Level9', 'first_utm_medium_c_Level11', 'first_utm_medium_c_Level5', 'first_utm_medium_c_Level8', 'first_utm_medium_c_Level20', 'first_utm_medium_c_Level13', 'first_utm_medium_c_Level30', 'first_utm_medium_c_Level33', 'first_utm_medium_c_Level16', 'first_utm_medium_c_Level10', 'first_utm_medium_c_Level15', 'first_utm_medium_c_Level26', 'first_utm_medium_c_Level43','first_utm_medium_others', 'first_utm_source_c_Level2', 'first_utm_source_c_Level0', 'first_utm_source_c_Level7', 'first_utm_source_c_Level4', 'first_utm_source_c_Level6', 'first_utm_source_c_Level16', 'first_utm_source_c_Level5', 'first_utm_source_c_Level14', 'total_leads_droppped', 'city_tier','referred_lead', 'app_complete_flag']

# list of features that need to be one-hot encoded
FEATURES_TO_ENCODE = ['first_platform_c', 'first_utm_medium_c', 'first_utm_source_c']
