#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ## Chargement du fichier taux_interet

# In[41]:


taux_interet = pd.read_csv('data/taux_interet.csv')


# ## Conversion de la colonne data en datetime

# In[42]:


taux_interet['date']=pd.to_datetime(taux_interet['date'])


# ## Création de la colonne année_mois

# In[43]:


taux_interet['année_mois'] = taux_interet['date'].dt.to_period('M')


# ## Tri du dataframe par date

# In[44]:


taux_interet = taux_interet.sort_values(by='date')


# ## Chargement du fichier transactions

# In[45]:


transaction = np.load('data/transactions.npz')


# ## Affichage du nom des colonnes et du nombre de lignes pour chaque colonnes

# In[46]:


for key in transaction.files:
    # transaction[key] accède au tableau NumPy associé à la clé
    print(f"Taille de {key}: {transaction[key].shape}")


# ## Sélection des data significatives

# In[47]:


colonnes_filtrees = {}

for key in transaction.files:
    if transaction[key].shape[0] == 8318280:  # Vérifier si le nombre de lignes correspond
        colonnes_filtrees[key] = transaction[key]


# ## Création du dataframe transactions à partir des colonnes filtrées

# In[48]:


transactions = pd.DataFrame(colonnes_filtrees)
transactions.head()


# ## Création de la colonne année_mois

# In[49]:


transactions['année_mois'] = transactions['date_transaction'].dt.to_period('M')


# ## Ajout de la colonne taux au dataframe transaction à l'aide d'une jointure sur la colonne année_mois

# In[50]:


transactions = pd.merge(transactions, taux_interet[['année_mois', 'taux']], on='année_mois', how='left')


# In[51]:


transactions.head()


# ## Suppression des lignes où le taux n'apparait pas

# In[52]:


print(transactions.shape)
print(transactions.isnull().sum())


# In[53]:


transactions.dropna(inplace=True)


# ## Retraitement de la colonne code_postal

# In[54]:


transactions['code_postal'] = transactions['code_postal'].astype(str) # conversion en chaine de caractères


# In[55]:


transactions['code_postal'] = transactions['code_postal'].apply(lambda x: x.zfill(5)) # ajout d'un 0 s'il n'y a que 4 caractères


# In[56]:


transactions.head()


# ## Ajout de la colonne département

# In[57]:


transactions['département'] = transactions['code_postal'].str.slice(0, 2)


# In[58]:


transactions.head()


# ## Ajout de la colonne Région

# In[59]:


correspondance_df = pd.read_csv('data/correspondance_region.csv') # chargement de la table de correspondance


# In[60]:


correspondance_df.head()


# In[61]:


departement_to_region = dict(zip(correspondance_df['département'], correspondance_df['Région']))
transactions['Région'] = transactions['département'].map(departement_to_region)


# In[62]:


transactions.head()


# ## Ajout de la colonne prix_m2

# In[63]:


transactions['prix_m2'] = transactions.prix / transactions.surface_habitable
transactions.head()


# ## Suppréssion de lignes incohérentes

# In[69]:


transactions=transactions[transactions['prix']>transactions['prix_m2']]


# ## Regroupement du dataframe par date et conservation des colonnes utiles à l'analyse

# In[70]:


grouped = transactions.groupby(['année_mois', 'Région']).agg(
    nombre_transactions=('id_transaction', 'count'),
    taux_moyen=('taux', 'mean'),
    prix_m2=('prix_m2', 'mean')
).reset_index()


# In[71]:


grouped.head()


# ## Modification du nom de la colonne année_mois en date_transaction

# In[72]:


grouped = grouped.rename(columns={'année_mois': 'date_transaction'})


# In[73]:


grouped.to_csv('transactions_csv.csv')


# In[ ]:




