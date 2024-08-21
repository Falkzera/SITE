import streamlit as st
import pandas as pd

def display_petianos():
    # Configuração da página
    # Caminho absoluto para o arquivo Excel
    try:
        file_path = 'pages/lista_petianos.xlsx'
    except FileNotFoundError:
        st.error('Arquivo Excel: Lista de Petianos não encontrado.')

    # Carregar o arquivo Excel
    df = pd.read_excel(file_path)

    if 'df' in locals():
        # Converter colunas de data para o tipo datetime
        if 'DATA_ENTRADA' in df.columns:
            df['DATA_ENTRADA'] = pd.to_datetime(df['DATA_ENTRADA'], errors='coerce')

            # Título da página
            st.title("PETIANOS DO PET ECONOMIA 🚀")
            st.subheader("Uma vez Petiano, para sempre Petiano :heart:")
            st.write(f"Membros que fizeram e fazem parte da história do PET Economia.")
            col1, col2, col3 = st.columns(3)
            with col2:
                try:
                    st.image('image/keuler_hissa.jpg', width=200)
                except FileNotFoundError:
                    st.error('Imagem do tutor não encontrada.')
                st.markdown('[Tutor: Keuler Hissa](http://lattes.cnpq.br/1732919330877406)')

            # Filtro temporal com slider
            st.sidebar.header("Filtro Temporal")

            # Definir intervalo de datas mínimo e máximo com base nos dados
            min_date = df['DATA_ENTRADA'].min().to_pydatetime()
            max_date = df['DATA_ENTRADA'].max().to_pydatetime()

            # Adicionar o slider de datas
            start_date, end_date = st.sidebar.slider(
                "Selecione o intervalo de datas",
                min_value=min_date,
                max_value=max_date,
                value=(min_date, max_date)
            )

            # Filtrar os dados com base no intervalo selecionado
            filtered_df = df[(df['DATA_ENTRADA'] >= pd.to_datetime(start_date)) & (df['DATA_ENTRADA'] <= pd.to_datetime(end_date))]

            # Exibir dados filtrados (apenas Nome e Imagem)
            # Criar três colunas
            col1, col2, col3 = st.columns(3)

            # Iterar sobre o DataFrame filtrado e distribuir os resultados nas colunas
            for index, row in filtered_df.iterrows():
                if index % 3 == 0:
                    with col1:
                        st.image(row['FOTO'], width=200)
                        st.markdown(f"[{row['NOME']}]({row['LINK']})")
                elif index % 3 == 1:
                    with col2:
                        st.image(row['FOTO'], width=200)
                        st.markdown(f"[{row['NOME']}]({row['LINK']})")
                else:
                    with col3:
                        st.image(row['FOTO'], width=200)
                        st.markdown(f"[{row['NOME']}]({row['LINK']})")
        else:
            st.error("Houve algum erro, verifique o código fonte.")
