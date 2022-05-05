#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:09:24 2022

@author: aboubakar
"""

"""
This file is the framework for generating multiple Streamlit applications 
through an object oriented framework. 
"""

# Import necessary libraries 
import streamlit as st

# Define the multipage class to manage the multiple apps in our program 
class MultiPage: 
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages = []
    
    def add_page(self, title, func) -> None: 
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps 
            
            func: Python function to render this page in Streamlit
        """

        self.pages.append(
            {
                "title": title, 
                "function": func
            }
        )
        
    def run(self):
        # Drodown to select the page to run  
        page = st.sidebar.selectbox(
            'Menu', 
            self.pages, 
            format_func=lambda page: page['title']
        )
        st.sidebar.info(
        "Projet DS - AOUT 2021"
        "\n\n"
        "Participants:"
        "\n\n"
        "ABOUBAKAR Moussa (https://www.linkedin.com/in/aboubakar-moussa/)"
        "\n\n"
        "Sivanesan BAGAVANDADAS \n(https://www.linkedin.com/in/sivanesanbagavandadas/) "
        )

        # run the app function 
        page['function']()