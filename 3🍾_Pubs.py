import streamlit as st
import pandas as pd
import numpy as np
df= pd.read_csv(r"/Users/apple/Downloads/open_pubs.csv")

x = df[['latitude','longitude']]

st.header('Find the Nearest pub in your area.')

lat = st.number_input('Enter latitude')
long = st.number_input('Enter longitude')
submit = st.button(label = 'submit')
y =  np.array([lat,long])


### using euclidient distance to measure distance.

dist = np.sqrt(np.sum((y-x)**2,axis = 1))


k = 5
sort = np.argpartition(dist,k-1)[:k]
if submit:
    st.map(df.iloc[sort])