import copy
import json

import streamlit as st
# from streamlit_image_select import image_select

# from utils import (
#     st_get_osm_geometries,
#     st_plot_all,
#     get_colors_from_style,
#     gdf_to_bytesio_geojson,
# )
# from prettymapp.geo import GeoCodingError, get_aoi
# from prettymapp.settings import STYLES

st.set_page_config(
    page_title="prettymapp", page_icon="🖼️", initial_sidebar_state="collapsed"
)
st.markdown("# Prettymapp")



st.markdown("---")
st.write(
    "Share on social media with the hashtag [#prettymaps](https://twitter.com/search?q=%23prettymaps&src=typed_query) !"
)
st.markdown(
    "More infos and :star: at [github.com/chrieke/prettymapp](https://github.com/chrieke/prettymapp)"
)


