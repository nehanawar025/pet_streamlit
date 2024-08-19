import streamlit as st

# Initialize connection using the details from the secrets.toml
conn = st.connection('mysql', type='sql', 
                     host=st.secrets["connections"]["mysql"]["host"], 
                     port=st.secrets["connections"]["mysql"]["port"],
                     database=st.secrets["connections"]["mysql"]["database"],
                     username=st.secrets["connections"]["mysql"]["username"], 
                     password=st.secrets["connections"]["mysql"]["password"])

# Perform query
df = conn.query('SELECT * from pet_info;', ttl=600)

# Print results
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
