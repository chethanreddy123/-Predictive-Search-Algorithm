import pandas as pd

df = pd.DataFrame({'Hospital': ['Nick hospital', 'Nick hospital', 'Nick hospital',
                                'Krish hospital', 'Krish hospital', 'Krish hospital'],
                   'document_source': ['NAR', 'PAR', 'Free Text', 'NAR', 'PAR', 'Free Text'],
                   'document_count': [1200, 150, 3, 2500, 342, 300]})
df.head()

import streamlit as st
#create sidebar
st.sidebar.title("Filter data")

temp = df.to_dict('list')
temp['Hospital'] = list(set(temp['Hospital']))
temp['document_source'] = list(set(temp['document_source']))
temp_records = df.to_dict('records')

#Checkbox for Hospitals
hosp_list = st.sidebar.selectbox("Select Hospital", temp['Hospital'])


#Chech box for Documents
doc_source = st.sidebar.selectbox("Select Document source", temp['document_source'])

st.subheader('Document Count')

