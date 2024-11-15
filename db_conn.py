import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables
load_dotenv()

# Function to establish MySQL connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

# Function to fetch a table as a DataFrame
def fetch_table_as_dataframe(table_name):
    connection = create_connection()
    if connection:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, connection)
        connection.close()
        return df
    else:
        print(f"Failed to connect to fetch {table_name}")
        return None

# Function to fetch all specified tables as DataFrames
def fetch_all_tables():
    tables = ['user', 'file', 'folder', 'verification', 'auth_log']
    dataframes = {}
    for table in tables:
        dataframes[table] = fetch_table_as_dataframe(table)
    return dataframes

# Function to get the total count of users
def get_total_users():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM user")
        total_users = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return total_users
    return None

# Function to get the count of active users
def get_active_users():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM user WHERE is_active = 1")
        active_users = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return active_users
    return None
