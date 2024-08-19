# import streamlit as st
# import mysql.connector

# # Initialize connection using mysql-connector-python
# conn = mysql.connector.connect(
#     host=st.secrets["connections"]["mysql"]["host"],
#     username=st.secrets["connections"]["mysql"]["username"],
#     password=st.secrets["connections"]["mysql"]["password"],
#     database=st.secrets["connections"]["mysql"]["database"],
#     port=st.secrets["connections"]["mysql"]["port"]
# )

# # Perform query
# cursor = conn.cursor()
# cursor.execute('SELECT * from pet_info;')
# rows = cursor.fetchall()

# # Print results
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")


import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from pet_info;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")


