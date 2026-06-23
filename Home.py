import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Portfolio",
    page_icon="🚀",
    layout="wide"
)

# ======================
# CSS (style léger startup)
# ======================
st.markdown("""
<style>
.main-title {
    font-size: 30px;
    font-weight: 700;
}
.subtitle {
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
.card1 {
    padding: 14px;
    border-radius: 12px;
    background-color: white;
    border: 2px solid #800020;
    color: black;
    font-size: 12px;
}
.subtitle1 {
    font-size: 16px;
    color: black;
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER (photo + intro)
# ======================
col1, col2 = st.columns([1, 3])

with col1:
    st.image("Assets/photo.png", width=180)

with col2:
    st.markdown('<div class="main-title"> Malicka-Yacine ZOUHO', unsafe_allow_html=True)

    st.markdown("""
    <div class="subtitle">
    Etudiante en M2 de Business Inteligence & Analytics à EFREI PARIS.
    Passionnée par la science de données, j'aime participé à des projets challengeants et innovants.          
    </div>
    """, unsafe_allow_html=True)

    # Boutons
    colA, colC = st.columns(2)

    with colA:
        st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/malicka-zouho/")

    with colC:
        cv_file = Path("Assets/CV.pdf")
        if cv_file.exists():
            with open(cv_file, "rb") as f:
                st.download_button(
                    "📄 Télécharger mon CV",
                    f,
                    file_name="CV.pdf"
                )


st.markdown("---")

st.markdown("#### 🎓 Formations")

col1, col2 , col3= st.columns(3)

with col1:
    st.markdown("""<div class="subtitle1"><b>Classes préparatoires MPSI/MP<b>""",unsafe_allow_html=True)
    st.write("📍 INP-HB | Côte d'Ivoire")
    st.write("📅 2021 - 2023")
    st.write("""
    - Formation en ingénierie
    - Mathématiques appliquées
    - Informatique / Data / Analyse
    """)

with col2:
    st.markdown("""<div class="subtitle1"><b>Mobilité Internationale<b>""",unsafe_allow_html=True)
    st.write("📍 Staffordshire University | Angleterre")
    st.write("📅 2024")
    st.write("""
    - Mathématiques avancées (algèbre, analyse, équations différentielles)
    - Physique et modélisation scientifique
    - Résolution de problèmes et raisonnement algorithmique
    """)

with col3:
    st.markdown("""<div class="subtitle1"><b>Diplôme d'Ingenieur<b>""",unsafe_allow_html=True)
    st.write("📍 EFREI PARIS | France")
    st.write("📅 2023 - Aujourd'hui")
    st.write("""
    - Analyse et exploitation de données pour l’aide à la décision (BI)
    - Conception de tableaux de bord et reporting (visualisation de données)
    - Modélisation et structuration de données pour l’analyse décisionnelle
    """)
st.markdown("---")

# -------------------------
# EXPERIENCES PROFESSIONNELLES
# -------------------------
st.markdown("#### 💼 Expériences professionnelles")

exp1, exp2 = st.columns(2)

with exp1:
    st.markdown("""<div class="subtitle1"><b>Stage Data Quality Analyst<b>""",unsafe_allow_html=True)
    st.write("🏢 Entreprise : Société Générale Security Services (SGSS)")
    st.write("📅 Période : Juillet/2025 - Janvier/2026")
    st.write("""
    - Contrôle et amélioration de la qualité des données clients dans un environnement international (multi-pays, multi-sources)
    - Automatisation de la détection d’anomalies et du reporting via Alteryx et Excel, réduction du traitement manuel
    - Création de tableaux de bord Power BI et documentation des processus pour assurer la fiabilité et la traçabilité des données
    """)

with exp2:
    st.markdown("""<div class="subtitle1"><b>Chargée Evenementiel<b>""",unsafe_allow_html=True)
    st.write("🏢Entreprise : Junior entreprise SEPEFREI")
    st.write("📅 Période : Mars/2025 - Mars/2026")
    st.write("""
    - Organisation et coordination d’événements étudiants (logistique, planning, gestion des intervenants)
    - Gestion de projet en équipe : répartition des tâches, suivi des deadlines et respect des objectifs
    - Communication et promotion de l’événement auprès des étudiants et partenaires
    """)

st.markdown("---")

# ======================
# PROJETS (mini cards)
# ======================
st.markdown("#### Projets")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    📊 <b>Analyse de données</b><br>
    EDA + visualisations de données
    </div>
    <br>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    🤖 <b>Machine Learning</b><br>
    Prédiction de prix / classification
    </div>
    <br>
    """, unsafe_allow_html=True)



with col3:
    st.markdown("""
    <div class="card">
    📈 <b>Dashboards</b><br>
    Tableau de bord POWER BI
    </div>
    <br>
    """, unsafe_allow_html=True)


st.markdown("---")
# ======================
# COMPÉTENCES (BADGES)
# ======================
st.markdown("#### Compétences Techniques")

st.markdown('<div class="subtitle1"> Language de programation', unsafe_allow_html=True)
st.markdown("""
<span class="badge">Python</span>
<span class="badge">SQL</span>
<span class="badge">Java</span>
""", unsafe_allow_html=True)

st.markdown('<div class="subtitle1"> Data visualisation & Business Intelligence', unsafe_allow_html=True)
st.markdown("""
<span class="badge">Power BI</span>
<span class="badge">Plotly</span>
<span class="badge">Matplotlib</span>
""", unsafe_allow_html=True)

st.markdown('<div class="subtitle1">Bibliothèques Data science & IA', unsafe_allow_html=True)
st.markdown("""
<span class="badge">Pandas</span>
<span class="badge">Numpy</span>
<span class="badge">Scikit-learn</span>
<span class="badge">TensorFlow</span>
<span class="badge">Keras</span>
<span class="badge">XGBoost</span>
""", unsafe_allow_html=True)

st.markdown('<div class="subtitle1"> Bases de données', unsafe_allow_html=True)
st.markdown("""
<span class="badge">MongoDB</span>
<span class="badge">Cassandra</span>
""", unsafe_allow_html=True)


st.markdown('<div class="subtitle1"> Outils Data Business', unsafe_allow_html=True)
st.markdown("""
<span class="badge">Alteryx</span>
<span class="badge">SAP</span>
<span class="badge">Jupiter Notebook</span>
<span class="badge">Excel</span>
""", unsafe_allow_html=True)


st.markdown("#### Certifications")

col4, col5, col6 = st.columns(3)

with col4:
    st.image("Certifs/Malicka-Yacine ZOUHO - Intro to Machine Learning.png", caption="Intro to Machine Learning", width=270)
    st.markdown("<br>", unsafe_allow_html=True)

with col5:
    st.image("Certifs/introduction-to-cybersecurity.png", caption="Introduction to cybersecurity", width=170)
    st.markdown("<br>", unsafe_allow_html=True)



with col6:
    st.image("Certifs/cybersecurity-essentials.png", caption="Cybersecurity Essentials", width=170)
    st.markdown("<br>", unsafe_allow_html=True)

# ======================
# FOOTER
# ======================
st.markdown("---")
st.markdown("🔥 Portfolio développé avec Streamlit | Python | Malicka-yacine Zouho")


