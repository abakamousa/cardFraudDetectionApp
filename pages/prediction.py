#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:53:01 2022

@author: aboubakar
"""
import streamlit as st
import pandas as pd
from joblib import load
import joblib


def predict(data):
    test_data = pd.read_csv("test_data.csv")
    test_data = test_data.iloc[:10, :880]
    filename = 'finalized_model.sav'
    loaded_model = joblib.load(filename)
    if (data=="fichier 1"):
        st.write(loaded_model.predict(test_data))
        st.info('Note: La classe 0 correspond à une transaction frauduleuse Fraud et la classe 1 correspond à une transaction Normale')
    if (data=="fichier 2"):
        st.write(loaded_model.predict(test_data))
        st.info('Note: La classe 0 correspond à une transaction frauduleuse Fraud et la classe 1 correspond à une transaction Normale')

def app():
    st.title('Prédiction (démo)')
    st.write('\n \n')
    option = st.selectbox(
     'Sélectionner les données de prédiction',
     ('fichier 1', 'fichier 2'))
    if st.button('Lancer la prédiction'):
     st.write('Prédiction en utilisant le modèle StackingClassifier')
     predict(option)
    
    
    
    #pred = loaded_model.predict(test)