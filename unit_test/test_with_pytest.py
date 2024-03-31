##############################################################################
# Import the necessary modules
##############################################################################
import sqlite3
from sqlite3 import Error
import pandas as pd
from constants import *
import utils
import pytest

###############################################################################
# Write test cases for load_data_into_db() function
# ##############################################################################

def test_load_data_into_db():
    """_summary_
    This function checks if the load_data_into_db function is working properly by
    comparing its output with test cases provided in the db in a table named
    'loaded_data_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'

    SAMPLE USAGE
        output=test_get_data()

    """
    conn_main = sqlite3.connect(TEST_DB_PATH+DB_FILE_NAME)
    conn_test = sqlite3.connect(TEST_DB_PATH+UNIT_TEST_DB_FILE_NAME)
    
    utils.load_data_into_db()
    df_main = pd.read_sql_query('SELECT * from loaded_data',conn_main)
    df_test = pd.read_sql_query('SELECT * from loaded_data_test_case',conn_test)
    
    conn_main.close()
    conn_test.close()
    
    assert df_main.equals(df_test), 'Test Failed: Data does not match the test cases'
    
    
    
    

###############################################################################
# Write test cases for map_city_tier() function
# ##############################################################################
def test_map_city_tier():
    """_summary_
    This function checks if map_city_tier function is working properly by
    comparing its output with test cases provided in the db in a table named
    'city_tier_mapped_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'

    SAMPLE USAGE
        output=test_map_city_tier()

    """
    conn_main = sqlite3.connect(TEST_DB_PATH+DB_FILE_NAME)
    conn_test = sqlite3.connect(TEST_DB_PATH+UNIT_TEST_DB_FILE_NAME)
    
    utils.map_city_tier()
    df_main = pd.read_sql_query('SELECT * from city_tier_mapping',conn_main)
    df_test = pd.read_sql_query('SELECT * from city_tier_mapped_test_case',conn_test)
    
    print(df_main.columns)
    print(df_test.columns)
    
    
    conn_main.close()
    conn_test.close()
    
    assert df_main.equals(df_test), 'Test Failed: Data does not match the test cases'
    
    
###############################################################################
# Write test cases for map_categorical_vars() function
# ##############################################################################    
def test_map_categorical_vars():
    """_summary_
    This function checks if map_cat_vars function is working properly by
    comparing its output with test cases provided in the db in a table named
    'categorical_variables_mapped_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'
    
    SAMPLE USAGE
        output=test_map_cat_vars()

    """
    conn_main = sqlite3.connect(TEST_DB_PATH+DB_FILE_NAME)
    conn_test = sqlite3.connect(TEST_DB_PATH+UNIT_TEST_DB_FILE_NAME)
    
    utils.map_categorical_vars()
    df_main = pd.read_sql_query('SELECT * from categorical_variables_mapped ',conn_main)
    df_test = pd.read_sql_query('SELECT * from categorical_variables_mapped_test_case',conn_test)
    
    print(df_main.columns)
    print(df_test.columns)
    
    
    conn_main.close()
    conn_test.close()
    
    assert df_main.equals(df_test), 'Test Failed: Data does not match the test cases'
    

###############################################################################
# Write test cases for interactions_mapping() function
# ##############################################################################    
def test_interactions_mapping():
    """_summary_
    This function checks if test_column_mapping function is working properly by
    comparing its output with test cases provided in the db in a table named
    'interactions_mapped_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'

    SAMPLE USAGE
        output=test_column_mapping()

    """ 
    conn_main = sqlite3.connect(TEST_DB_PATH+DB_FILE_NAME)
    conn_test = sqlite3.connect(TEST_DB_PATH+UNIT_TEST_DB_FILE_NAME)
    
    utils.interactions_mapping()
    df_main = pd.read_sql_query('SELECT * from interactions_mapped',conn_main)
    df_test = pd.read_sql_query('SELECT * from interactions_mapped_test_case',conn_test)
    
    print(df_main.shape)
    print(df_test.shape)
    
    
    conn_main.close()
    conn_test.close()
    
    assert df_main.shape == df_test.shape, 'Test Failed: Data does not match the test cases'
