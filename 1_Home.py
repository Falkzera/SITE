import streamlit as st
from streamlit_option_menu import option_menu
from style_background import style_background
from style_text import styled_text
import pandas as pd

# Configurações de página
st.set_page_config(
    page_title="Home",  
    page_icon=":home:",                  
    layout="centered",                        
    initial_sidebar_state="expanded"     
)
# Título do site
st.title('Seja-Bem vindo :wave:')
st.title('Ao site do PET ECONOMIA :fire:')

# Subtitle
st.header('Você sabe o que é o PET?')
st.subheader("#")

# Descrição
styled_text(
    'O Programa de Educação Tutorial (PET) foi criado para apoiar atividades acadêmicas que integram ensino, pesquisa e extensão. '
    'Formado por grupos tutoriais de aprendizagem em todo o Brasil, o PET propicia aos alunos participantes, sob a orientação de um tutor, '
    'a realização de atividades extracurriculares que complementem a formação acadêmica do estudante e atendam às necessidades do próprio curso de graduação.',
    font_size='24px',
    color='black',
    text_align='justify'
)
# divisor
st.markdown('---')

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['Novidades','Fotos', "Contato" ],
        icons = ['bell', 'camera', 'envelope'],
        orientation='horizontal',
    ) 

if selected == 'Novidades':
    st.subheader("#")
    st.subheader('Acomapanhe as Novidades do PETECO :fire:') 
    st.subheader("#") 
    st.markdown('#### Vem aí a Semana de Economia!')
    try:
        st.image('image/semana_economia_novo.gif')
    except FileNotFoundError:
        st.error('Imagem da seção de novidades não encontrada.')

elif selected == "Fotos":
    st.markdown('---')
    # st.header('Fotos')
    st.subheader('Um pouco das memórias e histórias do PET Economia')
    st.subheader('#')
    try: 
        st.image('image/capa.png')
    except FileNotFoundError:
        st.error('Imagem da seção de fotos não encontrada.')

elif selected == 'Contato':
    st.header('Contato')
    st.write('Envie-nos uma mensagem.')

    st.text_input('Seu Nome')
    st.text_input('Seu Email')
    st.text_area('Sua Mensagem')
    if st.button('Enviar'):
        st.write('Mensagem enviada com sucesso!')

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