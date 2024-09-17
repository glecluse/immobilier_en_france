import streamlit as st
from src.controllers.auth import auth
from src.controllers.signup import signup

from src.router import redirect


def load_view():
    
    col3, empty_col, col4 = st.columns([2, 0.5, 2])

    with col3:
        st.markdown("<h1 style='text-align: center;'>Connexion</h1>", unsafe_allow_html=True)

        email = st.text_input('E-mail', '')
        password = st.text_input('Mot de passe', '', type='password')
        col1, col2 = st.columns([1, 1], gap="small")
        with col1:
            log_in_button = st.button('Se connecter')
        with col2:
            sign_up_button = st.button("S'inscrire")

        if log_in_button:
            res = auth(email, password)
            if not res:
                st.text("Compte incorrect")
            else:
                st.text("Connexion en cours")
                redirect("home", reload=True)

        elif sign_up_button:
            res = signup(email, password)
            if not res:
                st.text("E-mail déjà utilisé. Veuillez vous connecter.")
            else:
                st.text("Inscription en cours...")
                redirect("home", reload=True)

    with col4:
        st.image("login.png", width=400)

