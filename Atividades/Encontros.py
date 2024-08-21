import streamlit as st

def styled_text(text, font_size='20px', color='black', text_align='justify'):
    st.markdown(
        f'<p style="font-size:{font_size}; color:{color}; text-align:{text_align};">{text}</p>',
        unsafe_allow_html=True
    )

def display_interpet():
    st.title('INTERPET')
    st.subheader('Encontro Alagoano dos Grupos PET da UFAL (2023.2)')
    styled_text(
        'O InterPET é o Encontro Alagoano dos Grupos do Programa de Educação Tutorial que ocorre a cada seis meses, tem como objetivo proporcionar a troca de experiências por meio de discussões sobre atividades dos grupos e/ou palestras relacionadas ao Programa; promover discussões sobre o PET na Ufal; deliberar em assembleia e fomentar a integração dos grupos PET através de atividades de socialização.',
        font_size='20px',
        color='black',
        text_align='justify'
    )
    st.subheader("##")
    try:
        st.image('image/interpet_2023.jpg', width=450, use_column_width=None)
    except FileNotFoundError:
        st.error('Imagem da seção de InterPET não encontrada.')

def display_enepet():
    st.title('ENEPET')
    st.subheader('Encontro Nordestino dos Grupos PET')
    styled_text(
        'Encontro Nordestino dos Grupos do Programa de Educação Tutorial (ENEPET 2023) é um evento em que a comunidade PETiana da região Nordeste se encontra para discutir questões relacionadas ao Programa de Educação Tutorial (PET) na região e no país. O encontro é caracterizado por assembleias, grupos de discussão e trabalhos, apresentação de trabalhos acadêmicos, atividades culturais, além da troca de experiências entre discentes e tutores nordestinos.'
        'O XXII ENEPET manterá o formato virtual e terá como tema: “Inteligência Artificial, desinformação e ética científica: um debate necessário”. Esta edição busca debater a desinformação no atual contexto das universidades pública brasileira.'
        'O ENEPET 2023 está sendo organizado pelos grupos PETs da Universidade Federal da Paraíba (UFPB).',
        font_size='20px',
        color='black',
        text_align='justify'
    )
    st.subheader("##")
    try:
        st.image('image/enepet_2023.png', width=450, use_column_width=None)
    except FileNotFoundError:
        st.error('Imagem da seção de ENEPET não encontrada.')

def display_enapet():
    st.title('ENAPET')
    st.subheader("Encontro Nacional dos grupos PET's ")
    styled_text(
        'Todos os anos, o Encontro Nacional do Programa de Educação Tutorial (ENAPET) reúne discentes, docentes e interlocutores vinculados ao programa com o objetivo de discutir, coletivamente, temas e questões relevantes para a manutenção e o desenvolvimento do PET nacionalmente.'
        'Em sua 28ª edição, O ENAPET será promovido pela Universidade Federal do Triângulo Mineiro (UFTM)  O evento ocorrerá nos dias 27 e 28 de outubro & 2, 3, e 4 de novembro de 2023, na modalidade remota, e terá como tema central “Programa de Educação Tutorial: Os desafios da permanência estudantil”. Diante do planejamento do Programa de Educação Tutorial de executar atividades que visam estimular e aprimorar os cursos de graduação oferecidos pelas universidades públicas e as ações voltadas à comunidade, o evento deste ano propõe que os participantes reflitam e discutam, por meio de grupos de discussão, apresentações de trabalhos, oficinas e minicursos, o significado e a relevância do PET para a educação brasileira, bem como sua importância para outros âmbitos da sociedade.',
        font_size='20px',
        color='black',
        text_align='justify'
    )
    st.subheader("##")
    try:
        st.image('image/enapet_2023.png', width=450, use_column_width=None)
    except FileNotFoundError:
        st.error('Imagem da seção de ENAPET não encontrada.')

if __name__ == '__main__':
    display_interpet()
    display_enepet()
    display_enapet()