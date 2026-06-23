import streamlit as st
import smtplib
import sqlite3
import pandas as pd
from datetime import datetime
from email.mime.text import MIMEText


st.set_page_config(page_title="À propos", page_icon="👤", layout="centered")

# ======================
# TITRE
# ======================
st.title("À propos")

st.write("""
Bienvenue sur mon application de data analyse 👨‍💻  
Ce projet a été conçu dans une démarche d’exploration, de visualisation et de valorisation des données.

Je suis passionné par la data, l’intelligence artificielle et la transformation des données en insights exploitables.
""")

# ======================
# CONTACT
# ======================
st.subheader("📬 Contact")

st.write("Vous pouvez me contacter via les moyens suivants :")

st.markdown("""
- 📧 Email : malicka-yacine-francesca.zouho@efrei.net
- 💼 LinkedIn : https://www.linkedin.com/in/tonprofil  
- 🐙 Téléphone: +33 7 65 88 45 02
""")

# ======================
# FEEDBACK
# ======================
st.subheader("💡 Vos avis m'intéresse")

st.write("""
Je cherche constamment à améliorer mes projets, votre retour est donc très précieux.
N'hésite pas à me dire ce que vous pensez de mes projets ou ce qui pourrait être amélioré.
""")



# =========================
# DATABASE (SQLite)
# =========================
conn = sqlite3.connect("feedbacks.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS feedbacks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    message TEXT
)
""")
conn.commit()

# =========================
# EMAIL FUNCTION
# =========================
def send_email(message):

    sender_email = "mprincesse750@gmail.com"
    receiver_email = "mprincesse750@gmail.com"
    password = "ehhe glkw yifs qxdc"

    msg = MIMEText(message)
    msg["Subject"] = "Nouveau feedback Streamlit"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"Erreur email : {e}")
        return False

# =========================
# SAVE TO DATABASE
# =========================
def save_to_db(message):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO feedbacks (date, message) VALUES (?, ?)", (date, message))
    conn.commit()

# =========================
# UI FORM
# =========================
feedback = st.text_area("💬 Laisse ton feedback ici :")

if st.button("Envoyer"):

    if feedback.strip():

        # 1. Save DB
        save_to_db(feedback)

        # 2. Send email
        email_ok = send_email(feedback)

        if email_ok:
            st.success("Merci ! Feedback envoyé et sauvegardé 🙏")
        else:
            st.warning("Sauvegardé mais email non envoyé ⚠️")

    else:
        st.warning("Merci d'écrire un message.")

# =========================
# ADMIN VIEW (historique)
# =========================
st.divider()
st.markdown("🔥 Portfolio développé avec Streamlit | Python | Malicka-yacine Zouho")