import streamlit as st

def styled_text(text, font_size='16px', color='black', text_align='left'):
    """
    Exibe texto estilizado com o tamanho da fonte, cor e alinhamento especificados.
    
    :param text: O texto a ser exibido. Deve ser uma string.
    :param font_size: O tamanho da fonte. Pode ser especificado em pixels (px), pontos (pt), ems, rems, ou outras unidades CSS. 
                      Exemplos: '16px', '24px', '1.5em', '1.2rem'. O valor padrão é '16px'.
    :param color: A cor do texto. Pode ser especificada usando nomes de cores padrão ('black', 'red', 'blue'), 
                  códigos hexadecimais ('#000000', '#FF5733'), ou valores RGB ('rgb(0, 0, 0)'). 
                  O valor padrão é 'black'.
    :param text_align: O alinhamento do texto. Pode ser 'left' (alinhado à esquerda), 'center' (centralizado), 
                        'right' (alinhado à direita) ou 'justify' (justificado). O valor padrão é 'left'.
    """
    html = f'''
    <div style="font-size:{font_size}; color:{color}; text-align:{text_align};">
        {text}
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)