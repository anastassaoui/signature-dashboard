import streamlit as st
from db_conn import get_total_users, get_active_users,fetch_all_tables

st.set_page_config(page_title="Absence Management Dashboard", layout="wide")


tailwind_cdn = """
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
<script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Center the table header and cell content */
        .css-1q8dd3e.e1ewe7hr3 th, .css-1q8dd3e.e1ewe7hr3 td {
            text-align: center !important;
        }
    </style>
"""
st.markdown(tailwind_cdn, unsafe_allow_html=True)
    
st.markdown("""

<h1 class="text-6xl text-center font-extrabold mt-10 md:text-7xl
            cursor-pointer md:text-8xl md:font-extrabold
            mb-10 hover:text-red-400 duration-1000 md:mt-20
            ">
    <i class="fas fas fa-signature header-icon text-7xl md:text-9xl hover:text-red-400 transition duration-1000 ease-in-out transform hover:scale-110"></i>
    Click-Sign 
    <span class="bg-red-100 text-red-600 md:text-7xl mt-10 text-5xl font-extrabold me-2 px-2.5 py-0.5 rounded dark:bg-red-400 dark:text-red-800 ms-2 hover:scale-125">
        Dashboard!
    </span>
</h1>

""", unsafe_allow_html=True)

# Fetch all tables as DataFrames
tables_data = fetch_all_tables()


col1,col2,col3,col4,col5 = st.columns([2,1, 5   ,2,1]) 
with col1:
    st.markdown("""
                            
    <h4 class="text-3xl text-center font-extrabold mt-5 hover:text-red-400 duration-1000 cursor-pointer  md:-mb-12  md:text-3xl  md:mb-2">
        <i class="fas fa-network-wired md:text-2xl header-icon text-3xl hover:text-red-400 transition duration-1000 ease-in-out transform hover:scale-110"></i>
        Total Users
    </h4>
    
    <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:mt-14 md:pt-1
    """, unsafe_allow_html=True)        
    
with col2:
    total_users = get_total_users()
    st.metric(label=" ", value=total_users if total_users is not None else "N/A")
    
with col4:
    st.markdown("""
                            
    <h4 class="text-3xl text-center font-extrabold mt-5 hover:text-red-400 duration-1000 cursor-pointer  md:-mb-12  md:text-3xl  md:mb-2">
        <i class="fas fa-user-check md:text-2xl header-icon text-3xl hover:text-red-400 transition duration-1000 ease-in-out transform hover:scale-110"></i>
        Active Users 
    </h4>
    
    <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:mt-14 md:pt-1
    """, unsafe_allow_html=True) 
    
    
with col5:
    active_users = get_active_users()
    st.metric(label=" ", value=active_users if active_users is not None else "N/A")




























if tables_data:
    table_names = list(tables_data.keys())
    num_tables = len(table_names)
    

    for i in range(0, num_tables, 5):

        col1, col2,col3 = st.columns([12,1, 18])  
        col4,col5,col6,col7 = st.columns([14,6,14,1])  
        

        with col1:
            if i < num_tables:
                
                st.markdown("""
                            
                <h4 class="text-5xl text-center font-extrabold mt-5 hover:text-red-400 duration-1000 cursor-pointer  md:-mb-12 md:mt-20 md:text-6xl  md:mb-2">
                    <i class="fas fa-users header-icon text-7xl hover:text-red-400 transition duration-1000 ease-in-out transform hover:scale-110"></i>
                    Users 
                </h4>
                
                <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:mt-14 md:pt-1">

                """, unsafe_allow_html=True)        
                    
                st.dataframe(tables_data[table_names[i]])
        
        with col3:
            if i + 1 < num_tables:
                st.markdown("""
                            
                <h4 class="text-5xl text-center font-extrabold mt-5 hover:text-red-400 duration-1000 cursor-pointer  md:-mb-12 md:mt-20 md:text-6xl  md:mb-2">
                    <i class="fas fa-folder-open header-icon text-7xl hover:text-red-400 transition duration-1000 ease-in-out transform hover:scale-110"></i>
                    Folders 
                </h4>
                
                <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:mt-14 md:pt-1">

                """, unsafe_allow_html=True)     
                st.dataframe(tables_data[table_names[i + 1]])
        

        with col4:
            if i + 2 < num_tables:
                st.markdown("""
                            
                <h4 class="text-5xl text-center font-extrabold mt-5 hover:text-red-400 duration-1000 cursor-pointer  md:-mb-12 md:mt-10 md:text-6xl  md:mb-2">
                    <i class="fas fa-file-alt header-icon text-7xl hover:text-red-400 transition duration-1000 ease-in-out transform hover:scale-110"></i>
                    folder 
                </h4>
                
                <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:mt-14 md:pt-1">

                """, unsafe_allow_html=True)   
                st.dataframe(tables_data[table_names[i + 2]])
                
            if i + 3 < num_tables:
                st.markdown("""
                            
                <h4 class="text-5xl text-center font-extrabold mt-5 hover:text-red-400 duration-1000 cursor-pointer  md:-mb-12 md:mt-10 md:text-6xl  md:mb-2">
                    <i class="fas fa-check-circle  header-icon text-7xl hover:text-red-400 transition duration-1000 ease-in-out transform hover:scale-110"></i>
                    verification 
                </h4>
                
                <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:mt-14 md:pt-1">

                """, unsafe_allow_html=True)   
                st.dataframe(tables_data[table_names[i + 3]])
                
                
                
        with col6:
            if i + 4 < num_tables:
                st.markdown("""
                            
                <h4 class="text-5xl text-center font-extrabold mt-5 hover:text-red-400 duration-1000 cursor-pointer  md:-mb-12 md:mt-10 md:text-6xl  md:mb-2">
                    <i class="fas fa-shield-alt header-icon text-7xl hover:text-red-400 transition duration-1000 ease-in-out transform hover:scale-110"></i>
                    auth_log 
                </h4>
                
                <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 md:mt-14 md:pt-1">

                """, unsafe_allow_html=True)   
                st.dataframe(tables_data[table_names[i + 4]])
