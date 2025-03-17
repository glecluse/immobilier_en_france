import streamlit as st
from urllib.parse import unquote
import time
import streamlit.components.v1 as components

def get_route():
    url = st.query_params.get("nav")
    url = url[0] if isinstance(url, list) else url
    route = unquote(url) if url is not None else url
    return route

def redirect(new_route, reload=False):
    if new_route[0] != "/":
        new_route = "/" + new_route
    st.query_params.update(nav=new_route)
    time.sleep(0.1) 
    if reload:
        st.rerun()
