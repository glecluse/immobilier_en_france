import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def load_view():

    st.title("Données utilisées pour l'analyse")

    tab3, tab1, tab2 = st.tabs(["Retraitement du fichier initial","Données relatives aux taux d'intêréts", "Données relatives aux transactions"])

    taux_interet = pd.read_csv('data/taux_interet.csv')
    taux_interet['année_mois'] = pd.to_datetime(taux_interet['date']).dt.to_period('M')

    grouped = pd.read_csv("transactions_csv.csv")
    
    
    with tab3:
        st.title("Retraitement du fichier initial")
        # Afficher le contenu du fichier Markdown
        st.write("Le fichier utilisé est sous format .npz (numpy). Ce fichier très volumineux (299 mo) a fait l'objet d'un traitement particulier afin de le transformer en fichier CSV exploitable pour l'analyse. Le but étant de sélectionner les colonnes utiles à notre analyse et de regrouper par dates afin d'en diminuer le volume.")
                
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            with open('traitement_fichier_transaction.ipynb') as f:
                file_contents = f.read()
                st.download_button('Télécharger le fichier .ipynb', file_contents, file_name='traitement_fichier_transaction.ipynb')
        
        with col2:
            st.write("""
            - **Chargement des fichiers** 
            - **Conversion de la colonne date en datetime**
            - **Création de colonnes supplémentaires**
            - **Tri des données**
            - **Sélection des colonnes utiles**
            - **Agrégation des données par date**
            - **Exportation vers CSV**
            """)
        with col3:
            st.image("code.jpg", width=500)
    with tab1:
        st.header("Tableau d'évolution des taux d'intérêts")
        st.write("---")
        col1, col2, col3, col4 = st.columns(4)        
        with col2:
            st.dataframe(taux_interet)
        with col3:
            st.write("Le fichier représente l'évolution des taux d'intêrét au niveau national pour la pèriode allant de décembre 2014 à octobre 2023.", text_align='center')
            st.image("taux.jpg")
    
    with tab2:
        st.header("Données de l'historique des transactions")
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(grouped.head(15))

        with col2:
            st.image("transactions.jpg", width = 600)