#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 00:23:59 2023

@author: izeboud
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%

st.markdown("""
            # Example Streamlit
            ## Because we can. 
            
            This works exactly the same as your markdown cells in 
            jupyter notebook! You can write any pretty text here.
            
            1. `different` ways of highlighting text
            2. like **bold** and *italic*
            """)

### DATAFRAMES PLOTTEN
# Test data
df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])

st.markdown(
    """
    # Show your dataframe
    """
    )

st.markdown("## Area Chart")
st.area_chart(df)

st.markdown("## Any matplotlib Figure")
fig, ax = plt.subplots(1)
df.plot(ax=ax)
st.plotly_chart(fig)

st.markdown("## Streamlit Bar Chart")
st.bar_chart(df)
