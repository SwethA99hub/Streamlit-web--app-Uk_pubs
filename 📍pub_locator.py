from optparse import Option
import streamlit as st
import pandas as pd

df= pd.read_csv(r"/Users/apple/Downloads/open_pubs.csv")

st.title(' Search with postcode or local_authority')

Option = st.selectbox('Area_name / postcodes',['local_authority','postcode'])

if True:
    if Option == 'local_authority':
        form = st.form(key = 'my_form')
        input = form.text_input('Enter Area_name/postcode')
        submit = form.form_submit_button(label = 'submit')
        lat=df.loc[df['local_authority']== input,'latitude']
        long=df.loc[df['local_authority']== input,'longitude']
        rdf= pd.DataFrame((lat,long)).T
        st.map(rdf)
    elif Option == 'postcode':
        form = st.form(key ='my_form')
        input = form.text_input('Enter Area_name/postcode')
        submit = form.form_submit_button(label = 'submit')
        lat=df.loc[df['postcode']== input,'latitude']
        long=df.loc[df['postcode']== input,'longitude']
        rdf= pd.DataFrame((lat,long)).T
        st.map(rdf)


