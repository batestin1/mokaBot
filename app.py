import streamlit as st
from PIL import Image
import base64
import requests
from io import BytesIO
from streamlit.components.v1 import html
from PyPDF2 import PdfReader

# Função para ler a imagem de fundo e convertê-la em base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Função para aplicar o estilo de fundo
def set_background_style():
    background_base64 = st.session_state.get("background_image_base64", "")
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{background_base64}");
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

# Defina o caminho relativo da imagem de fundo
background_image_path = 'assets/wallpaper.jpg'

# Inicializa o estado de sessão para a imagem de fundo
if "background_image_base64" not in st.session_state:
    # Inicializa com a imagem padrão se não existir no session_state
    st.session_state["background_image_base64"] = get_base64_image(background_image_path)

# Menu de navegação
menu = st.sidebar.selectbox("Menu", ["Página Principal", "Sobre Amazônia Legal", "Objetivos", "Gerar Imagem", "Perguntas e Respostas", "Contato"])

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
    maximized_chat_script = """<script src="https://unpkg.com/blip-chat-widget" type="text/javascript"></script>
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

# Página Sobre Amazônia Legal
elif menu == "Sobre Amazônia Legal":
    set_background_style()
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

# Página Objetivos
elif menu == "Objetivos":
    set_background_style()
    st.header("Objetivos")
    st.write("""
        1) Auxiliar gestores a elaborar planos e orçamentos (PPA, LDO, LOA) com base nas necessidades e vocações locais.
        2) Sugerir práticas de planejamento sustentável e de preservação ambiental.
        3) Oferecer informações sobre as políticas regionais e federais aplicáveis, como o Plano de Ação para Prevenção e Controle do Desmatamento na Amazônia (PPCDAm).
        4) Explicar e responder a dúvidas sobre regulamentos e programas federais, como os de incentivo à redução do desmatamento.
        5) Oferecer assistência em tempo real para resolver dúvidas frequentes dos gestores, como leis e normas, orçamento e gestão fiscal, usando uma base de conhecimento ou respostas prontas.
    """)

# Página de Contato
elif menu == "Contato":
    set_background_style()
    st.header("Contato")
    st.write("Preencha o formulário abaixo para entrar em contato conosco.")

    with st.form(key="contact_form"):
        name = st.text_input("Nome")
        phone = st.text_input("Telefone")
        message = st.text_area("Mensagem")
        submit_button = st.form_submit_button("Enviar")
    
    if submit_button:
        st.success("Mensagem recebida com sucesso!")

# Página Gerar Imagem
elif menu == "Gerar Imagem":
    set_background_style()  # Mantendo o mesmo fundo
    st.header("Gere uma imagem com o Mõka")

    # Configurações da API do Hugging Face
    api_key = "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"
    model_name = "stabilityai/stable-diffusion-2-1"  # Modelo compatível com a API de inferência
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"

    # Função para gerar a imagem
    def generate_image(prompt):
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        payload = {"inputs": prompt}
        response = requests.post(api_url, headers=headers, json=payload)
        
        if response.status_code == 200:
            image_data = response.content
            return image_data
        else:
            st.error(f"Erro ao gerar a imagem. Status Code: {response.status_code}")
            st.error(f"Detalhes do erro: {response.text}")
            return None

    # Campo de entrada de texto
    prompt = st.text_input("Digite o seu prompt", "Um pôr do sol sobre a Amazônia.")

    # Gerar imagem ao clicar no botão
    if prompt:
        if st.button("Gerar Imagem"):
            image_data = generate_image(prompt)
            if image_data:
                st.image(BytesIO(image_data))
# Página Perguntas e Respostas
elif menu == "Perguntas e Respostas":
      # Interface do Streamlit
    st.title("Perguntas e Respostas com Mõka")
    # Defina a chave de API e a URL do modelo de Q&A
    api_key = "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"
    model_name = "deepset/roberta-base-squad2"  # Modelo de Q&A compatível com a API de inferência
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    set_background_style()  # Mantendo o mesmo fundo
    def generate_answer(question, context):
        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "inputs": {
                "question": question,
                "context": context
            }
        }

        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 200:
            answer_data = response.json()
            return answer_data.get("answer", "Não foi possível encontrar uma resposta.")
        else:
            st.error(f"Erro ao obter a resposta. Status Code: {response.status_code}")
            st.error(f"Detalhes do erro: {response.text}")
            return None

  

    # Campo de entrada de pergunta
    question = st.text_input("Digite sua pergunta", "Resuma o documento em uma palavra!")

    # Upload de arquivo
    uploaded_file = st.file_uploader("Envie um documento (apenas .txt ou .pdf)", type=["txt", "pdf"])

    # Processar o arquivo e gerar resposta ao clicar no botão
    if question and uploaded_file:
        if st.button("Obter Resposta"):
            # Lê o conteúdo do arquivo
            if uploaded_file.type == "application/pdf":
                from PyPDF2 import PdfReader
                pdf_reader = PdfReader(uploaded_file)
                context = " ".join(page.extract_text() for page in pdf_reader.pages)
            else:
                context = uploaded_file.read().decode("utf-8")
            
            # Gera a resposta usando o modelo de Q&A
            answer = generate_answer(question, context)
            if answer:
                st.write("Resposta:", answer)

              