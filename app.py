import streamlit as st
from PIL import Image
import base64
import os
from streamlit.components.v1 import html

# Configuração da Página no Streamlit
st.set_page_config(
    page_title="Mõka Bot - Seu Assistente Virtual da Amazônia Legal",
    page_icon="assets/icon.png",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "About": """
            ## Mõka Bot
            ### Desenvolvido pela Tribo Legal
            **GitHub**: https://github.com/batestin1/
        """
    }
)

# Função para ler a imagem de fundo e convertê-la em base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Defina o caminho relativo da imagem de fundo
background_image_path = 'assets/wallpaper.jpg'
background_image_base64 = get_base64_image(background_image_path)

# CSS para o fundo e o título centralizado
def set_background_style():
    # Fundo padrão com a imagem
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{background_image_base64}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}
            .title {{
                position: absolute;
                top: 10%;
                left: 50%;
                transform: translate(-50%, 190%);
                font-size: 4em;
                color: white;
                text-shadow: 2px 2px 8px #4d0d9a;
                font-weight: bold;
                text-align: center;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

def set_transparent_background():
    # Fundo com transparência para páginas específicas (Sobre Amazônia Legal e Contato)
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-color: rgba(255, 255, 255, 0.1); /* 70% de transparência para branco */
                background-image: url("data:image/jpg;base64,{background_image_base64}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}
            .title {{
                position: absolute;
                top: 10%;
                left: 50%;
                transform: translate(-50%, 190%);
                font-size: 4em;
                color: white;
                text-shadow: 2px 2px 8px #4d0d9a;
                font-weight: bold;
                text-align: center;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Menu de navegação
menu = st.sidebar.selectbox("Menu", ["Página Principal", "Contato", "Sobre Amazônia Legal"])

# Adicionando informações sobre o Bot e a Tribo Legal na sidebar
st.sidebar.markdown("""
    ## Mõka Bot
    ### Desenvolvido pela Tribo Legal
    **GitHub**: [GitHub Repository](https://github.com/batestin1/mokaBot)
""")

# Adicionando a imagem do bot na sidebar
bot_image_path = "assets/icon.png"  # Substitua pelo caminho da imagem do seu bot
st.sidebar.image(bot_image_path, caption="Mõka Bot - Seu Assistente Virtual", use_column_width=True)

# Página Principal
if menu == "Página Principal":
    set_background_style()
    st.markdown('<div class="title">Mõka Bot!</div>', unsafe_allow_html=True)
    
    # Função JavaScript para maximizar o Blip Chat e monitorar o botão de reset
    maximized_chat_script = """<script src="https://unpkg.com/blip-chat-widget" type="text/javascript"></script>
    <script>
        (function () {
            window.onload = function () {
                new BlipChat() 
                    .withAppKey('bW9rYWJvdDE6OWVlMDhhZjItYzM5MS00MmUyLWI2MTEtNzZlZmNlMGE0Mzdi')
                    .withButton({"color":"#0096fa","icon":""})
                    .withCustomCommonUrl('https://maycon-cypriano-batestin-1p16g.chat.blip.ai/')
                    .build();
            }
        })();
    </script>   
    """

    # Renderiza o HTML e JavaScript
    html(maximized_chat_script, height=600, width=900, scrolling=True)

# Página de Contato
elif menu == "Contato":
    set_transparent_background()
    st.header("Contato")
    st.write("Preencha o formulário abaixo para entrar em contato conosco.")
    
    # Formulário de contato
    with st.form(key="contact_form"):
        name = st.text_input("Nome")
        phone = st.text_input("Telefone")
        message = st.text_area("Mensagem")
        
        # Botão de envio
        submit_button = st.form_submit_button("Enviar")
    
    # Confirmação de envio
    if submit_button:
        st.success("Mensagem recebida com sucesso!")

# Página Sobre Amazônia Legal
elif menu == "Sobre Amazônia Legal":
    set_transparent_background()
    st.header("Sobre Amazônia Legal")
    st.write("""
        A Amazônia Legal é uma área de 5,1 milhões de quilômetros quadrados que corresponde a 60% do território brasileiro. 
        Ela é composta por oito estados (Acre, Amapá, Amazonas, Mato Grosso, Pará, Rondônia, Roraima e Tocantins) e parte do Maranhão, 
        a oeste do meridiano de 44ºW.
        
        A Amazônia Legal foi criada pelo governo de Getúlio Vargas, em 1953, com o objetivo de promover o desenvolvimento econômico e social da região. 
        Atualmente, a região é administrada pela Superintendência de Desenvolvimento da Amazônia (SUDAM), uma autarquia federal vinculada ao Ministério do Desenvolvimento Regional.
        
        A Amazônia Legal é importante para a proteção do meio ambiente e dos povos tradicionais. A região é rica em biodiversidade, com uma grande variedade de ecossistemas e paisagens, 
        como a floresta tropical, o Cerrado e o Pantanal. Além disso, a Amazônia Legal abriga 51% dos indígenas brasileiros.
    """)
