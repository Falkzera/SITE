import streamlit as st
from streamlit_option_menu import option_menu
from Home.Sobre import *
from Home.Novidades import *
from Home.Fotos import *
from Home.Contato import *
from Home.Credito import *
from Home.Petiano import *
from Banner.Banner import display_banner


# Configurações de página
st.set_page_config(
    page_title="Home",  
    page_icon=":house:",                  
    layout="wide",                        
    initial_sidebar_state="auto"     
)


# Menu de navegação
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['Sobre','Petianos','Novidades','Fotos', "Contato" ],
        icons = ['person', 'people', 'newspaper', 'camera', 'envelope'],
        orientation='horizontal') 

# Banner
display_banner()

if selected == 'Sobre':
    display_sobre()

elif selected == 'Petianos':
    display_petianos()

elif selected == 'Novidades':
    display_novidades()

elif selected == "Fotos":
    display_fotos()

elif selected == 'Contato':
    display_contato()

# Redes sociais e créditos
with st.sidebar:
    display_credito()
