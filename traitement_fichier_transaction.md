```python
import pandas as pd
import numpy as np
```

## Chargement du fichier taux_interet


```python
taux_interet = pd.read_csv('data/taux_interet.csv')
```

## Conversion de la colonne data en datetime


```python
taux_interet['date']=pd.to_datetime(taux_interet['date'])
```

## Création de la colonne année_mois


```python
taux_interet['année_mois'] = taux_interet['date'].dt.to_period('M')
```

## Tri du dataframe par date


```python
taux_interet = taux_interet.sort_values(by='date')
```


```python
taux_interet.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>taux</th>
      <th>année_mois</th>
    </tr>
  </thead>
  <body>
    <tr>
      <th>106</th>
      <td>2014-12-31</td>
      <td>2.55</td>
      <td>2014-12</td>
    </tr>
    <tr>
      <th>105</th>
      <td>2015-01-31</td>
      <td>2.49</td>
      <td>2015-01</td>
    </tr>
    <tr>
      <th>104</th>
      <td>2015-02-28</td>
      <td>2.42</td>
      <td>2015-02</td>
    </tr>
    <tr>
      <th>103</th>
      <td>2015-03-31</td>
      <td>2.34</td>
      <td>2015-03</td>
    </tr>
    <tr>
      <th>102</th>
      <td>2015-04-30</td>
      <td>2.24</td>
      <td>2015-04</td>
    </tr>
  </body>
</table>
</div>



## Chargement du fichier transactions


```python
transaction = np.load('data/transactions.npz')
```

## Affichage du nom des colonnes et du nombre de lignes pour chaque colonnes


```python
for key in transaction.files:
    # transaction[key] accède au tableau NumPy associé à la clé
    print(f"Taille de {key}: {transaction[key].shape}")
```

    Taille de id_transaction: (8318280,)
    Taille de date_transaction: (8318280,)
    Taille de prix: (8318280,)
    Taille de departement: (25038689,)
    Taille de id_ville: (8318280,)
    Taille de ville: (99664044,)
    Taille de code_postal: (8318280,)
    Taille de adresse: (167154686,)
    Taille de type_batiment: (76761974,)
    Taille de vefa: (8318280,)
    Taille de n_pieces: (8318280,)
    Taille de surface_habitable: (8318280,)
    Taille de id_parcelle_cadastre: (124774199,)
    Taille de latitude: (8318280,)
    Taille de longitude: (8318280,)
    Taille de surface_dependances: (29933185,)
    Taille de surface_locaux_industriels: (25445296,)
    Taille de surface_terrains_agricoles: (30594823,)
    Taille de surface_terrains_sols: (46435763,)
    Taille de surface_terrains_nature: (25869120,)
    

## Sélection des data significatives


```python
colonnes_filtrees = {}

for key in transaction.files:
    if transaction[key].shape[0] == 8318280:  # Vérifier si le nombre de lignes correspond
        colonnes_filtrees[key] = transaction[key]
```

## Création du dataframe transactions à partir des colonnes filtrées


```python
transactions = pd.DataFrame(colonnes_filtrees)
transactions.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id_transaction</th>
      <th>date_transaction</th>
      <th>prix</th>
      <th>id_ville</th>
      <th>code_postal</th>
      <th>vefa</th>
      <th>n_pieces</th>
      <th>surface_habitable</th>
      <th>latitude</th>
      <th>longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>126289</td>
      <td>2014-01-02</td>
      <td>197000.0</td>
      <td>427</td>
      <td>1600</td>
      <td>False</td>
      <td>4</td>
      <td>84</td>
      <td>45.942301</td>
      <td>4.770694</td>
    </tr>
    <tr>
      <th>1</th>
      <td>126606</td>
      <td>2014-01-02</td>
      <td>157500.0</td>
      <td>451</td>
      <td>1440</td>
      <td>False</td>
      <td>4</td>
      <td>103</td>
      <td>46.236407</td>
      <td>5.262935</td>
    </tr>
    <tr>
      <th>2</th>
      <td>123875</td>
      <td>2014-01-02</td>
      <td>112000.0</td>
      <td>365</td>
      <td>1290</td>
      <td>False</td>
      <td>3</td>
      <td>78</td>
      <td>46.260087</td>
      <td>4.918587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>130652</td>
      <td>2014-01-02</td>
      <td>173020.0</td>
      <td>202</td>
      <td>1150</td>
      <td>False</td>
      <td>4</td>
      <td>72</td>
      <td>45.899056</td>
      <td>5.354210</td>
    </tr>
    <tr>
      <th>4</th>
      <td>132775</td>
      <td>2014-01-03</td>
      <td>49023.3</td>
      <td>27</td>
      <td>1360</td>
      <td>False</td>
      <td>5</td>
      <td>105</td>
      <td>45.832127</td>
      <td>5.097926</td>
    </tr>
  </tbody>
</table>
</div>



## Création de la colonne année_mois


```python
transactions['année_mois'] = transactions['date_transaction'].dt.to_period('M')
```

## Ajout de la colonne taux au dataframe transaction à l'aide d'une jointure sur la colonne année_mois


```python
transactions = pd.merge(transactions, taux_interet[['année_mois', 'taux']], on='année_mois', how='left')
```


```python
transactions.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id_transaction</th>
      <th>date_transaction</th>
      <th>prix</th>
      <th>id_ville</th>
      <th>code_postal</th>
      <th>vefa</th>
      <th>n_pieces</th>
      <th>surface_habitable</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>année_mois</th>
      <th>taux</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>126289</td>
      <td>2014-01-02</td>
      <td>197000.0</td>
      <td>427</td>
      <td>1600</td>
      <td>False</td>
      <td>4</td>
      <td>84</td>
      <td>45.942301</td>
      <td>4.770694</td>
      <td>2014-01</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>126606</td>
      <td>2014-01-02</td>
      <td>157500.0</td>
      <td>451</td>
      <td>1440</td>
      <td>False</td>
      <td>4</td>
      <td>103</td>
      <td>46.236407</td>
      <td>5.262935</td>
      <td>2014-01</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>123875</td>
      <td>2014-01-02</td>
      <td>112000.0</td>
      <td>365</td>
      <td>1290</td>
      <td>False</td>
      <td>3</td>
      <td>78</td>
      <td>46.260087</td>
      <td>4.918587</td>
      <td>2014-01</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>130652</td>
      <td>2014-01-02</td>
      <td>173020.0</td>
      <td>202</td>
      <td>1150</td>
      <td>False</td>
      <td>4</td>
      <td>72</td>
      <td>45.899056</td>
      <td>5.354210</td>
      <td>2014-01</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>132775</td>
      <td>2014-01-03</td>
      <td>49023.3</td>
      <td>27</td>
      <td>1360</td>
      <td>False</td>
      <td>5</td>
      <td>105</td>
      <td>45.832127</td>
      <td>5.097926</td>
      <td>2014-01</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Suppression des lignes où le taux n'apparait pas


```python
print(transactions.shape)
print(transactions.isnull().sum())
```

    (8318280, 12)
    id_transaction            0
    date_transaction          0
    prix                      0
    id_ville                  0
    code_postal               0
    vefa                      0
    n_pieces                  0
    surface_habitable         0
    latitude                  0
    longitude                 0
    année_mois                0
    taux                 575223
    dtype: int64
    


```python
transactions.dropna(inplace=True)
```

## Retraitement de la colonne code_postal


```python
transactions['code_postal'] = transactions['code_postal'].astype(str) # conversion en chaine de caractères
```


```python
transactions['code_postal'] = transactions['code_postal'].apply(lambda x: x.zfill(5)) # ajout d'un 0 s'il n'y a que 4 caractères
```


```python
transactions.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id_transaction</th>
      <th>date_transaction</th>
      <th>prix</th>
      <th>id_ville</th>
      <th>code_postal</th>
      <th>vefa</th>
      <th>n_pieces</th>
      <th>surface_habitable</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>année_mois</th>
      <th>taux</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5199</th>
      <td>130463</td>
      <td>2014-12-01</td>
      <td>200000.0</td>
      <td>108</td>
      <td>01270</td>
      <td>False</td>
      <td>5</td>
      <td>115</td>
      <td>46.386632</td>
      <td>5.351503</td>
      <td>2014-12</td>
      <td>2.55</td>
    </tr>
    <tr>
      <th>5200</th>
      <td>131354</td>
      <td>2014-12-01</td>
      <td>230000.0</td>
      <td>141</td>
      <td>01300</td>
      <td>False</td>
      <td>4</td>
      <td>94</td>
      <td>45.824796</td>
      <td>5.673966</td>
      <td>2014-12</td>
      <td>2.55</td>
    </tr>
    <tr>
      <th>5201</th>
      <td>130763</td>
      <td>2014-12-01</td>
      <td>118000.0</td>
      <td>283</td>
      <td>01100</td>
      <td>False</td>
      <td>3</td>
      <td>90</td>
      <td>46.261427</td>
      <td>5.665573</td>
      <td>2014-12</td>
      <td>2.55</td>
    </tr>
    <tr>
      <th>5202</th>
      <td>128794</td>
      <td>2014-12-01</td>
      <td>929000.0</td>
      <td>143</td>
      <td>01220</td>
      <td>False</td>
      <td>6</td>
      <td>159</td>
      <td>46.348864</td>
      <td>6.143717</td>
      <td>2014-12</td>
      <td>2.55</td>
    </tr>
    <tr>
      <th>5203</th>
      <td>132111</td>
      <td>2014-12-01</td>
      <td>227280.0</td>
      <td>72</td>
      <td>01250</td>
      <td>False</td>
      <td>4</td>
      <td>82</td>
      <td>46.180232</td>
      <td>5.321355</td>
      <td>2014-12</td>
      <td>2.55</td>
    </tr>
  </tbody>
</table>
</div>



## Ajout de la colonne département


```python
transactions['département'] = transactions['code_postal'].str.slice(0, 2)
```


```python
transactions.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id_transaction</th>
      <th>date_transaction</th>
      <th>prix</th>
      <th>id_ville</th>
      <th>code_postal</th>
      <th>vefa</th>
      <th>n_pieces</th>
      <th>surface_habitable</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>année_mois</th>
      <th>taux</th>
      <th>département</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5199</th>
      <td>130463</td>
      <td>2014-12-01</td>
      <td>200000.0</td>
      <td>108</td>
      <td>01270</td>
      <td>False</td>
      <td>5</td>
      <td>115</td>
      <td>46.386632</td>
      <td>5.351503</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
    </tr>
    <tr>
      <th>5200</th>
      <td>131354</td>
      <td>2014-12-01</td>
      <td>230000.0</td>
      <td>141</td>
      <td>01300</td>
      <td>False</td>
      <td>4</td>
      <td>94</td>
      <td>45.824796</td>
      <td>5.673966</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
    </tr>
    <tr>
      <th>5201</th>
      <td>130763</td>
      <td>2014-12-01</td>
      <td>118000.0</td>
      <td>283</td>
      <td>01100</td>
      <td>False</td>
      <td>3</td>
      <td>90</td>
      <td>46.261427</td>
      <td>5.665573</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
    </tr>
    <tr>
      <th>5202</th>
      <td>128794</td>
      <td>2014-12-01</td>
      <td>929000.0</td>
      <td>143</td>
      <td>01220</td>
      <td>False</td>
      <td>6</td>
      <td>159</td>
      <td>46.348864</td>
      <td>6.143717</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
    </tr>
    <tr>
      <th>5203</th>
      <td>132111</td>
      <td>2014-12-01</td>
      <td>227280.0</td>
      <td>72</td>
      <td>01250</td>
      <td>False</td>
      <td>4</td>
      <td>82</td>
      <td>46.180232</td>
      <td>5.321355</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
    </tr>
  </tbody>
</table>
</div>



## Ajout de la colonne Région


```python
correspondance_df = pd.read_csv('data/correspondance_region.csv') # chargement de la table de correspondance
```


```python
correspondance_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>département</th>
      <th>Région</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01</td>
      <td>Auvergne-Rhône-Alpes</td>
    </tr>
    <tr>
      <th>1</th>
      <td>02</td>
      <td>Hauts-de-France</td>
    </tr>
    <tr>
      <th>2</th>
      <td>03</td>
      <td>Auvergne-Rhône-Alpes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>04</td>
      <td>Provence-Alpes-Côte d'Azur</td>
    </tr>
    <tr>
      <th>4</th>
      <td>05</td>
      <td>Provence-Alpes-Côte d'Azur</td>
    </tr>
  </tbody>
</table>
</div>




```python
departement_to_region = dict(zip(correspondance_df['département'], correspondance_df['Région']))
transactions['Région'] = transactions['département'].map(departement_to_region)
```


```python
transactions.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id_transaction</th>
      <th>date_transaction</th>
      <th>prix</th>
      <th>id_ville</th>
      <th>code_postal</th>
      <th>vefa</th>
      <th>n_pieces</th>
      <th>surface_habitable</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>année_mois</th>
      <th>taux</th>
      <th>département</th>
      <th>Région</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5199</th>
      <td>130463</td>
      <td>2014-12-01</td>
      <td>200000.0</td>
      <td>108</td>
      <td>01270</td>
      <td>False</td>
      <td>5</td>
      <td>115</td>
      <td>46.386632</td>
      <td>5.351503</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
      <td>Auvergne-Rhône-Alpes</td>
    </tr>
    <tr>
      <th>5200</th>
      <td>131354</td>
      <td>2014-12-01</td>
      <td>230000.0</td>
      <td>141</td>
      <td>01300</td>
      <td>False</td>
      <td>4</td>
      <td>94</td>
      <td>45.824796</td>
      <td>5.673966</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
      <td>Auvergne-Rhône-Alpes</td>
    </tr>
    <tr>
      <th>5201</th>
      <td>130763</td>
      <td>2014-12-01</td>
      <td>118000.0</td>
      <td>283</td>
      <td>01100</td>
      <td>False</td>
      <td>3</td>
      <td>90</td>
      <td>46.261427</td>
      <td>5.665573</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
      <td>Auvergne-Rhône-Alpes</td>
    </tr>
    <tr>
      <th>5202</th>
      <td>128794</td>
      <td>2014-12-01</td>
      <td>929000.0</td>
      <td>143</td>
      <td>01220</td>
      <td>False</td>
      <td>6</td>
      <td>159</td>
      <td>46.348864</td>
      <td>6.143717</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
      <td>Auvergne-Rhône-Alpes</td>
    </tr>
    <tr>
      <th>5203</th>
      <td>132111</td>
      <td>2014-12-01</td>
      <td>227280.0</td>
      <td>72</td>
      <td>01250</td>
      <td>False</td>
      <td>4</td>
      <td>82</td>
      <td>46.180232</td>
      <td>5.321355</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
      <td>Auvergne-Rhône-Alpes</td>
    </tr>
  </tbody>
</table>
</div>



## Ajout de la colonne prix_m2


```python
transactions['prix_m2'] = transactions.prix / transactions.surface_habitable
transactions.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id_transaction</th>
      <th>date_transaction</th>
      <th>prix</th>
      <th>id_ville</th>
      <th>code_postal</th>
      <th>vefa</th>
      <th>n_pieces</th>
      <th>surface_habitable</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>année_mois</th>
      <th>taux</th>
      <th>département</th>
      <th>Région</th>
      <th>prix_m2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5199</th>
      <td>130463</td>
      <td>2014-12-01</td>
      <td>200000.0</td>
      <td>108</td>
      <td>01270</td>
      <td>False</td>
      <td>5</td>
      <td>115</td>
      <td>46.386632</td>
      <td>5.351503</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
      <td>Auvergne-Rhône-Alpes</td>
      <td>1739.130435</td>
    </tr>
    <tr>
      <th>5200</th>
      <td>131354</td>
      <td>2014-12-01</td>
      <td>230000.0</td>
      <td>141</td>
      <td>01300</td>
      <td>False</td>
      <td>4</td>
      <td>94</td>
      <td>45.824796</td>
      <td>5.673966</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
      <td>Auvergne-Rhône-Alpes</td>
      <td>2446.808511</td>
    </tr>
    <tr>
      <th>5201</th>
      <td>130763</td>
      <td>2014-12-01</td>
      <td>118000.0</td>
      <td>283</td>
      <td>01100</td>
      <td>False</td>
      <td>3</td>
      <td>90</td>
      <td>46.261427</td>
      <td>5.665573</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
      <td>Auvergne-Rhône-Alpes</td>
      <td>1311.111111</td>
    </tr>
    <tr>
      <th>5202</th>
      <td>128794</td>
      <td>2014-12-01</td>
      <td>929000.0</td>
      <td>143</td>
      <td>01220</td>
      <td>False</td>
      <td>6</td>
      <td>159</td>
      <td>46.348864</td>
      <td>6.143717</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
      <td>Auvergne-Rhône-Alpes</td>
      <td>5842.767296</td>
    </tr>
    <tr>
      <th>5203</th>
      <td>132111</td>
      <td>2014-12-01</td>
      <td>227280.0</td>
      <td>72</td>
      <td>01250</td>
      <td>False</td>
      <td>4</td>
      <td>82</td>
      <td>46.180232</td>
      <td>5.321355</td>
      <td>2014-12</td>
      <td>2.55</td>
      <td>01</td>
      <td>Auvergne-Rhône-Alpes</td>
      <td>2771.707317</td>
    </tr>
  </tbody>
</table>
</div>



## Regroupement du dataframe par date et conservation des colonnes utiles à l'analyse


```python
grouped = transactions.groupby(['année_mois', 'Région']).agg(
    nombre_transactions=('id_transaction', 'count'),
    taux_moyen=('taux', 'mean'),
    prix_m2=('prix_m2', 'mean')
).reset_index()
```


```python
grouped.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>année_mois</th>
      <th>Région</th>
      <th>id_transaction_count</th>
      <th>taux_mean</th>
      <th>prix_m2_mean</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014-12</td>
      <td>Auvergne-Rhône-Alpes</td>
      <td>8692</td>
      <td>2.55</td>
      <td>2538.377408</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014-12</td>
      <td>Bourgogne-Franche-Comté</td>
      <td>2736</td>
      <td>2.55</td>
      <td>1612.686598</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014-12</td>
      <td>Bretagne</td>
      <td>3536</td>
      <td>2.55</td>
      <td>1923.711200</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014-12</td>
      <td>Centre-Val de Loire</td>
      <td>2550</td>
      <td>2.55</td>
      <td>1761.444114</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014-12</td>
      <td>Grand Est</td>
      <td>2264</td>
      <td>2.55</td>
      <td>1547.575417</td>
    </tr>
  </tbody>
</table>
</div>



## Modification du nom de la colonne année_mois en date_transaction


```python
grouped = grouped.rename(columns={'année_mois': 'date_transaction'})
```

## Enregistrement du dataframe grouped en csv


```python
grouped.to_csv('transactions_csv.csv')
```


```python

```
