import streamlit as st, pathlib
st.set_page_config(page_title="Snow Cover Dashboard", layout="wide")
st.title("Snow Cover Area (km²)")
html = pathlib.Path("index.html").read_text(encoding="utf-8")   # your HTML in repo root
st.components.v1.html(html, height=6000, scrolling=True)       # tall so everything shows
