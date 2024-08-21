import streamlit as st

def styled_text(text, font_size='20px', color='black', text_align='justify'):
    st.markdown(
        f'<p style="font-size:{font_size}; color:{color}; text-align:{text_align};">{text}</p>',
        unsafe_allow_html=True
    )

def display_nivelamento():
    st.title('Nivelamento de matemática:')
    styled_text(
        'Nossos petianos oferecem aulas especialmente projetadas para preencher possíveis lacunas em matérias quantitativas, com foco especial em pré-cálculo. Essas aulas têm o objetivo de construir uma base sólida e abrangente que prepara os alunos para compreender e abordar temas mais avançados com segurança e confiança. Nosso compromisso é garantir que cada aluno adquira a fundamentação necessária para enfrentar desafios acadêmicos futuros, promovendo uma compreensão profunda dos conceitos fundamentais. Além disso, as aulas são conduzidas de forma interativa e adaptada às necessidades individuais, promovendo um ambiente de aprendizado colaborativo e enriquecedor. Ao oferecer esse suporte, buscamos não apenas preencher lacunas no conhecimento, mas também incentivar a curiosidade intelectual e a paixão pela matemática, preparando nossos alunos para o sucesso em suas jornadas acadêmicas e além.',
        font_size='20px',
        color='black',
        text_align='justify'
    )
    st.subheader("##")
    try:
        st.image('image/nivelamento.png', width=450, use_column_width=None)
    except FileNotFoundError:
        st.error('Imagem da seção de nivelamento não encontrada.')

if __name__ == '__main__':
    display_nivelamento()
