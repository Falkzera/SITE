import streamlit as st

def display_credito():
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

if __name__ == '__main__':
    display_credito()