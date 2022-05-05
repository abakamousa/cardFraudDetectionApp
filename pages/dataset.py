#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:38:36 2022

@author: aboubakar
"""

import streamlit as st
import numpy as np
import pandas as pd


def app():
    st.title('DATASET')
    st.header('A propos du jeu de données')
    
    
    url = "https://www.kaggle.com/c/ieee-fraud-detection/data"
    st.write("Lien de téléchargement du dataset: [link](%s)" % url)
    st.write("Les données que nous allons utiliser dans ce projet sont divisées en deux ﬁchiers identité qui incluent les informations des utilisateurs et transaction contenant les variables de la transaction. Ces fichiers sont joints par TransactionID. "
            "\n"
            "Les transactions n’ont pas d’informations d’identité correspondantes. La cible est isFraud qui est codée à 1 si cette transaction est frauduleuse et 0 sinon."

             )
    st.header('Aperçu de la table sample')
    st.write("La table sample contient les ID de Transaction et un champ is Fraud. Cette table ne contient pas d'informations intéressantes à exploiter , le champ 'is Fraud' étant alimenté exclusivement de la donnée 0.5. Il est donc inexploitable dans notre projet et ne peut donc être utilisé")
    sample = pd.read_csv('sample_submission.csv')
    st.dataframe(sample)
     
   
    st.header('Aperçu de la table transaction train') 
    st.write("La table transaction train contient 590 540 lignes et 394 colonnes. Cette table est plus intéressante que celle du test, car elle contient l'information sur la fraude constatée. Nous allons donc baser notre projet sur les fichiers train , qui sont plus complets que les fichiers tests.")
    
    df_transaction      = pd.read_csv('train_transaction.csv', nrows=10000)
    st.dataframe(df_transaction)
    
    st.header('Aperçu de la table transaction test')
    st.write("La table test_transaction contient 506 691 lignes et 392 colonnes. Cette table contient des champs intéressants comme les id de transactions et les montants de transactions, mais il n'y a pas d'information sur une éventuelle fraude. Les 2 datas de tests ont été splités auparavant de l'ensembles des données en prenant en compte la variable cible 'is Fraud', nous ne pouvons donc pas les utiliser dans notre projet ")
    
    df_test_transaction = pd.read_csv('test_transaction.csv', nrows=5000)#nrows=10000)
    st.dataframe(df_test_transaction)
    
    st.header('Aperçu de la table train identity')
    df_identity         = pd.read_csv('train_identity.csv', nrows=10000)#nrows=50000
    st.write("La table test_identity contenant 141 907 lignes et 40 colonnes. Cette fichier contient des champs nommés de id-01 à id-38, sans explication sur leur signification , et contenant énormémement de données NaN ")
    st.dataframe(df_identity)
    
    

    st.header('Aperçu de la table test identity')
    df_test_identity    = pd.read_csv('test_identity.csv', nrows=5000)#nrows=10000)
    st.write("Cette table contient 144 233 lignes et 41 colonnes.  Elle contient des champs nommée de id-01 à 1d-38, sans explication sur leur signification, ayant des données NaN, et de type objet ou float 64 (données booléenne ou données numériques) ")
    st.dataframe(df_test_identity)
    
    
    
    
    
    
    