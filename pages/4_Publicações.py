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














# Redes Sociais e créditos
st.sidebar.title('Redes Sociais')
with st.sidebar:
    st.write('Siga-nos nas redes sociais:')

    social_media_html = """
    <div style="text-align: left;">
        <a href="https://www.instagram.com/petecoufal/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width:40px;height:40px;margin:10px;">
        </a>
    </div>
    """

    with st.sidebar:
        st.markdown(social_media_html, unsafe_allow_html=True)
        st.markdown('---')
        st.sidebar.markdown('Developer by: [Lucas Falcão](https://GitHub.com/Falkzera)')
