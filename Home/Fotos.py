import streamlit as st

def display_fotos():
    st.markdown('---')
    st.subheader('Um pouco das memórias e histórias do PET Economia')
    st.subheader('#')
    try: 
        st.image('image/capa.png')
    except FileNotFoundError:
        st.error('Imagem da seção de fotos não encontrada.')

if __name__ == '__main__':
    display_fotos()