import streamlit as st
from streamlit_option_menu import option_menu
from style_background import style_background
from style_text import styled_text
import pandas as pd

# Configuração wide
# Configuração da página
st.set_page_config(
    page_title="Atividades",  # Título da aba do navegador
    page_icon="file-text",                  # Ícone da aba do navegador (opcional)
    layout="wide",                        # Define o layout da página como "wide"
    initial_sidebar_state="expanded"      # Estado inicial da barra lateral ("expanded" ou "collapsed")
)

# Boletim
df_boletins = pd.read_excel(r'C:\Users\lucas\Desktop\PYTHON\CURSOS\CURSO DE PYTHON UDEMY\SITE\pages\boletins.xlsx')
# Inverter a ordem do DataFrame
df_boletins = df_boletins.iloc[::-1]

st.title('Nossas atividades:')
styled_text(
    'O PET Economia realiza diversas atividades durante o ano, selecione a atividade que deseja viusalizar no menu abaixo:',
    font_size='20px',
    color='black',
    text_align='justify'
)
st.subheader("#")


with st.container():
    selected = option_menu(
        menu_title = None,
        options = ["Boletim", "Nivelamento", "Série de Estudos", "Encontros", "Outros"],
        icons = ['file-text', 'book', 'lightbulb', 'calendar', 'three-dots'],
        orientation='horizontal',
    )


if selected == 'Boletim':
    
    st.title('Boletim da Conjuntura Alagoana:')
    styled_text(
            'A cada seis meses, desenvolvemos e publicamos artigos e relatórios científicos que cobrem uma ampla gama de áreas dentro da Economia. Esses trabalhos são resultados de pesquisas aprofundadas e são compartilhados com a comunidade acadêmica e profissional em seminários e congressos, onde discutimos e socializamos nossas descobertas.'
            'Boletim de Conjuntura Econômica de Alagoas:'
'           Além disso, produzimos um boletim trimestral sobre a conjuntura econômica de Alagoas. Este boletim oferece uma análise abrangente e detalhada de vários aspectos da economia local, incluindo comércio e serviços, balança comercial, mercado de trabalho, agricultura, construção civil e inadimplência. Nosso objetivo é fornecer informações atualizadas e relevantes para ajudar a entender as dinâmicas econômicas da região e apoiar a tomada de decisões informadas.',
            
            font_size='20px',
            color='black',
            text_align='justify'
)
    st.subheader("##")
    # # st.image('image/boletim.png', width=450, use_column_width=None)
    # st.subheader("##")



    # Criar uma lista suspensa
    st.subheader('Selecione o boletim que deseja visualizar:')

    # Verificar se o DataFrame está carregado corretamente
    if 'df_boletins' in locals():
        

        # Adicionar seleção da lista suspensa
        boletim_selecionado = st.selectbox('Escolha uma edição do boletim:', df_boletins['NOME'])

        # Exibir o boletim selecionado e o link
        selected_boletim = df_boletins[df_boletins['NOME'] == boletim_selecionado]
        if not selected_boletim.empty:
            # st.write(f"**{selected_boletim['NOME'].values[0]}**")
            st.markdown(f"[Leia mais]({selected_boletim['LINK'].values[0]})")
    else:
        st.error("O DataFrame 'df_boletins' não está carregado.")

    st.image('image/boletim.png', width=450, use_column_width=None)



if selected == 'Nivelamento':
    
    st.title('Nivelamento de matemática:')
    styled_text(
        'Nossos petianos oferecem aulas especialmente projetadas para preencher possíveis lacunas em matérias quantitativas, com foco especial em pré-cálculo. Essas aulas têm o objetivo de construir uma base sólida e abrangente que prepara os alunos para compreender e abordar temas mais avançados com segurança e confiança. Nosso compromisso é garantir que cada aluno adquira a fundamentação necessária para enfrentar desafios acadêmicos futuros, promovendo uma compreensão profunda dos conceitos fundamentais. Além disso, as aulas são conduzidas de forma interativa e adaptada às necessidades individuais, promovendo um ambiente de aprendizado colaborativo e enriquecedor. Ao oferecer esse suporte, buscamos não apenas preencher lacunas no conhecimento, mas também incentivar a curiosidade intelectual e a paixão pela matemática, preparando nossos alunos para o sucesso em suas jornadas acadêmicas e além.',

            font_size='20px',
            color='black',
            text_align='justify'
)
    st.subheader("##")
    st.image('image/nivelamento.png', width=450, use_column_width=None)

if selected == 'Série de Estudos':
    
    st.title('Série de Estudos Econômicos:')
    styled_text(
        'A Série Estudos Econômicos, publicada semestralmente pelo Programa de Educação Tutorial em Economia (PET Economia), visa compartilhar e divulgar pesquisas elaboradas pelos membros do PET-Economia, graduandos do curso de Economia e docentes da instituição. Esta série contribui para o debate e a análise de temas relevantes para o Estado de Alagoas.'
        'É importante ressaltar que as conclusões, metodologias e propostas apresentadas nos trabalhos são de responsabilidade exclusiva dos autores e não refletem, necessariamente, a posição ou o endosse oficial do PET-Economia.',
            font_size='20px',
            color='black',
            text_align='justify'
)
    st.subheader("##")
    # st.image('image/nivelamento.png', width=450, use_column_width=None)

if selected == 'Encontros':
    
    st.title('INTERPET')
    st.subheader('Encontro Alagoano dos Grupos PET da UFAL (2023.2)')
    styled_text(
        'O InterPET é o Encontro Alagoano dos Grupos do Programa de Educação Tutorial que ocorre a cada seis meses, tem como objetivo proporcionar a troca de experiências por meio de discussões sobre atividades dos grupos e/ou palestras relacionadas ao Programa; promover discussões sobre o PET na Ufal; deliberar em assembleia e fomentar a integração dos grupos PET através de atividades de socialização.',
        
            font_size='20px',
            color='black',
            text_align='justify'
)
    st.subheader("##")
    st.image('image/interpet_2023.jpg', width=450, use_column_width=None)

# ATIVIDADE
    st.subheader("##")

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
    st.image('image/enepet_2023.png', width=450, use_column_width=None)

# ATIVIDADE
    st.subheader("##")

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
    st.image('image/enapet_2023.png', width=450, use_column_width=None)

if selected == 'Outros':
    
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
            'A apresentação de trabalhos e pesquisas ou mesmo a defesa de um ponto de vista é uma constante na vida acadêmica do petiano. Apesar disso, muitos alunos apresentam grande dificuldade para falar em público e expor seus argumentos. Pensando em contribuir para a melhoria das exposições orais dos discentes, a atividade busca desenvolver a oratória, além de promover um maior conhecimento dos integrantes do grupo e integração entre eles. ',
                font_size='20px',
                color='black',
                text_align='justify')

    if outros_atividade == 'PET Cidadania':
        st.title('PET Cidadania:')
        styled_text(
            'A discussão de temas éticos, políticos, culturais e educacionais, além daqueles relativos à saúde mental, é de extrema importância para formar cidadãos orientados por senso crítico e valores sociais. Portanto, a atividade consiste em reuniões que visam discutir temas relacionados a questões de diversidade, gênero, raça, preconceito, entre outros. O objetivo é formar cidadãos e cidadãs mais sensíveis às diversas temáticas presentes na sociedade ao seu redor, bem como contribuir para o desenvolvimento do senso crítico dos alunos.',
                font_size='20px',
                color='black',
                text_align='justify')

    if outros_atividade == 'PetecoCast':
        st.title('PetecoCast:')
        styled_text(
            'O PetecoCast é um podcast produzido pelos membros do PET Economia, que tem como objetivo discutir temas relevantes para a economia brasileira e alagoana, além de promover a divulgação científica e a interação com a comunidade acadêmica e profissional. Os episódios são lançados nas redes sociais do pet e abordam assuntos como política econômica, mercado de trabalho, finanças públicas, entre outros. O podcast é uma ferramenta de comunicação e educação que visa levar informações e análises econômicas de qualidade para um público amplo e diversificado.',
                font_size='20px',
                color='black',
                text_align='justify')
    
    if outros_atividade == 'NEPE':
        st.title('Núcleo de Estudos e Pesquisas Ecônomica:')
        styled_text(
            'O Núcleo de Estudos e Pesquisas em Ecônomica (NEPE) é um grupo de estudos formado por alunos do PET, com o objetivo de promover a discussão e a produção de conhecimento na área de Economia. O NEPE realiza reuniões semanais para discutir artigos científicos, dissertações e teses. O grupo também organiza eventos acadêmicos, como seminários e congressos, e desenvolve projetos de pesquisa e extensão em parceria com outras instituições de ensino e pesquisa.',
                font_size='20px',
                color='black',
                text_align='justify')
    
    if outros_atividade == 'Peteco em Discussão':
        st.title('Peteco em Discussão:')
        styled_text(
            'O Peteco em Discussão é um evento organizado pelo PET Economia que tem como objetivo promover a discussão de temas relevantes para a economia brasileira e alagoana. As discussões são mediadas pelos membros do PET e abordam temas como política econômica, mercado de trabalho, finanças públicas, entre outros. O Peteco em Discussão é uma oportunidade para a comunidade acadêmica e profissional debater e refletir sobre questões econômicas atuais e futuras.',
                font_size='20px',
                color='black',
                text_align='justify')


# Redes sociais e créditos
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




