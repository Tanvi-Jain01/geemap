# import geemap
# import ee
# import streamlit as st

# Map=geemap.Map()
# Map


# import ipywidgets as widgets

# # Create the map
# Map = geemap.Map()

# # Define the available layer options
# layer_options = ['NLCD 2016 CONUS Land Cover', 'NLCD 2001 CONUS Land Cover']

# # Create dropdown widgets for layer selection
# left_layer_dropdown = widgets.Dropdown(options=layer_options, description='Left Layer:')
# right_layer_dropdown = widgets.Dropdown(options=layer_options, description='Right Layer:')

# # Define the split_map function
# def split_map(left_layer, right_layer):
#     Map.split_map(left_layer=left_layer, right_layer=right_layer)

# # Use the interact function to update the split map based on the selected layers
# widgets.interact(split_map, left_layer=left_layer_dropdown, right_layer=right_layer_dropdown)

# # Display the map
# Map
import geemap
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

