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
        with open('traitement_fichier_transaction.ipynb') as f:
            file_contents = f.read()
            st.download_button('Télécharger le fichier .ipynb', file_contents, file_name='traitement_fichier_transaction.ipynb')
        with open("traitement_fichier_transaction.md", "r") as markdown_file:
            markdown_content = markdown_file.read()
        st.markdown(markdown_content)

    with tab1:
        st.header("Tableau d'évolution des taux d'intérêts")
        st.write("---")
        col1, col2, col3 = st.columns(3)        
        with col1:
            st.dataframe(taux_interet)
        with col2:
            st.write("Le fichier représente l'évolution des taux d'intêrét au niveau national pour la pèriode allant de décembre 2014 à octobre 2023.", text_align='center')
    
    with tab2:
        st.header("Données de l'historique des transactions")
        st.dataframe(grouped.head(15))