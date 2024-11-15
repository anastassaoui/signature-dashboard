import mysql.connector
import streamlit as st
import pandas as pd

# Function to establish MySQL connection using st.secrets with nested structure
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=st.secrets["connections"]["dbx"]["host"],
            user=st.secrets["connections"]["dbx"]["username"],
            password=st.secrets["connections"]["dbx"]["password"],
            database=st.secrets["connections"]["dbx"]["database"],
            port=st.secrets["connections"]["dbx"]["port"]
        )
        if connection.is_connected():
            return connection
    except mysql.connector.Error as e:
        st.write(f"Error while connecting to MySQL: {e}")
        return None

# Function to fetch a table as a DataFrame
def fetch_table_as_dataframe(table_name):
    connection = create_connection()
    if connection:
        try:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, connection)
            return df
        except Exception as e:
            print(f"Error fetching data from table {table_name}: {e}")
            return None
        finally:
            connection.close()
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
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM user")
            total_users = cursor.fetchone()[0]
            return total_users
        except Error as e:
            print(f"Error fetching total users count: {e}")
            return None
        finally:
            cursor.close()
            connection.close()

# Function to get the count of active users
def get_active_users():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM user WHERE is_active = 1")
            active_users = cursor.fetchone()[0]
            return active_users
        except Error as e:
            print(f"Error fetching active users count: {e}")
            return None
        finally:
            cursor.close()
            connection.close()
