import streamlit as st

def styled_text(text, font_size='20px', color='black', text_align='justify'):
    st.markdown(
        f'<p style="font-size:{font_size}; color:{color}; text-align:{text_align};">{text}</p>',
        unsafe_allow_html=True
    )

def display_outras_atividades():
    st.title('Outras atividades:')
    styled_text(
        'Além das atividades mencionadas acima, o PET Economia também realiza diversas outras atividades ao longo do ano, incluindo:'
        'Workshops e palestras sobre temas relevantes para a economia brasileira e alagoana;'
        'Participação em eventos acadêmicos, como congressos e seminários;'
        'Atividades de extensão, como aulas de reforço escolar e orientação profissional;'
        'Projetos de pesquisa e extensão em parceria com outras instituições de ensino e pesquisa;'
        'Atividades de integração e socialização entre os membros do grupo PET e a comunidade acadêmica.'
        'Selecione a atividade que deseja visualizar melhor no menu abaixo:',
        font_size='20px',
        color='black',
        text_align='justify'
    )
    st.subheader("##")

    outros_atividade = st.selectbox('Escolha uma atividade:', ['Apresenta PET', 'PET Cidadania', 'PetecoCast', 'NEPE', 'Peteco em Discussão'])
    
    if outros_atividade == 'Apresenta PET':
        st.title('Apresenta PET:')
        styled_text(
            'A apresentação de trabalhos e pesquisas ou mesmo a defesa de um ponto de vista é uma constante na vida acadêmica do petiano. Apesar disso, muitos alunos apresentam grande dificuldade para falar em público e expor seus argumentos. Pensando em contribuir para a melhoria das exposições orais dos discentes, a atividade busca desenvolver a oratória, além de promover um maior conhecimento dos integrantes do grupo e integração entre eles.',
            font_size='20px',
            color='black',
            text_align='justify'
        )

    elif outros_atividade == 'PET Cidadania':
        st.title('PET Cidadania:')
        styled_text(
            'A discussão de temas éticos, políticos, culturais e educacionais, além daqueles relativos à saúde mental, é de extrema importância para formar cidadãos orientados por senso crítico e valores sociais. Portanto, a atividade consiste em reuniões que visam discutir temas relacionados a questões de diversidade, gênero, raça, preconceito, entre outros. O objetivo é formar cidadãos e cidadãs mais sensíveis às diversas temáticas presentes na sociedade ao seu redor, bem como contribuir para o desenvolvimento do senso crítico dos alunos.',
            font_size='20px',
            color='black',
            text_align='justify'
        )

    elif outros_atividade == 'PetecoCast':
        st.title('PetecoCast:')
        styled_text(
            'O PetecoCast é um podcast produzido pelos membros do PET Economia, que tem como objetivo discutir temas relevantes para a economia brasileira e alagoana, além de promover a divulgação científica e a interação com a comunidade acadêmica e profissional. Os episódios são lançados nas redes sociais do pet e abordam assuntos como política econômica, mercado de trabalho, finanças públicas, entre outros. O podcast é uma ferramenta de comunicação e educação que visa levar informações e análises econômicas de qualidade para um público amplo e diversificado.',
            font_size='20px',
            color='black',
            text_align='justify'
        )

    elif outros_atividade == 'NEPE':
        st.title('Núcleo de Estudos e Pesquisas Econômica:')
        styled_text(
            'O Núcleo de Estudos e Pesquisas em Economia (NEPE) é um grupo de estudos formado por alunos do PET, com o objetivo de promover a discussão e a produção de conhecimento na área de Economia. O NEPE realiza reuniões semanais para discutir artigos científicos, dissertações e teses. O grupo também organiza eventos acadêmicos, como seminários e congressos, e desenvolve projetos de pesquisa e extensão em parceria com outras instituições de ensino e pesquisa.',
            font_size='20px',
            color='black',
            text_align='justify'
        )

    elif outros_atividade == 'Peteco em Discussão':
        st.title('Peteco em Discussão:')
        styled_text(
            'O Peteco em Discussão é um evento organizado pelo PET Economia que tem como objetivo promover a discussão de temas relevantes para a economia brasileira e alagoana. As discussões são mediadas pelos membros do PET e abordam temas como política econômica, mercado de trabalho, finanças públicas, entre outros. O Peteco em Discussão é uma oportunidade para a comunidade acadêmica e profissional debater e refletir sobre questões econômicas atuais e futuras.',
            font_size='20px',
            color='black',
            text_align='justify'
        )