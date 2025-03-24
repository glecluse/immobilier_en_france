import streamlit as st
import re
from src.controllers.auth import auth
from src.controllers.signup import signup
from src.router import redirect
import time

st.title("Le déploiement s'est correctement déroulé !")

def is_password_secure(password):
    if len(password) < 12:
        return "Le mot de passe doit contenir au moins 12 caractères."
    if not re.search(r"[A-Z]", password):
        return "Le mot de passe doit contenir au moins une majuscule."
    if not re.search(r"[a-z]", password):
        return "Le mot de passe doit contenir au moins une minuscule."
    if not re.search(r"\d", password):
        return "Le mot de passe doit contenir au moins un chiffre."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Le mot de passe doit contenir au moins un caractère spécial (?@#$%^&*...)."
    return None 

def load_view():
    col3, _, col4 = st.columns([2, 0.5, 2])

    with col3:
        st.markdown("<h1 style='text-align: center;'>Connexion</h1>", unsafe_allow_html=True)
        email = st.text_input('E-mail', '')
        sign_up_mode = st.checkbox("Créer un compte")

        password = st.text_input('Mot de passe', '', type='password')
        confirm_password = st.text_input('Confirmer le mot de passe', '', type='password') if sign_up_mode else None

        col1, col2 = st.columns([1, 1])

        with col1:
            log_in_button = st.button('Se connecter')
        with col2:
            sign_up_button = st.button("S'inscrire") if sign_up_mode else None

        if log_in_button and not sign_up_mode:
            if auth(email, password):
                st.success("Connexion réussie.")
                redirect("home", reload=True)
            else:
                st.error("Compte incorrect.")

        elif sign_up_button and sign_up_mode:
            if password != confirm_password:
                st.error("Les mots de passe ne correspondent pas.")
            else:
                password_error = is_password_secure(password)
                if password_error:
                    st.error(password_error)
                else:
                    if signup(email, password):
                        st.success("Inscription réussie, vous allez être redirigé vers la page d'accueil de l'application.")
                        time.sleep(3)
                        redirect("home", reload=True)
                    else:
                        st.error("E-mail déjà utilisé ou erreur technique.")

    with col4:
        st.image("login.png", width=400)
