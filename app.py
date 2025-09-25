import streamlit as st
st.set_page_config(page_title="Snow Cover Dashboard", layout="wide")
st.title("Snow Cover Area (km²)")
st.components.v1.iframe("https://bilavel14.github.io/SnowCoverArea/", height=1300)
