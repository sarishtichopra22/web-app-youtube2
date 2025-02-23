# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:01:42 2025

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Title
st.title("Data Analysis")
st.subheader("Data Analysis using Python and Streamlit ")

#upload dataset
upload=st.file_uploader("Upload your datset (In csv format")

if upload is not None:
    data=pd.read_csv(upload)
    
#show dataset
if upload is not None:
    if st.checkbox("Preview dataset"):
        if st.button("head"):
            st.write(data.head())
        if st.checkbox("Preview Tail"):
            st.write(data.tail())

#check datatype of each column 
if upload is not None:
    if st.checkbox ("Data Type of each column"):
        st.text("Data Types")
        st.write(data.dtypes)
        
#shape of our dataset
if upload is not None:
   data_shape=st.radio("What dimension you want to check?",('Rows','Columns'))
   
   if data_shape=='Rows':
       st.text("No of Rows")
       st.write(data.shape[0])
       
   if data_shape=='Columns':
       st.text("No of Rows")
       st.write(data.shape[1])
       
#check for null values
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Check for Null Values in the Dataset"):
            fig=sns.heatmap(data.isnull())
            st.pyplot()
            
    else:
            st.success("Congratulations!! No missing values")
        
#duplicate
if upload is not None:
    test=data.duplicated().any()
    st.warning("Data  has duplicated values")
    dup=st.selectbox("Do you want to remove duplicates",\
                     ("Select One","Yes","Nos"))
    if dup=="Yes":
        data=data.drop_duplicates()
        st.text("Duplicates are removed")
        
    if dup=="No":
        st.text("No problem")
        
        
if upload is not None:
    if st.checkbox("Sumarry of Dataset"):
        st.write(data.describe())
        
        
# About
if st.button("About App"):
    st.text("Built with Streamlit")
if st.checkbox("By"):
    st.success("By Sarishti")
        
        
            
            
 

       
       