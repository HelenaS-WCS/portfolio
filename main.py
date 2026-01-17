import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Helena Steyaert - Data analyst", layout="wide")

with st.sidebar:
    st.title("Portfolio :                        Helena Steyaert")
    st.divider()
    st.write("Menu")
    selection = option_menu(
            menu_title=None,
            options = ["Présentation", "Projets","CV"])
    
if selection == "Présentation":
    st.title("Bienvenue sur mon portfolio !")
    st.write("""
    Bonjour! Je m'appelle Helena Steyaert et je suis passionnée par l'analyse de données. 
    Sur ce portfolio, vous trouverez des informations sur mes compétences, mes projets et mon parcours professionnel.
    N'hésitez pas à explorer les différentes sections pour en savoir plus sur moi et mon travail !
    """)    

if selection == "Projets":
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Projet 1", "🎬 Projet 2", "🎲 Projet 3", "🐮 Mission Data"])

    with tab1:
        st.image("images/projet 1/BI 1.PNG")


if selection == "CV":
    st.image("images/CV .jpg",width=800)
    st.download_button(
        label="Télécharger CV",
        data=open("images/1 - Helena Steyaert - CV .pdf", "rb").read(),
        file_name="Helena_Steyaert_CV.pdf")