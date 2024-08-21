import streamlit as st
from streamlit_option_menu import option_menu
from Banner.Banner import *
from Atividades.Boletim import *
from Atividades.Nivelamento import *
from Atividades.SerieEstudo import *
from Atividades.Encontros import *
from Atividades.Outros import *
from Home.Credito import *


# Configuração da página
st.set_page_config(
    page_title="Atividades",
    page_icon=":book:",
    layout="wide",       
    initial_sidebar_state="auto"
    )

# Menu de navegação
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ["Boletim", "Nivelamento", "Série de Estudos", "Publicações","Encontros", "Outros"],
        icons = ['file-text', 'book', 'lightbulb', 'calendar', 'three-dots'],
        orientation='horizontal',
    )

# Banner
display_banner()


st.title('Nossas atividades:')
styled_text(
    'O PET Economia realiza diversas atividades durante o ano, selecione a atividade que deseja viusalizar no menu abaixo:',
    font_size='20px',
    color='black',
    text_align='justify'
)
st.subheader("#")


if selected == 'Boletim':
    try:
        file_path = 'pages/boletins.xlsx'
        display_boletim(file_path)
    except FileNotFoundError:
        st.error('Arquivo Excel: Boletins não encontrado.')
    
  
if selected == 'Nivelamento':
    display_nivelamento()

if selected == 'Série de Estudos':
    display_serie_estudos()

if selected == 'Encontros':
    display_interpet()
    display_enepet()
    display_enapet()

if selected == 'Outros':
    display_outras_atividades()

# Redes sociais e créditos
with st.sidebar:
    display_credito()
