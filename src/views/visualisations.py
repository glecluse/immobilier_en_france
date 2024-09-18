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
    st.subheader(f'région sélectionnée : {selected_region}')
        
    transactions_region_selected = grouped.loc[grouped['Région'] == selected_region]

    # 1 nombre de transactions et taux d'intérêt moyen par mois
    st.header('nombre de transactions et taux d\'intérêt moyen par mois')
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
    ax1.set_ylabel('nombre de transactions', color=couleur)
    ax1.plot(x.index, x.values, color=couleur)
    ax1.tick_params(axis='y', labelcolor=couleur)
    ax2 = ax1.twinx()
    couleur = 'tab:red'
    ax2.set_ylabel('taux d\'intérêt moyen', color=couleur)
    ax2.plot(grouped['date_transaction'], grouped['taux_moyen'], color=couleur)
    ax2.tick_params(axis='y', labelcolor=couleur)
    plt.title('nombre de transactions et taux d\'intérêt moyen par année')
    fig.tight_layout()
    plt.grid()
    plt.title('nombre de transactions et taux d\'intérêt moyen par mois')
    st.pyplot(fig)
    
    # 2 - nombre de transactions et prix moyen au m²
    st.header('nombre de transactions et prix moyen au m²')
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
    ax1.set_ylabel('nombre de transactions', color=couleur)
    ax1.plot(x.index, x.values, color=couleur)
    ax1.tick_params(axis='y', labelcolor=couleur)    
    ax2 = ax1.twinx()
    y=grouped.groupby(grouped['date_transaction'])['prix_m2'].mean()
    color = 'tab:red'
    ax2.set_ylabel('prix moyen au m²', color=color) 
    ax2.plot(y.index, y.values, color=color)
    ax2.tick_params(axis='y', labelcolor=color)    
    plt.title('nombre de transactions et prix moyen au m²')
    fig.tight_layout() 
    plt.title('nombre de transactions et prix moyen au m²')
    plt.grid(True)
    st.pyplot(fig)

    # 3 - évolution des prix au m² en fonction des taux
    st.header('évolution des prix au m² en fonction des taux')
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
    ax1.set_ylabel("taux d'intérêt moyen", color=couleur)
    ax1.plot(x.index, x.values, color=couleur)
    ax1.tick_params(axis='y', labelcolor=couleur)
    ax2 = ax1.twinx()

    y = grouped.groupby(grouped['date_transaction'])['prix_m2'].mean()
    couleur = 'tab:red'
    ax2.set_ylabel('prix moyen au m²', color=couleur)
    ax2.plot(y.index, y.values, color=couleur)
    ax2.tick_params(axis='y', labelcolor=couleur)
    plt.title('évolution des prix au m² en fonction des taux')
    fig.tight_layout()
    plt.grid()
    st.pyplot(fig)

    # 4 - classement des régions par prix au m²
    st.header('classement des régions par prix au m²')
    st.write('---')

    grouped = pd.read_csv("transactions_csv.csv")
    df = grouped[grouped['date_transaction']=="2023-06"]
    df_sorted = df.sort_values(by="prix_m2", ascending=False)

    fig = px.bar(df_sorted, x="Région", y="prix_m2", title="prix du mètre carré par région",
                 labels={"prix_m2": "prix du mètre carré", "Région": "région"},
                 width=800, height=500)
    fig.update_layout(width=1000, height=600)
    st.plotly_chart(fig)
