#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:53:01 2022

@author: aboubakar
"""
import streamlit as st





def app():
    st.title('Methodologie') 
    st.subheader("Classification du problème")
    st.write("Notre projet s’apparente à un problème de type classification car la variable cible contient des valeurs discrètes. En outre, il est à noter que ce projet correspond à une tâche de détection d’anomalie. " )
    st.subheader("Exploitation des données")
    st.write("Pour exploiter les données mis à notre disposition, nous avons effectués les étapes suivantes de preprocessing:"
             "\n \n"
             "* L'imputation des valeurs manquantes"
             "\n \n"
             "* La jointure des différentes tables"
             "\n \n"
             "* L'encodage des valeurs catégorielles"
             "\n \n"
             "* Le réechantillonnage du dataset"
             "\n \n"
             "* La normalisation avec RobustScaler"
             )
    st.subheader("Evaluation des performances")                  
    st.write("Pour évaluer notre modèle, nous avons considérés les métriques suivantes : l’accuracy, le F1-score, la precision et le recall. "
             "\n \n"
             "* L’accuracy est une métrique utilisée pour évaluer les performances d’un modèle de classification. Elle permet de connaître la proportion de bonnes prédictions par rapport à toutes les prédictions."
             "\n \n"
             "* Le F1-score est une métrique de classification qui mesure la capacité d’un modèle à bien prédire les individus positifs, tant en termes de precision (taux de prédictions positives correctes) qu’en termes de recall (taux de positifs correctement prédits). Il correspond en effet à la moyenne harmonique de ces indicateurs, qui doivent tous deux être élevés pour que le F1-score le soit aussi. Le F1-score est particulièrement utilisé pour les problèmes utilisant des données déséquilibrées comme la détection de fraudes ou la prédiction d’incidents graves."
             "\n \n"
             "* La précision correspond au nombre d’éléments correctement attribués à la classe i par rapport au nombre total d’éléments prédits comme appartenant à la classe i (total predicted positive)"
             "\n \n"
             "* Le recall ou rappel correspond au nombre d’éléments correctement attribués à la classe i par rapport au nombre total d’éléments appartenant à la classe i (total true positive)."
             )
    