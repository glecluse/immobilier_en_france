import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go

def load_view():

    plt.style.use('dark_background')
    
    taux_interet = pd.read_csv('data/taux_interet.csv')
    taux_interet['année_mois'] = pd.to_datetime(taux_interet['date']).dt.to_period('M')

        
    grouped = pd.read_csv("transactions_csv.csv")
    regions = grouped['Région'].unique().tolist() 
    regions.sort()  
    regions.insert(0, "Toutes les régions") 
    selected_region = st.sidebar.selectbox('Sélectionner une région', regions)    

    st.header('Visualisations')
    st.subheader(f'Région sélectionnée : {selected_region}')
        
    transactions_region_selected = grouped.loc[grouped['Région'] == selected_region]

    # 1 Nombre de Transactions et Taux d\'Intérêt Moyen par Mois
    st.header('Nombre de Transactions et Taux d\'Intérêt Moyen par Mois')
    st.write('---')

    if selected_region != "Toutes les régions":
        grouped = grouped.loc[grouped['Région'] == selected_region]
    else:
        grouped = grouped

    grouped['date_transaction'] = pd.to_datetime(grouped['date_transaction'])

    
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    grouped['date_transaction'] = pd.to_datetime(grouped['date_transaction'], format='%Y-%m')
    x = grouped.groupby(grouped['date_transaction'])['nombre_transactions'].sum()
    couleur = 'tab:blue'
    ax1.set_xlabel('Année')
    ax1.set_ylabel('Nombre de transactions', color=couleur)
    ax1.plot(x.index, x.values, color=couleur)
    ax1.tick_params(axis='y', labelcolor=couleur)
    ax2 = ax1.twinx()
    couleur = 'tab:red'
    ax2.set_ylabel('Taux d\'intérêt moyen', color=couleur)
    ax2.plot(grouped['date_transaction'], grouped['taux_moyen'], color=couleur)
    ax2.tick_params(axis='y', labelcolor=couleur)
    plt.title('Nombre de Transactions et Taux d\'Intérêt Moyen par Année')
    fig.tight_layout()
    plt.grid()
    plt.title('Nombre de Transactions et Taux d\'Intérêt Moyen par Mois')
    st.pyplot(fig)
    

    # 2 - Nombre de Transactions et prix moyen au m²
    st.header('Nombre de Transactions et prix moyen au m²')
    st.write('---')
    if selected_region != "Toutes les régions":
        grouped = grouped.loc[grouped['Région'] == selected_region]
    else:
        grouped = grouped

    fig, ax1 = plt.subplots(figsize=(10, 6))
    grouped['date_transaction'] = pd.to_datetime(grouped['date_transaction'], format='%Y-%m')
    x = grouped.groupby(grouped['date_transaction'])['nombre_transactions'].sum()
    couleur = 'tab:blue'
    ax1.set_xlabel('Année')
    ax1.set_ylabel('Nombre de transactions', color=couleur)
    ax1.plot(x.index, x.values, color=couleur)
    ax1.tick_params(axis='y', labelcolor=couleur)    
    ax2 = ax1.twinx()
    y=grouped.groupby(grouped['date_transaction'])['prix_m2'].mean()
    color = 'tab:red'
    ax2.set_ylabel('Prix moyen au m²', color=color) 
    ax2.plot(y.index, y.values, color=color)
    ax2.tick_params(axis='y', labelcolor=color)    
    plt.title('Nombre de Transactions et prix moyen au m²')
    fig.tight_layout() 
    plt.title('Nombre de Transactions et prix moyen au m²')
    plt.grid(True)
    st.pyplot(fig)

    # 3 - Evolution des prix au m2 en fonction des taux
    st.header('Evolution des prix au m2 en fonction des taux')
    st.write('---')
    if selected_region != "Toutes les régions":
        grouped = grouped.loc[grouped['Région'] == selected_region]
    else:
        grouped = grouped

    fig, ax1 = plt.subplots(figsize=(10, 6))
    grouped['date_transaction'] = pd.to_datetime(grouped['date_transaction'], format='%Y-%m')
    x = grouped.groupby(grouped['date_transaction'])['taux_moyen'].mean()
    couleur = 'tab:blue'
    ax1.set_xlabel('Année')
    ax1.set_ylabel("Taux d'interet moyen", color=couleur)
    ax1.plot(x.index, x.values, color=couleur)
    ax1.tick_params(axis='y', labelcolor=couleur)
    ax2 = ax1.twinx()

    y = grouped.groupby(grouped['date_transaction'])['prix_m2'].mean()
    couleur = 'tab:red'
    ax2.set_ylabel('Prix moyens au m2', color=couleur)
    ax2.plot(y.index, y.values, color=couleur)
    ax2.tick_params(axis='y', labelcolor=couleur)
    plt.title('Evolution des prix au m2 en fonction des taux')
    fig.tight_layout()
    plt.grid()
    st.pyplot(fig)

    # 4 classement des régions par prix au m2
    st.header('Classement des régions par prix au m2')
    st.write('---')

    grouped = pd.read_csv("transactions_csv.csv")
    df = grouped[grouped['date_transaction']=="2023-06"]
    df_sorted = df.sort_values(by="prix_m2", ascending=False)


    fig = px.bar(df_sorted, x="Région", y="prix_m2", title="Prix du mètre carré par région",
             labels={"prix_m2": "Prix du mètre carré", "Région": "Région"},
             width=800, height=500)
    fig.update_layout(width=1000, height=600)
    st.plotly_chart(fig)
