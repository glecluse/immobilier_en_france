import streamlit as st

def load_view():
    st.title("Conclusion de l'analyse du marché immobilier en France")

    # Créer des colonnes : texte à gauche et image à droite
    col1, col2 = st.columns([2, 1])  # La colonne de gauche est plus large pour le texte

    # Texte à gauche
    with col1:
        st.markdown("""
        Les graphiques interactifs de cette application ont permis de visualiser des tendances et des corrélations importantes entre les transactions immobilières et les taux d'intérêt en France de 2015 à 2023. Voici les principales conclusions tirées de ces analyses :

        #### Corrélation entre le nombre de transactions et les taux d'intérêt
        Sur toute la période analysée, il existe une corrélation notable entre le nombre de transactions immobilières et les taux d'intérêt. Cela indique que les fluctuations des taux d'intérêt ont un impact significatif sur le volume des transactions immobilières. Une baisse des taux d'intérêt tend à stimuler le marché, augmentant le nombre de transactions, tandis qu'une hausse des taux d'intérêt semble freiner l'activité transactionnelle.

        #### Corrélation entre le nombre de transactions et le montant moyen des transactions
        Les données montrent une corrélation entre le nombre de transactions et le montant moyen des transactions jusqu'à la fin de l'année 2022. Cela suggère qu'une augmentation du volume des transactions est généralement associée à une augmentation des prix des transactions immobilières. Cependant, à partir de 2023, cette corrélation s'est rompue, indiquant une décorrélation entre ces deux variables jusqu'en 2024. Cette rupture pourrait être due à divers facteurs économiques ou réglementaires, nécessitant une analyse plus approfondie pour identifier les causes sous-jacentes.

        #### Corrélation entre les taux d'intérêt et le montant moyen des transactions
        De manière similaire, une corrélation est observée entre les taux d'intérêt et le montant moyen des transactions jusqu'à la fin de l'année 2022. Les taux d'intérêt plus bas sont souvent associés à des montants de transaction plus élevés, ce qui peut être attribué à un pouvoir d'achat accru des emprunteurs. Cependant, cette relation a également montré une décorrélation à partir de 2023, suggérant que d'autres facteurs ont commencé à influencer les prix des transactions indépendamment des taux d'intérêt.

        #### Implications et recommandations
        Les résultats de cette analyse soulignent l'importance des taux d'intérêt comme facteur clé influençant le marché immobilier en France. La corrélation persistante entre les taux d'intérêt et le nombre de transactions suggère que les décideurs politiques et les investisseurs doivent surveiller attentivement les politiques monétaires et les conditions de prêt.

        La rupture des corrélations observées à partir de 2023 entre le nombre de transactions et le montant moyen des transactions, ainsi qu'entre les taux d'intérêt et le montant moyen des transactions, indique des changements dans le marché qui méritent une attention particulière. Ces changements pourraient être dus à des facteurs macroéconomiques, des modifications de la réglementation immobilière, ou des variations dans l'offre et la demande de logements.

        Pour les utilisateurs de cette application, il est recommandé de continuer à surveiller ces tendances et d'approfondir l'analyse pour comprendre les dynamiques sous-jacentes qui influencent le marché immobilier français. En utilisant cette application, vous disposez d'un outil puissant pour explorer les données et prendre des décisions informées.

        Nous espérons que cette application vous a fourni des insights précieux sur le marché immobilier et vous encourageons à continuer vos explorations et analyses.

        Bonnes analyses et merci de votre utilisation de notre application !
        """)

    # Image à droite
    with col2:
        st.image("maison.png", caption="Marché immobilier en France", use_column_width=True)

