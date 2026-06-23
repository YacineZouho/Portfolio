import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components



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

st.title("📈 Dashboard POWER BI")
st.markdown("""
<div class="subtitle">Ce projet de dashboard repose sur une analyse structurée en deux pages complémentaires, combinant des données de consommation médiatique et des données d'opinion.</div>
""" , unsafe_allow_html=True)

st.divider()
st.markdown("""<div class="subheader"> Page 1 : <div class="subtitle2"> Analyse de l'audience et de la consommation des contenus""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">La première page constitue un tableau de bord de suivi des performances d'audience à partir de données déjà traitées.
            

Cette page permet de mesurer et d'analyser la performance des contenus selon plusieurs dimensions :

- identification des sujets et chaînes les plus performants
- suivi de l'évolution de l'audience dans le temps
- analyse des variations saisonnières (hebdomadaire et mensuelle)
- compréhension des dynamiques de consommation des contenus 
            </div>
""" , unsafe_allow_html=True)

st.markdown("""<div class="subheader"> Page 2 : <div class="subtitle2">Analyse du niveau de confiance dans les sources d'information""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">La seconde page est dédiée à l'étude des perceptions des individus vis-à-vis des sources d'information.

Cette page permet d'identifier les comportements de confiance en fonction des profils sociologiques et démographiques :

- comparaison du niveau de confiance selon les sources
- mise en évidence des écarts entre catégories de population
- analyse des facteurs influençant la perception de l'information
- segmentation des opinions selon les caractéristiques individuelles
            </div>
""" , unsafe_allow_html=True)

st.divider()



html = """<iframe title="Application_Business" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNjc3NGQwOTItYTFjYy00ZTkwLWIzNzgtY2RhMWUzNzgyYWEzIiwidCI6IjQxMzYwMGNmLWJkNGUtNGM3Yy04YTYxLTY5ZTczY2RkZjczMSIsImMiOjh9" frameborder="0" allowFullScreen="true"></iframe>"""

components.html(html, width=1900, height=800)

st.divider()
st.markdown("🔥 Portfolio développé avec Streamlit | Python | Malicka-yacine Zouho")