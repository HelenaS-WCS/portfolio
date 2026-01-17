import streamlit as st
from streamlit_option_menu import option_menu


# Configuration de la page
st.set_page_config(page_title="Helena Steyaert - Data analyst",layout="centered")

# Menu de navigation dans la barre latérale
with st.sidebar:
    st.title("Helena Steyaert")
    st.subheader("Data Analyst")
    st.write("Portfolio")
    st.divider()
    st.subheader("Menu")
    selection = option_menu(
            menu_title=None,
            options = ["Présentation", "Projets","CV"])
# Page de présentation    
if selection == "Présentation":
    st.title("Bienvenue sur mon portfolio !")
    
    col1,col2 = st.columns([1.8,3])
    with col1: 
        st.image("images/Photo.jpg",width=300)
        st.subheader("Coordonnées:")
        st.write("📞 06 72 10 97 07")
        st.write("📧 helena_steyaert@hotmail.com")
        st.write("🔗 [LinkedIn](https://www.linkedin.com/in/helena-steyaert/)")
        
    with col2:   
        
        st.write("Je suis Helena Steyaert. Je suis ancienne technicienne, puis ingénieure matériaux au sein d’un laboratoire d’essais mécaniques pour des matériaux destinés à l’aéronautique.")
        st.write("""A mon dernier poste, j’ai pu découvrir python, on l’utilisait pour automatiser certaines tâches. 
                J’ai ensuite commencé à m’auto-former et depuis mon intérêt n’a fait que grandir. 
                Après une longue période de réflexion, ainsi qu’un bilan de compétence qui a fait ressortir la Data analyse,
                j’ai décidé de sauter le pas et j’ai fait une formation certifiante de Data Analyst.""") 
        st.write("""Lors de cette formation j’ai pu approfondir mes connaissances en python, ainsi qu’apprendre le SQL,la data-visualisation sur Power BI et les bases du machine learning. 
                J’ai réalisé quelques projets, que vous pourrez découvrir dans la section "projets". 
                Je souhaite continuer mes études en effectuant une alternance de data ingénieur à partir de mars ou octobre 2026.""")
        st.write("""Malgré mon statut junior dans ce domaine, mes expériences professionnelles précédentes m’ont permis de développer une certaine rigueur analytique, une vraie capacité à comprendre les exigences clients, et aussi une bonne base en gestion de projet. Je suis autonome, polyvalente, mais surtout très motivée pour continuer à évoluer dans le domaine de la data.""")    

# Page de projets
if selection == "Projets":
    st.set_page_config(page_title="Helena Steyaert - Data analyst",layout="wide")
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Projet 1", "🎬 Projet 2", "🎲 Projet 3", "🐮 Mission Data"])

    # Projet 1 - Power BI
    with tab1:
        st.image("images/projet 1/BI 1.PNG")

# Page CV
if selection == "CV":
    st.image("images/CV .jpg",width=800)
    st.download_button(
        label="Télécharger CV",
        data=open("images/1 - Helena Steyaert - CV .pdf", "rb").read(),
        file_name="Helena_Steyaert_CV.pdf")