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
    
    # Colonnes : 1 = photo + coordonnées, 2 = présentation
    col1,col2 = st.columns([1.8,3])
    with col1: 
        st.image("images/Photo.jpg",width=300)
        st.subheader("Coordonnées:")
        st.write("📞 06 72 10 97 07")
        st.write("📧 helena_steyaert@hotmail.com")
        st.write("🔗 [LinkedIn](https://www.linkedin.com/in/helena-steyaert/)")
        
    with col2:   
        
        st.write("Je suis Helena Steyaert, ancienne technicienne, puis ingénieure matériaux au sein d’un laboratoire d’essais mécaniques pour des matériaux destinés à l’aéronautique.")
        st.write("""A mon dernier poste, j’ai pu découvrir Python que l'on utilisait pour automatiser certaines tâches. 
                J’ai ensuite commencé à m’auto-former et depuis mon intérêt n’a fait que grandir. 
                Après une longue période de réflexion, ainsi qu’un bilan de compétences qui a fait ressortir la Data analyse,
                j’ai décidé de sauter le pas et j’ai suivi une formation certifiante de Data Analyst.""") 
        st.write("""Lors de cette formation j’ai pu approfondir mes connaissances en Python, ainsi qu’apprendre le SQL, la data-visualisation sur Power BI et les bases du machine learning. 
                J’ai réalisé quelques projets, que vous pouvez découvrir dans la section "projets". 
                Je souhaite continuer mes études en effectuant une alternance de data ingénieur à partir de mars ou octobre 2026.""")
        st.write("""Mes expériences professionnelles précédentes m’ont permis de développer une certaine rigueur analytique, une vraie capacité à comprendre les exigences clients, et aussi une bonne base en gestion de projet. Je suis autonome, polyvalente, mais surtout très motivée pour continuer à évoluer dans le domaine de la data.""")    

# Page de projets
if selection == "Projets":
    
    # Configuration de la page
    st.set_page_config(page_title="Helena Steyaert - Data analyst",layout="wide")
    
    # Création des onglets
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Projet 1 - SQL & BI", "🎬 Projet 2 - Streamlit & ML", "🐮 Projet 3", "🎲 Mission Data - Power BI"])

    # Projet 1 - Power BI
    with tab1:
        st.title("SQL & BI - Toys & Models")
        st.subheader("Objectif :")
        st.write("""Création d'un tableau de bord dynamique qui peut être actualisé chaque matin pour obtenir les dernières informations afin de gérer l’entreprise Toys & Models.
                 Le tableau de bord devait s’articuler autour de 4 axes : ventes, finances, logistique, et ressources humaines.""")
        st.subheader("Première partie : Calcul des métrique en SQL")
        st.write("""Avant de passer sur powerBI, il a fallu calculer les KPI demandés par le client en SQL. 
                 Ceci nous a permis d'explorer la base de données et de déterminer quels attributs étaient nécessaires aux calculs des KPI. 
                 Des vues ont été créées, nous avons défini des tables de fait (FACT) et de dimensions (DIM) pour ensuite créer un modèle relationnel en étoile exploitable dans Power BI.""")
        cola,colb = st.columns([2,1])
        with cola:
            st.subheader("Requête SQL:")
            st.image("images/projet 1/SQL1.PNG",width="stretch")
            
        with  colb:
            st.subheader("Réponse:")
            st.image("images/projet 1/SQL1result.PNG",width="stretch")
            
        cola,colb = st.columns([2,1])
        with cola:
            st.image("images/projet 1/SQL3.PNG",width="stretch")
            
        with  colb:
            st.image("images/projet 1/SQL3result.PNG",width="stretch")
            
        st.subheader("Deuxième partie : Transformation et modélisation des données")
        st.write(""" une fois les vues créées, nous avons pu importer nos tables et nos données dans Power Query afin de transformer et nettoyer les données. 
                 Nous avons également complété le modèle relationnel des données dans Power BI et ajouté la table des dates (pour les mesures DAX notamment).""")
        st.image("images/projet 1/BImodel.PNG",width="stretch")
        
        st.subheader("Troisième partie : Création du tableau de bord")
        st.write("""Avec nos données dans un modèle propre et exploitable, Nous avons pu créer un tableau de bord interactif avec Power BI. 
                 Ce tableau de bord permet d'analyser les performances de l'entreprise, avec des filtres et des visualisations dynamiques.""")
        cola,colb = st.columns([1,1])
        with cola:
            st.image("images/projet 1/BI 1.PNG",width="stretch")
            st.image("images/projet 1/BI 3.PNG",width="stretch")
        with  colb:
            st.image("images/projet 1/BI 2.PNG",width="stretch")
            st.image("images/projet 1/BI 4.PNG",width="stretch")
            
            
    # Projet 2 - Recommandation des films
    with tab2:
        st.title("Projet 2 - Application de recommandation de films avec ML")
        st.write("🔗 [Vous pouvez découvrir notre application ici](https://filmdatalab.streamlit.app/)")

        st.subheader("Objectif :")
        st.write("""Création d'un moteur de recommandation de films sur streamlit avec un modèle de Machine Learning intégré.
                 Nous avons utilisé les bases de données IMDB et TMDB pour créer cette application.""")
        
        st.subheader("Première partie : Etude de marché")
        st.write("""Nous avons commencé par une étude de marché sur la consommation de cinéma en Loire-Atlantique, afin de mieux comprendre les attentes et les préférences du public local. 
                 Cette étape préliminaire nous a permis de définir une orientation adaptée pour la suite de l’analyse de notre base de données.
                 Le but était d'obtenir une dataset contenant entre 5 000 et 10 000 films, pour éviter que l'application soit trop lourde à exécuter.""")
        
        cola,colb = st.columns([1.3,2])
        with cola:
            st.image("images/projet 2/Etude de marché1.PNG",width="stretch")
            
        with  colb:
            st.image("images/projet 2/Etude de marché2.PNG",width="stretch")
            
        st.write("""Après cette étude nous avons décidé de nous focaliser sur les comédies et les films d'animation, en version française, avec une note supérieure à 6/10
                 Ceci répond aux préférences du public local qui reste relativement jeune.""")
            
        st.subheader("Deuxième partie : Récupération, transformation et nettoyage des données")
        st.write("""Les données IMDB et TMDB ont été récupérées avec DuckDB.
                 Les données ont ensuite été transformées avec python (pandas/numpy) et les descriptions, mots clés et les affiches des films ont été récupérées grâce à l'API TMDB.
                 Une fois le nettoyage terminé, nous avons créé quelques visualisations avec matplotlib et seaborn pour mieux comprendre notre dataset.""")
        col1,col2 = st.columns([2,1.85])
        
        with col1:
            st.subheader("Requête DuckDB:")
            st.image("images/projet 2/duckdb.PNG",width="stretch")
            
        with col2:
            st.subheader("Utilisation API:")
            st.image("images/projet 2/api.PNG",width="stretch")
        
        col1,col2 = st.columns([1.5,1])
        
        with col1:
            st.subheader("Matplotlib:")
            st.image("images/projet 2/python0.PNG",width="stretch")
            
        with col2:
            st.subheader("visualisation:")
            st.image("images/projet 2/python0result.PNG",width="stretch")

        st.subheader("Troisième partie : Machine Learning")
        st.write("""Pour pouvoir recommander des films proches d'un film donné, nous avons du créer un modèle de Machine Learning.
                 Nous avons choisi Nearest Neighbors, qui permet de trouver les films les plus similaires en fonction des features choisies.""")
        st.image("images/projet 2/ML.PNG",width=1000)
        
        st.subheader("Quatrième partie : Création de l'application Streamlit")
        st.write("""Une fois tous les éléments prêts, nous avons pu créer l'application de recommandation de films avec Streamlit.
                 Le système de recommandation a été intégré avec un fichier joblib pour plus de rapidité.
                 Une option de recherche par filtres a également été ajoutée. 
                 Nous avons tout mis en oeuvre pour créer une application fluide, ergonomique et (tout simplement) jolie.""")
        
        col1,col2 = st.columns([1,1])
        
        with col1:
            st.image("images/projet 2/streamlit1.PNG",width="stretch")
            st.image("images/projet 2/streamlit3.PNG",width="stretch")
            
        with col2:
            st.image("images/projet 2/streamlit2.PNG",width="stretch")
            st.image("images/projet 2/streamlit4.PNG",width="stretch")
            
    # Projet 3 - en cours (Gouts et Couleurs)
    with tab3:
        st.title("Projet 3 - En cours de réalisation")
        st.image("images/projet 3/work-in-progress.svg",width=400)

    # Mission data - Power BI en 2 jours
    with tab4:
        st.title("Mission Data - Rapport Power BI - Deadline : 2 jours")
        st.write("""Le but de ce mini projet était de créer un petit rapport Power BI à partir d'un dataset réel ou fictif, sur un sujet de notre choix.
                 Etant passionnée de jeux de société, j'ai choisi un dataset de BGG (Board Game Geek) qui recense des milliers de jeux de société avec leurs caractéristiques et notes utilisateurs.
                 Après une courte phase d'exploration et de nettoyage des données, j'ai pu déterminer les KPI les plus pertinents et créer un rapport Power BI interactif en seulement 2 jours.""")
        st.image("images/Mission Data/md1.PNG",width="stretch")
        st.image("images/Mission Data/md2.PNG",width="stretch")
        
# Page CV
if selection == "CV":
    st.title("CV - Helena Steyaert")
    st.image("images/CV .jpg",width=800)
    
    # Bouton de téléchargement
    st.download_button(
        label="Télécharger Mon CV",
        data=open("images/1 - Helena Steyaert - CV .pdf", "rb").read(),
        file_name="Helena_Steyaert_CV.pdf")
