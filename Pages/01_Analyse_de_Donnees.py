import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ======================
# CSS (style léger startup)
# ======================
st.markdown("""
<style>
.main-title {
    font-size: 30px;
    font-weight: 700;
}
.subheader {
    font-size: 22px;
    font-weight: 700;
}
.texte {
    font-size: 15px;
    color: #666;
}
.badge {
    display: inline-block;
    padding: 6px 12px;
    margin: 4px;
    border-radius: 12px;
    background-color: white;
    border: 2px solid #800020;
    color: black;
    font-size: 12px;
            
}
.card {
    padding: 14px;
    border-radius: 12px;
    background-color: #f5f5f5;
}
.subtitle1 {
    font-size: 16px;
    color: black;
}
.subtitle2 {
    font-size: 20px;
    color: #800020;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Analyse des données des chaines de télévision ( 2000-2020)")

st.markdown("""
<div class="subtitle">Cette étude a pour objectif d'analyser l'évolution des chaînes de télévision TF1, France 2, M6, France 3 et Arte entre 2000 et 2020 à travers un jeu de données regroupant différentes informations relatives à leur audience, leur popularité et leurs performances au fil des années.

L'industrie audiovisuelle a connu de profondes transformations durant cette période, notamment avec l'arrivée d'Internet, des plateformes de streaming et l'évolution des habitudes de consommation des médias. Cette étude permet de mettre en évidence les tendances majeures qui ont marqué le secteur sur deux décennies.
</div>
""" , unsafe_allow_html=True)

st.divider()

st.markdown('<div class="main-title">Objectifs de cette analyse', unsafe_allow_html=True)


st.markdown("""
<div class="subtitle">
- Comprendre l'évolution des audiences par chaîne,
- Etudier la structure et la qualité du dataset,
- Identifier des profils éditoriaux de chaînes,
- Distinguer les effets réels de diffusion des effets liés à la structure des données.

L'objectif principal n'est pas uniquement descriptif, mais analytique et critique, en mettant en évidence les biais potentiels du dataset et la manière dont ils influencent les résultats.
</div>""", unsafe_allow_html=True)
            
st.markdown("""<div class="subtitle1">L'approche suivie reproduit les principales étapes d'un projet Data Analyst :
""", unsafe_allow_html=True)

st.markdown("""<div class="subtitle">
            
- Compréhension des données

- Nettoyage et préparation
- Analyse exploratoire
- Analyse des tendances temporelles
- Réduction dimensionnelle
- Interprétation des résultats
-  Conclusion et recommandations
 </div>
""" , unsafe_allow_html=True)

st.divider() 

st.markdown('<div class="subheader"> Compétences mobilisées', unsafe_allow_html=True)
st.markdown("""
<span class="badge">Python</span>
<span class="badge">Pandas</span>
<span class="badge">NumPy</span>
<span class="badge">Matplotlib</span>
<span class="badge">Seaborn</span>
<span class="badge">Analyse exploratoire de données (EDA)</span>
<span class="badge">Visualisation de données</span>
<span class="badge">Storytelling analytique</span>
<span class="badge">Analyse de la qualité des données</span>     
""", unsafe_allow_html=True)

st.divider()

# ==========================
# 2. CHARGEMENT DES DONNÉES
# ==========================
st.markdown('<div class="main-title">Nettoyage des données', unsafe_allow_html=True)

st.markdown("""<div class="subtitle">Avant toute analyse, il est nécessaire de vérifier la qualité des données afin d'éviter des résultats biaisés ou erronés.""", unsafe_allow_html=True)

df = pd.read_csv("Data/Données.csv",delimiter=';',header=None, encoding="latin-1")
df.columns = ['date', 'chaine', 'vide', 'thème', 'number', 'auditoire']
df.drop(columns=['vide'], inplace=True)

st.markdown('<div class="subheader"> Aperçu des données', unsafe_allow_html=True)

st.dataframe(df.head())


# ==========================
# 3. Info sur le dataset
# ==========================
st.markdown('<div class="subheader"> Informations sur le dataset', unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Nombre de lignes", df.shape[0])

with col2:
    st.metric("Nombre de colonnes", df.shape[1])

with col3:
    st.metric("Valeurs manquantes", df.isna().sum().sum())



st.markdown("Types des variables")

st.dataframe(
    pd.DataFrame({
        "Variable": df.columns,
        "Type": df.dtypes.astype(str)
    }),
    use_container_width=True
)


st.divider()

st.markdown("""<div class="subtitle2">Interprétation
""", unsafe_allow_html=True)

st.markdown("""<div class="subtitle1">
Les éventuelles valeurs manquantes ou doublons sont identifiés et traités afin de garantir la fiabilité des résultats.
Au vu des résultats qu'on a on voit bien que le jeu de données est suffisamment propre pour poursuivre l'analyse. 
            </div>
""" , unsafe_allow_html=True)

st.divider()



# ==========================
# 4. Analyse Exploratoire des données
# ==========================

st.markdown('<div class="main-title">Analyse exploratoire', unsafe_allow_html=True)
st.markdown("""<div class="subtitle">L'analyse exploratoire permet d'obtenir une première compréhension du comportement des chaînes de télévision entre 2000 et 2020.
             <br>
            """, unsafe_allow_html=True)

st.markdown("""<div class="subheader">Statistiques descriptives""", unsafe_allow_html=True)

st.dataframe(df.describe())


# Distribution des données
st.markdown("""<div class="subheader">Distribution des valeurs""", unsafe_allow_html=True)
col_num = df.select_dtypes(include="number").columns
variable = st.selectbox(
    "Choisir une variable",
    col_num
)
fig, ax = plt.subplots()
ax.hist(df[variable], bins=20)
ax.set_title(variable)
st.pyplot(fig)

st.divider()

st.markdown("""<div class="subtitle2">Interprétation
""", unsafe_allow_html=True)
st.markdown("Number")
st.markdown("""<div class="subtitle1">
L'analyse de la distribution révèle une forte concentration des programmes sur de faibles fréquences de diffusion.
La présence d'une longue queue à droite indique que quelques émissions sont diffusées beaucoup plus souvent que la moyenne. 
Cette asymétrie traduit une stratégie de programmation reposant sur un nombre limité de programmes à forte récurrence.
             <br>
            </div>
""" , unsafe_allow_html=True)
st.markdown("Auditoir")
st.markdown("""<div class="subtitle1">
Quelques émissions captent une part importante des téléspectateurs tandis que la majorité des programmes attire des audiences modérées.
              <br>
            </div>
           
 """ , unsafe_allow_html=True)

st.divider()


#Matrice de correlation
st.markdown("""<div class="subheader">Matrice de correlation""", unsafe_allow_html=True)
corr = df.select_dtypes(include="number").corr()
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    ax=ax
)
st.pyplot(fig)

st.divider()

st.markdown("""<div class="subtitle2">Interprétation
""", unsafe_allow_html=True)
st.markdown("""<div class="subtitle1">
Il y a une corrélation de 0,88. Elle est considérée comme très forte, positive et linéaire

Cela signifie que plus un programme est diffusé fréquemment, plus son audience tend à être élevée.    
            
Cela revient à determiner qu'environ"77%" de la variation observée dans l'audiance peut être expliqué pas la fréquence de diffusion des programmes.     
              </div>
""" , unsafe_allow_html=True)

st.divider()


#Repartition des données par chaines
st.markdown("""<div class="subheader">Repatition des donées par chaines""", unsafe_allow_html=True)
nb_donnees = (
    df.groupby("chaine")
      .size()
      .reset_index(name="nombre_donnees")
      .sort_values("nombre_donnees", ascending=False)
)
fig = px.bar(
    nb_donnees,
    x="chaine",
    y="nombre_donnees",
    text="nombre_donnees",
    
)
st.plotly_chart(fig, use_container_width=True)
st.dataframe(nb_donnees)

st.divider()

st.markdown("""<div class="subtitle2">Interprétation
""", unsafe_allow_html=True)
st.markdown("""<div class="subtitle1">
Ces écarts indiquent une différence notable de volume entre chaînes, avec TF1 et France 2 en tête, et Arte présentant un volume significativement plus faible.
On pourait se dire que cela est dû au fait que les thèmes sont moins diversifiées chez Arte</div>
""" , unsafe_allow_html=True)

st.divider()

st.markdown("""<div class="subheader">Nombre de Thème par chaine""", unsafe_allow_html=True)
st.dataframe(df.groupby("chaine")["thème"].nunique())

st.divider()

st.markdown("""<div class="subtitle2">Interprétation
""", unsafe_allow_html=True)
st.markdown("""<div class="subtitle1">
Cela indique que la diversité thématique est strictement identique entre chaînes dans le dataset.
Alors et si les chaînes ne se distinguent pas par leur nombre de thèmes, mais par la manière dont ces thèmes sont exploités et enregistrés?""" , unsafe_allow_html=True)

st.divider()
# 2. Moyenne par chaîne
st.markdown("""<div class="subheader">Enregistrement moyen par jour""", unsafe_allow_html=True)
daily = (
    df.groupby(["date", "chaine"])
      .size()
      .reset_index(name="Enregistrement moyen par jour")
)

moyenne_par_chaine = (
    daily.groupby("chaine")["Enregistrement moyen par jour"]
         .mean()
         .reset_index()
         .sort_values("Enregistrement moyen par jour", ascending=False)
)
st.dataframe(moyenne_par_chaine)

st.divider()
st.markdown("""<div class="subtitle2">Interprétation
""", unsafe_allow_html=True)
st.markdown("""<div class="subtitle1">
On observe une hiérarchie claire dans la densité des enregistrements :

- chaînes généralistes (TF1, France 2) → forte granularité
- chaînes intermédiaires (France 3, M6) → granularité moyenne
- Arte → granularité plus faible
            
On peut considerer selon laquelle ces différences reflètent principalement la structure des données (découpage des programmes, segmentation des événements), et non une différence de contenu ou de volume réel de diffusion.""" , unsafe_allow_html=True)
st.divider()


df["date"] = pd.to_datetime(df["date"], dayfirst=True)
presence_par_jour = (
    df.groupby(["date", "chaine"])
      .size()
      .unstack(fill_value=0)
)

all_dates = pd.date_range(df["date"].min(), df["date"].max(), freq="D")
all_chaines = df["chaine"].unique()
full_index = pd.MultiIndex.from_product(
    [all_dates, all_chaines],
    names=["date", "chaine"]
)
presence = (
    df.groupby(["date", "chaine"])
      .size()
      .reindex(full_index, fill_value=0)
      .reset_index(name="nb_enregistrements")
)
absences = presence[presence["nb_enregistrements"] == 0]

st.markdown("""<div class="subheader">Nombre de jour sans enregistrement""", unsafe_allow_html=True)
zeros_par_chaine = (
    absences
    .groupby("chaine")
    .size()
    .reset_index(name="nb_jours_0")
    .sort_values("nb_jours_0", ascending=False)
)
st.dataframe(zeros_par_chaine)

st.divider()
st.markdown("""<div class="subtitle2">Interprétation
""", unsafe_allow_html=True)
st.markdown("""<div class="subtitle1">
Le dataset est structuré de manière homogène sur les thèmes, mais hétérogène sur le volume et la granularité, ce qui indique une représentation structurée plutôt qu'une mesure brute de la réalité télévisuelle.
            
Les différences entre chaînes sont cohérentes avec la structure des données (granularité, segmentation, couverture), plutôt qu'avec des différences réelles d'activité télévisuelle.
            
Ainsi, les résultats doivent être interprétés comme une lecture de la représentation des données télévisuelles dans le dataset, et non comme une mesure directe de la performance ou de la diversité des chaînes.
""" , unsafe_allow_html=True)
st.divider()

df["date"] = pd.to_datetime(df["date"], dayfirst=True)



# PCA

features = df.groupby(["chaine", "thème"]).size().unstack(fill_value=0)
features_norm = features.div(features.sum(axis=1), axis=0)

X = StandardScaler().fit_transform(features_norm)

pca = PCA(n_components=2)
components = pca.fit_transform(X)

pca_df = pd.DataFrame(components, columns=["PC1", "PC2"])
pca_df["chaine"] = features_norm.index

st.markdown("""<div class="subheader">Projection PCA des chaînes""", unsafe_allow_html=True)

fig = px.scatter(
    pca_df,
    x="PC1",
    y="PC2",
    text="chaine",
    title="Carte des chaînes TV (PCA)",
)

fig.update_traces(textposition="top center")

st.plotly_chart(fig, use_container_width=True)

st.divider()
st.markdown("""<div class="subtitle2">Interprétation
""", unsafe_allow_html=True)
st.markdown("""<div class="subtitle1">
La projection PCA met en évidence une structuration claire des chaînes en plusieurs profils éditoriaux. Arte apparaît comme une chaîne fortement distincte, tandis que TF1, France 2, M6 et France 3 forment un groupe plus homogène mais différencié selon une seconde dimension liée à la dynamique de diffusion ou d'audience.""" , unsafe_allow_html=True)
st.divider()

st.divider()
st.markdown("🔥 Portfolio développé avec Streamlit | Python | Malicka-yacine Zouho")