DB_PATH = '/home/airflow/dags/Lead_scoring_data_pipeline/'
DB_FILE_NAME = 'lead_scoring_data_cleaning.db'
DATA_DIRECTORY = '/home/airflow/dags/Lead_scoring_data_pipeline/data/'
DATA_FLE_NAME='leadscoring.csv' #'leadscoring_inference.csv'
city_tier_mapping = '/home/airflow/dags/Lead_scoring_data_pipeline/mapping/city_tier_mapping.py'
INTERACTION_MAPPING = '/home/airflow/dags/Lead_scoring_data_pipeline/mapping/interaction_mapping.csv'
INDEX_COLUMNS_TRAINING = ['created_date', 'first_platform_c', 'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'city_tier','referred_lead', 'app_complete_flag']
INDEX_COLUMNS_INFERENCE = ['created_date', 'first_platform_c', 'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'city_tier','referred_lead']
NOT_FEATURES = ['created_date','assistance_interaction','career_interaction','payment_interaction','social_interaction','syllabus_interaction']




