import streamlit as st
import pandas as pd

def styled_text(text, font_size='20px', color='black', text_align='justify'):
    st.markdown(
        f'<p style="font-size:{font_size}; color:{color}; text-align:{text_align};">{text}</p>',
        unsafe_allow_html=True
    )

def display_boletim(file_path):
    df_boletins = pd.read_excel(file_path)
    df_boletins = df_boletins.iloc[::-1]

    st.title('Boletim da Conjuntura Alagoana:')
    styled_text(
        'A cada seis meses, desenvolvemos e publicamos artigos e relatórios científicos que cobrem uma ampla gama de áreas dentro da Economia. Esses trabalhos são resultados de pesquisas aprofundadas e são compartilhados com a comunidade acadêmica e profissional em seminários e congressos, onde discutimos e socializamos nossas descobertas.'
        'Boletim de Conjuntura Econômica de Alagoas:'
        'Além disso, produzimos um boletim trimestral sobre a conjuntura econômica de Alagoas. Este boletim oferece uma análise abrangente e detalhada de vários aspectos da economia local, incluindo comércio e serviços, balança comercial, mercado de trabalho, agricultura, construção civil e inadimplência. Nosso objetivo é fornecer informações atualizadas e relevantes para ajudar a entender as dinâmicas econômicas da região e apoiar a tomada de decisões informadas.',
        font_size='20px',
        color='black',
        text_align='justify'
    )
    st.subheader("##")

    st.subheader('Selecione o boletim que deseja visualizar:')

    if 'df_boletins' in locals():
        boletim_selecionado = st.selectbox('Escolha uma edição do boletim:', df_boletins['NOME'])
        selected_boletim = df_boletins[df_boletins['NOME'] == boletim_selecionado]
        if not selected_boletim.empty:
            st.markdown(f"[Leia mais]({selected_boletim['LINK'].values[0]})")
    else:
        st.error("O DataFrame 'df_boletins' não está carregado.")
    
    try:
        st.image('image/boletim.png', width=450, use_column_width=None)
    except FileNotFoundError:
        st.error('Imagem da seção de boletim não encontrada.')

if __name__ == '__main__':
    display_boletim('data/boletins.xlsx')