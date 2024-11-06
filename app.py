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

# Função para aplicar o estilo de fundo
def set_background_style():
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{background_image_base64}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 100vh;
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .title {{
                font-size: 4em;
                color: white;
                text-shadow: 2px 2px 8px #4d0d9a;
                font-weight: bold;
                text-align: center;
                margin: 0;
            }}
            /* Responsividade */
            @media only screen and (max-width: 768px) {{
                .title {{
                    font-size: 2.5em;
                    text-align: center;
                }}
            }}
            @media only screen and (max-width: 480px) {{
                .title {{
                    font-size: 2em;
                    padding: 10px;
                }}
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
                background-color: rgba(255, 255, 255, 0.7); /* 70% de transparência para branco */
                background-image: url("data:image/jpg;base64,{background_image_base64}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 100vh;
                width: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .title {{
                font-size: 4em;
                color: white;
                text-shadow: 2px 2px 8px #4d0d9a;
                font-weight: bold;
                text-align: center;
                margin: 0;
            }}
            /* Responsividade */
            @media only screen and (max-width: 768px) {{
                .title {{
                    font-size: 2.5em;
                    text-align: center;
                }}
            }}
            @media only screen and (max-width: 480px) {{
                .title {{
                    font-size: 2em;
                    padding: 10px;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Menu de navegação
menu = st.sidebar.selectbox("Menu", ["Página Principal",  "Sobre Amazônia Legal", "Objetivos", "Contato",])

# Adicionando informações sobre o Bot e a Tribo Legal na sidebar
st.sidebar.markdown("""
    ## O que faço?
    - **Auxilio na elaboração de planos e orçamentos** (PPA, LDO, LOA).
    - **Ofereço informações sobre políticas regionais e federais** como o PPCDAm.
    - **Esclareço dúvidas sobre regulamentos e incentivos à redução do desmatamento.**
    - **E muito mais...**
""")

# Adicionando a imagem do bot na sidebar
bot_image_path = "assets/icon.png"  # Substitua pelo caminho da imagem do seu bot
st.sidebar.image(bot_image_path, caption="Mõka Bot - Seu Assistente Virtual", use_column_width=True)

# Página Principal
if menu == "Página Principal":
    set_background_style()
    st.markdown('<div class="title">Mõka Bot!</div>', unsafe_allow_html=True)
    
    # Função JavaScript para maximizar o Blip Chat e manter sempre aberto
    maximized_chat_script = """<script src="https://unpkg.com/blip-chat-widget" type="text/javascript">

</script>

<script>

    (function () {

        window.onload = function () {

		

           blipClient  = new BlipChat()

            .withAppKey('bW9rYWJvdDE6OWVlMDhhZjItYzM5MS00MmUyLWI2MTEtNzZlZmNlMGE0Mzdi')

			.withEventHandler(BlipChat.LOAD_EVENT, function () {

      blipClient.sendMessage({

                "type": "text/plain",

                "content": "Olá poderia me ajudar"

        });

		})

            .withButton({"color":"#2CC3D5","icon":""})

            .withCustomCommonUrl('https://chat.blip.ai/')

             

			

			blipClient.build();

			window.setTimeout(function() { blipClient.toogleChat() }, 500); 

			const blipChatButton = document.getElementById('blip-chat-open-iframe')

			blipChatButton.classList.remove('opened')





        }

    })();

	

</script>
    """

    # Renderiza o HTML e JavaScript
    html(maximized_chat_script, height=600, width=900, scrolling=True)

#

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

elif menu == "Objetivos":
    set_transparent_background()
    st.header("Objetivos")
    st.write("""
        1) Auxiliar gestores a elaborar planos e orçamentos (PPA, LDO, LOA) com base nas necessidades e vocações locais.
        2) Sugerir práticas de planejamento sustentável e de preservação ambiental.
        3) Oferecer informações sobre as políticas regionais e federais aplicáveis, como o Plano de Ação para Prevenção e Controle do Desmatamento na Amazônia (PPCDAm).
        4) Explicar e responder a dúvidas sobre regulamentos e programas federais, como os de incentivo à redução do desmatamento.
        5) Oferecer assistência em tempo real para resolver dúvidas frequentes dos gestores, como leis e normas, orçamento e gestão fiscal, usando uma base de conhecimento ou respostas prontas.
    """)

 #Página de Contato
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