#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd
import seaborn as sns
from IPython import get_ipython

data = sns.load_dataset('titanic')
st.header('## Titanic Dataset')
st.dataframe(data)

st.write('Gender count in each town',pd.crosstab(data['sex'], data['embark_town']))

st.info('Some String Test :)')
txt = st.text_area('Converting to UPPER', '''My name is Ganesh. This is my first text in streamlit!!''')
st.write('UPPER CASE: ', txt.upper())


# In[ ]:





# In[ ]:




