import streamlit as st
from streamlit_option_menu import option_menu
from style_background import style_background
from style_text import styled_text
import pandas as pd

# Configuração wide
# Configuração da página
st.set_page_config(
    page_title="Petianos",  # Título da aba do navegador
    page_icon=":write:",                  # Ícone da aba do navegador (opcional)
    layout="wide",                        # Define o layout da página como "wide"
    initial_sidebar_state="expanded"      # Estado inicial da barra lateral ("expanded" ou "collapsed")
)

st.title('Publicações')













# Redes sociais e créditos
with st.sidebar:
    social_media_html = """
    <div style="text-align: center;">
        <h2>Redes Sociais</h2>
        <a href="https://www.instagram.com/petecoufal/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width:40px;height:40px;margin:10px;">
        </a>
        <a href="https://tiktok.com/@petecoufal" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/34/Ionicons_logo-tiktok.svg" alt="TikTok" style="width:40px;height:40px;margin:10px;">
        </a>
    </div>
    """
    st.markdown(social_media_html, unsafe_allow_html=True)
    st.markdown('---')
    st.sidebar.markdown('Developer by: [Lucas Falcão](https://GitHub.com/Falkzera)')