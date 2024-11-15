import streamlit as st
from db_conn import create_connection


st.title("MySQL Database Connection")

if st.button("Connect to Database"):
    connection = create_connection()
    if connection:
        st.success("Connected to MySQL Server successfully!")
        connection.close()
        st.write("Connection closed.")
    else:
        st.error("Failed to connect to the database.")
