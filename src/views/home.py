import streamlit as st
from src.router import redirect

def load_view():

    st.title("Présentation de l'Application d'Analyse du Marché Immobilier en France")

    # Créer un tableau à trois colonnes
    col1, col2, col3 = st.columns([3, 5, 1])  # La colonne du milieu est plus large pour l'image

    # Placer l'image au centre dans la colonne du milieu
    with col2:
        st.image("house.jpg", width=500)  # Ajustez 'width' pour réduire la taille de l'image

    st.write("""
    ### Objectif de l'Application
    Le principal objectif de cette application est de mettre en évidence les incohérences de marché entre le prix de l'immobilier et les taux d'intérêt. En explorant les données, vous pourrez identifier des tendances, des anomalies et potentiellement des opportunités sur le marché immobilier français.

    ### Sources des Données
    - **Transactions immobilières :** Les données proviennent de la base "Demande de Valeurs Foncières" (DVF), qui recense les transactions immobilières en France.
    - **Taux d'intérêt :** Les données des taux d'intérêt sont fournies par la Banque de France.

    ### Visualisations Disponibles
    L'application propose trois graphiques principaux, chacun permettant de sélectionner la région de votre choix pour une analyse plus précise :

    1. **Nombre de Transactions et Taux d'Intérêt Moyen par Mois :**
    - Ce graphique montre le nombre de transactions immobilières et le taux d'intérêt moyen mensuel. 
    - Il permet d'observer comment les variations des taux d'intérêt peuvent affecter le volume des transactions.

    2. **Nombre de Transactions et Montant Moyen des Transactions par Mois :**
    - Ce graphique affiche le nombre de transactions et le montant moyen des transactions chaque mois.
    - Vous pouvez explorer les fluctuations des prix des biens immobiliers en relation avec le volume des transactions.

    3. **Montant Moyen des Transactions et Taux d'Intérêt Moyen par Mois :**
    - Ce graphique met en relation le montant moyen des transactions immobilières avec le taux d'intérêt moyen.
    - Il permet de visualiser les éventuelles corrélations entre les prix des transactions et les taux d'intérêt.

    ### Technologies Utilisées
    - **Streamlit :** L'application a été créée avec Streamlit, une bibliothèque Python permettant de créer des applications web interactives pour les analyses de données.
    - **Pandas :** Les données sont manipulées et analysées à l'aide de Pandas, une bibliothèque Python puissante pour la manipulation des données.
    - **Matplotlib :** Les visualisations graphiques sont générées avec Matplotlib, une bibliothèque Python dédiée à la création de graphiques.

    ### Utilisation de l'Application
    L'interface utilisateur est conçue pour être simple et intuitive. Vous pouvez sélectionner la région de votre choix à l'aide des menus déroulants et observer instantanément les changements dans les graphiques. Chaque graphique offre des perspectives uniques sur le marché immobilier, permettant une analyse approfondie des tendances et des anomalies.

    ### Limites et Avertissements
    Les données présentées sont basées sur les transactions enregistrées et les taux publiés par les sources mentionnées. Les utilisateurs doivent garder à l'esprit que d'autres facteurs non représentés dans ces visualisations peuvent également influencer le marché immobilier. Les analyses fournies par cette application doivent être complétées par des recherches supplémentaires pour une prise de décision éclairée.

    Nous espérons que cette application vous sera utile pour mieux comprendre le marché immobilier en France et pour identifier des tendances et des incohérences importantes. N'hésitez pas à explorer les différentes régions et à tirer vos propres conclusions à partir des données présentées.

    Bonnes analyses !
    """)

