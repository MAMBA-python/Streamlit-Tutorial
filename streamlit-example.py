#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 00:23:59 2023

@author: izeboud
"""

import streamlit as st
import pandas as pd
import numpy as np
# import geopandas as gpd
# import contextily as ctx
# import altair as alt
# import matplotlib.pyplot as plt
# import leafmap.foliumap as leafmap
# from streamlit_folium import st_folium

# %%

st.markdown("""
            # Bigger header
            ## Anything is possible with Markdown
            ### smaller header
            
            This works exactly the same as your markdown cells in 
            jupyter notebook!
            
            1. some summations
            2. nmbr 2
            
            use the `pandas` package. Got to **love** *markdown*!
            """)
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


# st.video("/home/izeboud/Downloads/WhatsApp Video 2023-01-25 at 16.10.42.mp4")

# %%

# df = pd.read_csv(r'/home/izeboud/Downloads/vb-data-streamlit.csv')
# # df_bruggen.head()

# # GeoDataFrame maken van DataFrame, waarin x en y gedefinieerd en 
# geometry = gpd.points_from_xy(df['Long'], df['Lat'])
# gdf = gpd.GeoDataFrame(df, geometry=geometry, crs=4326)

# # m = leafmap.Map(center=[20, 0], zoom=1)
# # m.add_gdf(gdf_bruggen_popup)
# m = leafmap.Map(center=[20, 0], zoom=3)
# gdf.explore(m=m, marker_type='circle', popup=True, tooltip=False)

# # call to render Folium map in Streamlit
# st_data = st_folium(m, width=725)
