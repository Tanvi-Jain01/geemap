import geemap as geemap
import streamlit as st
import ee

# Create the map
Map = geemap.Map()

# Define the available layer options
layer_options = ['NLCD 2016 CONUS Land Cover', 'NLCD 2001 CONUS Land Cover']

# Create dropdown widgets for layer selection
left_layer_dropdown = st.selectbox('Left Layer:', layer_options)
right_layer_dropdown = st.selectbox('Right Layer:', layer_options)

# Define the split_map function
def split_map(left_layer, right_layer):
    Map.split_map(left_layer=left_layer, right_layer=right_layer)

# Check if both layers are selected
if left_layer_dropdown and right_layer_dropdown:
    # Use the split_map function to update the map
    split_map(left_layer_dropdown, right_layer_dropdown)

# Display the map
Map.to_streamlit()

