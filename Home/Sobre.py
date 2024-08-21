import streamlit as st

def styled_text(text, font_size='24px', color='black', text_align='justify'):
    st.markdown(
        f'<p style="font-size:{font_size}; color:{color}; text-align:{text_align};">{text}</p>',
        unsafe_allow_html=True
    )

def display_sobre():
    # Título do site
    # st.image('image/banner_site.png', use_column_width=True)
    # st.title('PROGRAMA DE EDUCAÇÃO TUTORIAL DE ECONOMIA DA UFAL')

    # Subtitle
    st.header('Você sabe o que é o PET?')
    # Descrição
    with st.expander('', expanded=True):
        styled_text(
            'O Programa de Educação Tutorial (PET) foi criado para apoiar atividades acadêmicas que integram ensino, pesquisa e extensão. '
            'Formado por grupos tutoriais de aprendizagem em todo o Brasil, o PET propicia aos alunos participantes, sob a orientação de um tutor, '
            'a realização de atividades extracurriculares que complementem a formação acadêmica do estudante e atendam às necessidades do próprio curso de graduação.',
            font_size='24px',
            color='black',
            text_align='justify'
        )

if __name__ == '__main__':
    display_sobre()