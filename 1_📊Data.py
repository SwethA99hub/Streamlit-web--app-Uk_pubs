import streamlit as st
import pandas as pd
import io

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write('Welcome to the Streamlit project!👋🏻 ')




st.title('Search for your nearby Pubs')
st.write('🍷')
st.subheader('Welcome to the UK🇬🇧 pubs 🥃 ')

### background image
from PIL import Image
image = Image.open('image2.jpg')

st.image(image)
####################
## reading data.
st.checkbox('use container width',value = False,key="use_container_width")
df = pd.read_csv(r"/Users/apple/Downloads/open_pubs.csv")
df.drop(['Unnamed: 0'],axis =1,inplace = True)
df1= st.dataframe(df)

st.write('The description of the data is:')
st.dataframe(df.describe())

buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.write('Area/no.of pubs')
st.dataframe(df['local_authority'].value_counts())
st.text("""
## This  Dataset is About available pub location within 5kms radius with respective of the
area. """)

### background image
from PIL import Image
image = Image.open('image1.jpeg')

st.image(image)
