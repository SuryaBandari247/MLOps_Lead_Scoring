import pandas as pd
from Lead_scoring_data_pipeline.constants import *
from Lead_scoring_data_pipeline.schema import *
import sqlite3
from sqlite3 import Error


###############################################################################

# Define function to validate raw data's schema
############################################################################## 

def raw_data_schema_check():
    '''
    This function check if all the columns mentioned in schema.py are present in
    leadscoring.csv file or not.

   
    INPUTS
        DATA_DIRECTORY : path of the directory where 'leadscoring.csv' 
                        file is present
        raw_data_schema : schema of raw data in the form oa list/tuple as present 
                          in 'schema.py'

    OUTPUT
        If the schema is in line then prints 
        'Raw datas schema is in line with the schema present in schema.py' 
        else prints
        'Raw datas schema is NOT in line with the schema present in schema.py'

    
    SAMPLE USAGE
        raw_data_schema_check
    '''
    data_file_path = DATA_DIRECTORY + DATA_FLE_NAME
    
    df = pd.read_csv(data_file_path, index_col=[0])
    
    columns_list = df.columns.to_list()

    if columns_list == raw_data_schema:
        print('Raw datas schema is in line with the schema present in schema.py')
    else:
        print('Raw datas schema is NOT in line with the schema present in schema.py')
    

###############################################################################
# Define function to validate model's input schema
# ############################################################################## 

def model_input_schema_check():
    '''
    This function check if all the columns mentioned in model_input_schema in 
    schema.py are present in table named in 'model_input' in db file.

   
    INPUTS
        DB_FILE_NAME : Name of the database file
        DB_PATH : path where the db file should be present
        model_input_schema : schema of models input data in the form oa list/tuple
                          present as in 'schema.py'

    OUTPUT
        If the schema is in line then prints 
        'Models input schema is in line with the schema present in schema.py'
        else prints
        'Models input schema is NOT in line with the schema present in schema.py'
    
    SAMPLE USAGE
        raw_data_schema_check
    '''
    conn = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    
    df = pd.read_sql_query('SELECT * FROM model_input',conn)
    
    columns_list = df.columns.to_list()
    
    if sorted(columns_list) == sorted(model_input_schema):
        print('Models input schema is in line with the schema present in schema.py')
    else:
        print('Models input schema is NOT in line with the schema present in schema.py')
    conn.close()
    
    
