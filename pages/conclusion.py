#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:53:01 2022

@author: aboubakar
"""
import streamlit as st




def app():
    st.title('Conclusion et perspectives')
    st.subheader("Bilan")
    st.write("Le projet est une mise en pratique concrète et continue des acquis de connaissances dispensées par la formation. Il a de plus permis de découvrir d’autres aspects et techniques permettant de travailler un cas pratique de data science, non enseignés dans la formation."
             "\n \n"
             "L’objectif principal du projet était de proposer un modèle d’apprentissage permettant de détection de façon précise une anomalie dans le cadre des transactions bancaires. Pour cela, nous avons utilisé un dataset provenant de kaggle, puis nous avons procédé à la phase de préprocessing avec notamment : l’exploration, l’analyse et le nettoyage du dataset. Nous avons ensuite réalisé un benchmark de différend modèles de Machine Learning. Ceci aussi bien pour les modèles de types supervisés que non supervisés.  "
             )
    st.subheader("Piste d'amélioration")
    st.write("Pour améliorer les performances du modèle, il serait intéressant d’expérimenter une nouvelle stratégie de rééchantillonnage des données.")