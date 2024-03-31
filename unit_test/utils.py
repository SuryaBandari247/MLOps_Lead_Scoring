##############################################################################
# Import necessary modules and files
##############################################################################


import pandas as pd
import os
import sqlite3
from sqlite3 import Error
from constants import *
from significant_categorical_level import *



###############################################################################
# Define the function to build database
###############################################################################

def build_dbs():
    '''
    This function checks if the db file with specified name is present 
    in the /Assignment/01_data_pipeline/scripts folder. If it is not present it creates 
    the db file with the given name at the given path. 


    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should exist  


    OUTPUT
    The function returns the following under the given conditions:
        1. If the file exists at the specified path
                prints 'DB Already Exists' and returns 'DB Exists'

        2. If the db file is not present at the specified loction
                prints 'Creating Database' and creates the sqlite db 
                file at the specified path with the specified name and 
                once the db file is created prints 'New DB Created' and 
                returns 'DB created'


    SAMPLE USAGE
        build_dbs()
    '''
    db_file_path = os.path.join(DB_PATH, DB_FILE_NAME)
    if os.path.exists(db_file_path):
        print('Creating Database')
        conn_1=None
        try:
            conn_1 = sqlite3.connect(db_file_path)
            print('New DB Created')
        except Error as er:
            print(f'exception occurred during db creation:{er}' )
        finally:
            if conn_1:
                conn_1.close()
        return 'DB created'
    else:
        print('DB Already Exists') 
        return 'DB Exists'

###############################################################################
# Define function to load the csv file to the database
###############################################################################

def load_data_into_db():
    '''
    Thie function loads the data present in data directory into the db
    which was created previously.
    It also replaces any null values present in 'total_leads_dropped' and
    'referred_lead' columns with 0.


    INPUTS
        DB_FILE_NAME : Name of the database file
        DB_PATH : path where the db file should be
        DATA_DIRECTORY : path of the directory where 'leadscoring.csv' 
                        file is present
        

    OUTPUT
        Saves the processed dataframe in the db in a table named 'loaded_data'.
        If the table with the same name already exsists then the function 
        replaces it.


    SAMPLE USAGE
        load_data_into_db()
    '''
    if os.path.exists(DATA_DIRECTORY+DATA_FLE_NAME):
        df = pd.read_csv(DATA_DIRECTORY+DATA_FLE_NAME)
        
        df["total_leads_droppped"] = df["total_leads_droppped"].fillna(0)
        df["referred_lead"] = df["referred_lead"].fillna(0)
        
        conn_1 = sqlite3.connect(DB_PATH + DB_FILE_NAME)
        df.to_sql('loaded_data', conn_1, if_exists='replace', index=False)
        
        print('load_data_into_db completed')
        print(DB_PATH + DB_FILE_NAME)
        conn_1.close()
        
    else:
        print(f'{DATA_DIRECTORY+DATA_FLE_NAME} file is missing')
        
    


###############################################################################
# Define function to map cities to their respective tiers
###############################################################################

    
def map_city_tier():
    '''
    This function maps all the cities to their respective tier as per the
    mappings provided in the city_tier_mapping.py file. If a
    particular city's tier isn't mapped(present) in the city_tier_mapping.py 
    file then the function maps that particular city to 3.0 which represents
    tier-3.


    INPUTS
        DB_FILE_NAME : Name of the database file
        DB_PATH : path where the db file should be
        city_tier_mapping : a dictionary that maps the cities to their tier

    
    OUTPUT
        Saves the processed dataframe in the db in a table named
        'city_tier_mapped'. If the table with the same name already 
        exsists then the function replaces it.

    
    SAMPLE USAGE
        map_city_tier()

    '''
    table = 'loaded_data'
    file_path = city_tier_mapping
    
    parameters = {}
    with open(file_path, 'r') as file:
        exec(file.read(), parameters)
    mapping = parameters.get('city_tier_mapping',{})
    
    conn_1 = sqlite3.connect(DB_PATH + DB_FILE_NAME)
    
    query = f"SELECT * FROM {table}"
    df = pd.read_sql_query(query, conn_1)
    
    df["city_tier"] = df["city_mapped"].map(mapping)
    df["city_tier"] = df["city_tier"].fillna(3.0)
    
    df = df.drop(['city_mapped'],axis=1)
    df.to_sql('city_tier_mapping',conn_1,if_exists='replace', index=False)
    
    print('map_city_tier completed')
    
    conn_1.close()
    
    
    

###############################################################################
# Define function to map insignificant categorial variables to "others"
###############################################################################


def map_categorical_vars():
    '''
    This function maps all the insignificant variables present in 'first_platform_c'
    'first_utm_medium_c' and 'first_utm_source_c'. The list of significant variables
    should be stored in a python file in the 'significant_categorical_level.py' 
    so that it can be imported as a variable in utils file.
    

    INPUTS
        DB_FILE_NAME : Name of the database file
        DB_PATH : path where the db file should be present
        list_platform : list of all the significant platform.
        list_medium : list of all the significat medium
        list_source : list of all rhe significant source

        **NOTE : list_platform, list_medium & list_source are all constants and
                 must be stored in 'significant_categorical_level.py'
                 file. The significant levels are calculated by taking top 90
                 percentils of all the levels. For more information refer
                 'data_cleaning.ipynb' notebook.
  

    OUTPUT
        Saves the processed dataframe in the db in a table named
        'categorical_variables_mapped'. If the table with the same name already 
        exsists then the function replaces it.

    
    SAMPLE USAGE
        map_categorical_vars()
    '''
    conn_1 = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    table = 'city_tier_mapping'
    
    query = f"SELECT * FROM {table}"
    df = pd.read_sql_query(query, conn_1)
    
    new_df = df[~df['first_platform_c'].isin(list_platform)]
    new_df['first_platform_c'] = "others"
    old_df = df[df['first_platform_c'].isin(list_platform)] 
    df = pd.concat([new_df, old_df])
    
    new_df = df[~df['first_utm_medium_c'].isin(list_medium)]
    new_df['first_utm_medium_c'] = "others"
    old_df = df[df['first_utm_medium_c'].isin(list_medium)]
    df = pd.concat([new_df, old_df])
    
    new_df = df[~df['first_utm_source_c'].isin(list_source)]
    new_df['first_utm_source_c'] = "others"
    old_df = df[df['first_utm_source_c'].isin(list_source)]
    df = pd.concat([new_df, old_df])
    
    df.to_sql('categorical_variables_mapped',conn_1,if_exists='replace', index=False)
    
    print('map_categorical_vars completed')
    
    conn_1.close()

##############################################################################
# Define function that maps interaction columns into 4 types of interactions
##############################################################################
def interactions_mapping():
    '''
    This function maps the interaction columns into 4 unique interaction columns
    These mappings are present in 'interaction_mapping.csv' file. 


    INPUTS
        DB_FILE_NAME: Name of the database file
        DB_PATH : path where the db file should be present
        INTERACTION_MAPPING : path to the csv file containing interaction's
                                   mappings
        INDEX_COLUMNS_TRAINING : list of columns to be used as index while pivoting and
                                 unpivoting during training
        INDEX_COLUMNS_INFERENCE: list of columns to be used as index while pivoting and
                                 unpivoting during inference
        NOT_FEATURES: Features which have less significance and needs to be dropped
                                 
        NOTE : Since while inference we will not have 'app_complete_flag' which is
        our label, we will have to exculde it from our features list. It is recommended 
        that you use an if loop and check if 'app_complete_flag' is present in 
        'categorical_variables_mapped' table and if it is present pass a list with 
        'app_complete_flag' column, or else pass a list without 'app_complete_flag'
        column.

    
    OUTPUT
        Saves the processed dataframe in the db in a table named 
        'interactions_mapped'. If the table with the same name already exsists then 
        the function replaces it.
        
        It also drops all the features that are not requried for training model and 
        writes it in a table named 'model_input'

    
    SAMPLE USAGE
        interactions_mapping()
    '''
    conn_1 = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    table = 'categorical_variables_mapped'
    
    query = f"SELECT * FROM {table}"
    df = pd.read_sql_query(query, conn_1)
    
    if 'app_complete_flag' in df.columns:
        index_columns = INDEX_COLUMNS_TRAINING
    else:
        index_columns = INDEX_COLUMNS_INFERENCE
    
    df = df.drop_duplicates()
    
    df_event_mapping = pd.read_csv(INTERACTION_MAPPING, index_col=[0])
    
    df_unpivot = pd.melt(df, id_vars=index_columns, var_name='interaction_type', value_name='interaction_value')    
    df_unpivot['interaction_value'] = df_unpivot['interaction_value'].fillna(0)
    
    df = pd.merge(df_unpivot, df_event_mapping, on='interaction_type', how='left')
    
    df = df.drop(['interaction_type'], axis=1)
    
    df_pivot = df.pivot_table(values='interaction_value', index=index_columns, columns='interaction_mapping', aggfunc='sum')
    df_pivot = df_pivot.reset_index()
   
    df_pivot.to_sql('interactions_mapped',conn_1,if_exists='replace', index=False)
    
    df_model_input = df_pivot.drop(NOT_FEATURES, axis=1)
    df_model_input.to_sql('model_input',conn_1,if_exists='replace', index=False)
    
    print('interactions_mapping completed')
    
    conn_1.close()