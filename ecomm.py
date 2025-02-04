import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

def main():
    st.title('This is app for ecomm I am creating')
    st.sidebar.title('you can upload your file here')
    
    upload_file= st.sidebar.file_uploader('upload your file', tye=['csv','xlsx'])
    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
                data= pd.read_csv(upload_file)
            else:
                data= pd.read_excel(upload_file)
            st.sidebar.success('file uploaded successfully')

            st.subheader('i am going to show you a data details')
            st.dataframe(data.head())
        except Exception as e:
            print(e)




if __name__== '__main__':
    main()

