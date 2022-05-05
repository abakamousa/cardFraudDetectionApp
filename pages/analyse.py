#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:53:03 2022

@author: aboubakar
"""
import streamlit as st
import pandas as pd
#import plotly.express as px
import matplotlib.pyplot as plt
import io

import seaborn as sns


#@st.cache(suppress_st_warning=True)
def description(name):
    if (name=="identity train"):
        df_identity         = pd.read_csv('train_identity.csv', nrows=10000)
        st.dataframe(df_identity)
        st.write("\n \n ")
        resume = st.checkbox('Afficher le résumé')
        information = st.checkbox('Afficher les informations sur le dataframe')
        correlation = st.checkbox('Afficher la matrice de corrélation')
        distribution = st.checkbox('Afficher la distribution des données')
        if resume:
             st.write(df_identity.describe())
        if information:
            #st.write(df_identity.info())
            buffer = io.StringIO()
            df_identity.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)
        if correlation:
             fig, ax = plt.subplots(figsize=(15,10))  
             sns.heatmap(df_identity.corr(), ax = ax)
             st.write(fig)
        if distribution:
            df_identity.hist(figsize=(18,9))
            plt.show()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
    elif (name=="identity test"):
        df_test_identity    = pd.read_csv('test_identity.csv', nrows=5000)
        st.dataframe(df_test_identity)
        st.write("\n \n ")        
        resume = st.checkbox('Afficher le résumé')
        information = st.checkbox('Afficher les informations sur le dataframe')
        correlation = st.checkbox('Afficher la matrice de corrélation')
        distribution = st.checkbox('Afficher la distribution des données')
        if resume:
             st.write(df_test_identity.describe())
        if information:
            #st.write(df_identity.info())
            buffer = io.StringIO()
            df_test_identity.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)
        if correlation:
             fig, ax = plt.subplots(figsize=(15,10))  
             sns.heatmap(df_test_identity.corr(), ax = ax)
             st.write(fig)
        if distribution:
            df_test_identity.hist(figsize=(18,9))
            plt.show()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
    elif (name=="transaction train"):
        df_transaction      = pd.read_csv('train_transaction.csv', nrows=10000)
        st.dataframe(df_transaction)
        st.write("\n \n ")        
        resume = st.checkbox('Afficher le résumé')
        information = st.checkbox('Afficher les informations sur le dataframe')
        correlation = st.checkbox('Afficher la matrice de corrélation')
        distribution = st.checkbox('Afficher la distribution des données')
        if resume:
             st.write(df_transaction.describe())
        if information:
            #st.write(df_identity.info())
            buffer = io.StringIO()
            df_transaction.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)
        if correlation:
             fig, ax = plt.subplots(figsize=(15,10))  
             sns.heatmap(df_transaction.corr(), ax = ax)
             st.write(fig)
        if distribution:
            df_transaction.hist(figsize=(18,9))
            plt.show()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
    elif (name=="transaction test"):
        df_test_transaction = pd.read_csv('test_transaction.csv', nrows=5000)#nrows=10000)
        st.dataframe(df_test_transaction)
        st.write("\n \n ")        
        resume = st.checkbox('Afficher le résumé')
        information = st.checkbox('Afficher les informations sur le dataframe')
        correlation = st.checkbox('Afficher la matrice de corrélation')
        distribution = st.checkbox('Afficher la distribution des données')
        if resume:
             st.write(df_test_transaction.describe())
        if information:
            #st.write(df_identity.info())
            buffer = io.StringIO()
            df_test_transaction.info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)
        if correlation:
             fig, ax = plt.subplots(figsize=(15,10))  
             sns.heatmap(df_test_transaction.corr(), ax = ax)
             st.write(fig)
        if distribution:
            df_test_transaction.hist(figsize=(18,9))
            plt.show()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
            
            

        
    
#@st.cache
def app():
    st.title('Analyse exploratoire')
    #st.write('Model training')
    option = st.selectbox(
     'Afficher la description d\'un dataset',
     ('identity train', 'identity test', 'transaction train', 'transaction test'))

    #st.write('You selected:', option)
    description(option)
    

#st.title('Moussa')