#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 00:23:59 2023

@author: izeboud
"""

import streamlit as st
import pandas as pd
import numpy as np

# %%

### DATAFRAMES PLOTTEN
# Test data
df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])

col1, col2 = st.columns(2) 

def display_graph():
    with col2:
        if option == 'bar chart':
            st.bar_chart(df)
        elif option == 'area chart':
            st.area_chart(df)
        elif option == 'no chart':
            st.write('no chart!')

with col1:
    st.markdown("""
                # Different charts
                ## Choose your favourite chart
                """)
    
    
    option = st.selectbox("choose your chart", ["bar chart", "area chart", "no chart"])
    submit_button = st.button(label='Submit', on_click=display_graph)

st.write('hallo')
