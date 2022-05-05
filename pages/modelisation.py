#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:53:01 2022

@author: aboubakar
"""
import streamlit as st
from PIL import  Image




def app():
    st.title('Modélisation') 
    st.write("Nous avons utiliser un apprentissage de type ensembliste pour obtenir de meilleures prédictions. \n"
             "Plus précisément, nous avons utiliser la méthode de stacking,  qui consiste à appliquer un algorithme de machine learning à des classifieur générés par un autre algorithme de machine learning"
             "\n"
             "Dans notre cas, nous avons considéré les modèles suivants: Linear regression, Random forest et le SVC."
             "\n \n"
             "La figure ci-après présente les différentes étapes ayant permis la construction de notre modèle."
             )
    display = Image.open('images/architecture.png')
    col1, col2 = st.beta_columns(2)    
    col1.image(display, width = 600)