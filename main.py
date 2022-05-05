#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:08:04 2022

@author: aboubakar
"""


import os
import streamlit as st
from PIL import  Image


# Custom imports 
from multipages import MultiPage
from pages import presentation, dataset, methodologie, modelisation, analyse, prediction, conclusion # import your pages here

import warnings
warnings.filterwarnings("ignore")

# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('images/ieee.png')
#display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
col1, col2 = st.beta_columns(2)
col1.image(display, width = 200)
col2.title("PyFraud_Detection")


# Add all your application here
app.add_page("Présentation du projet", presentation.app)
app.add_page("Le dataset", dataset.app)
app.add_page("Analyse exploratoire", analyse.app)
app.add_page("Méthodologie", methodologie.app)
app.add_page("Modélisation", modelisation.app)
app.add_page("Prédiction", prediction.app)
app.add_page("Conclusion et perspective", conclusion.app)

# The main app
app.run()


