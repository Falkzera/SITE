import streamlit as st

def convert_to_direct_link(link):
    # Verifica se o link é do Google Drive e converte para link de visualização direta
    if 'drive.google.com' in link:
        file_id = link.split('/')[-2]
        direct_link = f"https://drive.google.com/file/d/{file_id}/preview"
        return direct_link
    return link

def display_novidades():
    st.subheader("#")
    st.header('Acomapanhe as Novidades ! 📢') 
    st.subheader('Fique por dentro das últimas notícias do PETECO! 👀')
    st.write("---")
    # st.subheader("#") 
    st.subheader('Boletim 2T/2024 Postado! 🚀')
    st.write('Confira o boletim do PETECO referente ao segundo trimestre de 2024.')

    with st.expander('CLIQUE AQUI PARA VISUALIZAR', expanded=False):
        st.caption('Boletim 2T/2024')
        
        pdf_path = "news/2T_24.pdf"
        # Ler o arquivo PDF
        with open(pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        # Exibir o PDF na página
        st.download_button(label="Baixar PDF", data=pdf_bytes, file_name=pdf_path, mime="application/pdf")

        # Link do Google Drive
        google_drive_link = "https://drive.google.com/file/d/1AuFH30gvOuw6e1qKh1_dZ2CeS12p3Z_j/view"
        direct_link = convert_to_direct_link(google_drive_link)
        
        st.write(f'Visualize Online: [Boletim 2T/24]({direct_link})')
        
        # Exibir o PDF usando um iframe
        st.markdown(f'<iframe src="{direct_link}" width="1000" height="1000"></iframe>', unsafe_allow_html=True)
        
    # Novidade 2
    st.subheader("#") 
    st.header("Semana de Economia :fire:")
    st.write("A semana de economia é um evento que ocorre anualmente na FEAC, com o objetivo de promover a integração entre a comunidade acadêmica.")
    with st.expander('CLIQUE PARA SABER MAIS', expanded=False):
        st.write("A semana de Economia ocorrerá entre os dias 28 a 30 de Agosto, e contará com palestras e minicusros, NÃO PERCA!.")
        st.markdown('#### Vem aí a Semana de Economia! ⚙️')
        try:
            st.image('image/semana_economia_novo.gif')
        except FileNotFoundError:
            st.error('Imagem da seção de novidades não encontrada.')

if __name__ == '__main__':
    display_novidades()