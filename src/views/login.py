import streamlit as st
import re  
import sqlite3 
from src.controllers.auth import auth
from src.controllers.signup import signup
from src.router import redirect

def get_db_connection():
    """ Connexion à la base de données SQLite. """
    conn = sqlite3.connect("project.db")  
    return conn

def email_exists(email):
    """ Vérifie si l'email existe déjà dans la base de données. """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def is_password_secure(password):
    """ Vérifie si le mot de passe respecte les critères de sécurité. """
    if len(password) < 12:  
        return "Le mot de passe doit contenir au moins 12 caractères."
    if not re.search(r"[A-Z]", password):
        return "Le mot de passe doit contenir au moins une majuscule."
    if not re.search(r"[a-z]", password):
        return "Le mot de passe doit contenir au moins une minuscule."
    if not re.search(r"\d", password):
        return "Le mot de passe doit contenir au moins un chiffre."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Le mot de passe doit contenir au moins un caractère spécial (!@#$%^&*...)."
    
    return "Mot de passe sécurisé."

def load_view():
    col3, empty_col, col4 = st.columns([2, 0.5, 2])

    with col3:
        st.markdown("<h1 style='text-align: center;'>Connexion</h1>", unsafe_allow_html=True)
        st.write('test')
        email = st.text_input('E-mail', '')

        # Ajout d'une case à cocher pour différencier connexion et inscription
        sign_up_mode = st.checkbox("Créer un compte")

        if sign_up_mode:
            password = st.text_input('Mot de passe', '', type='password')
            confirm_password = st.text_input('Confirmer le mot de passe', '', type='password')
        else:
            password = st.text_input('Mot de passe', '', type='password')
            confirm_password = None

        col1, col2 = st.columns([1, 1], gap="small")
        with col1:
            log_in_button = st.button('Se connecter')
        with col2:
            sign_up_button = st.button("S'inscrire") if sign_up_mode else None

        # Gestion de la connexion
        if log_in_button and not sign_up_mode:
            res = auth(email, password)
            if not res:
                st.error("Compte incorrect")
            else:
                st.success("Connexion en cours")
                redirect("home", reload=True)

        # Gestion de l'inscription avec confirmation du mot de passe, sécurité et vérification email
        elif sign_up_button and sign_up_mode:
            if email_exists(email):
                st.error("E-mail déjà utilisé. Veuillez vous connecter.")
            elif password != confirm_password:
                st.error("Les mots de passe ne correspondent pas. Veuillez réessayer.")
            else:
                # Vérification de la sécurité du mot de passe
                password_error = is_password_secure(password)
                if password_error:
                    st.error(password_error)
                else:
                    res = signup(email, password)
                    if not res:
                        st.error("Une erreur est survenue lors de l'inscription. Veuillez réessayer.")
                    else:
                        st.success("Inscription réussie. Redirection en cours...")
                        redirect("home", reload=True)

    with col4:
        st.image("login.png", width=400)
