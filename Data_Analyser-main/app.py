import streamlit as st
import Home
import Visualization
import Dashboard


st.set_page_config(layout="wide")
s = st.button("Home")
PAGES = {
    "Home": Home,
    "Visualizer": Visualization,
    "Dashboard": Dashboard,

}
image = Image.open('auto-ra-banner.png')
st.image(image)
if s == True:
    selection = st.selectbox("Choose one", list(PAGES.keys()), key ='2')
    Home.app()
else:
    selection = st.selectbox("Choose one", list(PAGES.keys()), key ='3')
    page = PAGES[selection]
    page.app()
