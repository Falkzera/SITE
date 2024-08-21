import streamlit as st

def styled_text(text, font_size='20px', color='black', text_align='justify'):
    st.markdown(
        f'<p style="font-size:{font_size}; color:{color}; text-align:{text_align};">{text}</p>',
        unsafe_allow_html=True
    )

def display_serie_estudos():
    st.title('Série de Estudos Econômicos:')
    styled_text(
        'A Série Estudos Econômicos, publicada semestralmente pelo Programa de Educação Tutorial em Economia (PET Economia), visa compartilhar e divulgar pesquisas elaboradas pelos membros do PET-Economia, graduandos do curso de Economia e docentes da instituição. Esta série contribui para o debate e a análise de temas relevantes para o Estado de Alagoas.'
        'É importante ressaltar que as conclusões, metodologias e propostas apresentadas nos trabalhos são de responsabilidade exclusiva dos autores e não refletem, necessariamente, a posição ou o endosse oficial do PET-Economia.',
        font_size='20px',
        color='black',
        text_align='justify'
    )
    st.subheader("##")

if __name__ == '__main__':
    display_serie_estudos()