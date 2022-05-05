#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:19:57 2022

@author: aboubakar
"""

import streamlit as st
import numpy as np
from PIL import  Image




def app():
    #st.title("PyFraud_Detection")
    st.header("Application pour la détection des fraudes bancaire")
    st.write("\n\n")  
    #img = Image.open("images/ieee.png")
    #st.image(img, width = 200, caption = "")
    st.write(
            "Dans le cadre de ce projet, il sera question de mettre en place un modèle prédictif permettant de détecter de façon précise  des fraudes lié aux opérations de paiement par carte bancaire. Pour cela, nous allons utiliser les données fournies par Vesta Corporation, une société leader dans le domaine des solutions de paiement de commerce électronique garanties. Le principal objectif à atteindre est de pouvoir prédire si oui ou non une transaction est frauduleuse, tout en s’assurant d’éviter les faux positifs et les faux négatifs. Ceci afin de permettre une amélioration du process de détection des fraudes bancaire."
            "\n \n"
            "Pour cela, nous allons suivre les étapes suivantes:"
            "\n \n"
            "* L'exploration et nettoyage des données : à cette étape, il s’agira pour nous d’analyser les données (Identification des valeurs manquantes, vision d’ensemble sur les données, etc) et de proposer des visualisations commentées et analysées."
            "\n"
            " * La construction du modèle : à cette étape, il s’agira pour nous d’identifier le modèle de machine learning le plus adapté pour la résolution de notre problème. Ensuite, nous procéderons à l’entrainement et optimisation des paramètres de notre modèle."
            "\n"
            "* Evaluation des performances : à cette étape, il s’agira pour nous d’évaluer les performances de notre modèle et produire une analyse de ces résultats."
            "\n"
            "* Préparation de la démonstration"

            )