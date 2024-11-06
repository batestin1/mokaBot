# Mõka Bot - Seu Assistente Virtual da Amazônia Legal

## Descrição

O **[Mõka Bot](https://mokabot.streamlit.app/)** é um assistente virtual desenvolvido com o objetivo de **auxiliar gestores públicos e outros stakeholders** a melhorar o planejamento e a gestão de recursos na região da **Amazônia Legal**, com foco em sustentabilidade, preservação ambiental e políticas públicas. O projeto foi desenvolvido para o **Hackathon Impulso Regional** pela **Tribo Legal**, com a finalidade de fornecer suporte em tempo real para resolver dúvidas frequentes relacionadas a regulamentos, orçamento e gestão fiscal, além de oferecer sugestões práticas para o desenvolvimento sustentável.

## Objetivos do Projeto

O **Mõka Bot** tem como principais objetivos:

1. **Auxiliar gestores a elaborar planos e orçamentos (PPA, LDO, LOA)** com base nas necessidades e vocações locais.
2. **Sugerir práticas de planejamento sustentável e de preservação ambiental** para melhorar a qualidade de vida na região.
3. **Oferecer informações sobre as políticas regionais e federais aplicáveis**, como o Plano de Ação para Prevenção e Controle do Desmatamento na Amazônia (PPCDAm).
4. **Explicar e responder a dúvidas sobre regulamentos e programas federais**, como os de incentivo à redução do desmatamento.
5. **Oferecer assistência em tempo real** para resolver dúvidas frequentes dos gestores, como leis e normas, orçamento e gestão fiscal, usando uma base de conhecimento ou respostas prontas.

## Como Funciona

O **Mõka Bot** foi treinado com dados específicos da região da Amazônia Legal, utilizando a plataforma **Blip** para integração com um chatbot inteligente. A base de dados (localizada na pasta `datasets`) foi usada para alimentar a inteligência artificial do bot, que foi configurado para fornecer respostas rápidas e precisas, além de oferecer sugestões baseadas em práticas sustentáveis.

O bot também está integrado com a plataforma Blip Chat para interação em tempo real com os usuários, garantindo uma comunicação eficiente com gestores e demais interessados.

## Funcionalidades

1. **Integração com o Blip Chat**: O bot pode ser acessado diretamente por meio de uma interface de chat, permitindo uma interação fluida com os usuários.
2. **Página de Contato**: Um formulário para que os usuários possam entrar em contato diretamente com a equipe do projeto.
3. **Informações sobre a Amazônia Legal**: O bot fornece dados importantes sobre a região, sua história, e a importância para o Brasil e o mundo.
4. **Design Responsivo**: A interface foi projetada para ser intuitiva e fácil de navegar, com uma imagem de fundo que reflete a identidade da Amazônia Legal.
5. **Suporte em Tempo Real**: Respostas rápidas a perguntas sobre regulamentações, orçamento, leis ambientais, e políticas de incentivo ao desenvolvimento sustentável.

## Tecnologias Utilizadas

- **Streamlit**: Framework para criar a interface web do chatbot.
- **Blip Chat**: Plataforma para o treinamento e integração do chatbot.
- **Python**: Linguagem de programação usada para o desenvolvimento do backend.
- **Pandas e Numpy**: Para o tratamento de dados.
- **HTML/CSS**: Para personalização da interface, incluindo o design de fundo e interatividade.
- **Base64**: Para conversão de imagens em base64 e carregamento eficiente no frontend.

## Estrutura do Projeto

- **`/assets`**: Contém os arquivos de mídia, como ícones e imagens usadas no projeto.
- **`/datasets`**: Pasta que contém os dados usados para treinar a inteligência do bot. Esses dados incluem informações sobre políticas públicas, sustentabilidade, planejamento financeiro, e leis ambientais.
- **`app.py`**: Arquivo principal do Streamlit que executa o app.
- **`requirements.txt`**: Lista de dependências do projeto para instalação.

## Instalação

Para rodar o projeto localmente, siga as instruções abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/batestin1/moka-bot.git
   cd moka-bot
   ```
2. Crie um ambiente virtual:
    ```
    python -m venv venv
    source venv/bin/activate

    ```
3. Instale as dependências:
    ```
    pip install -r requirements.txt

    ```
4. Execute o aplicativo:

    ```
    streamlit run app.py
    ````
## Contribuidores

Este projeto foi desenvolvido pela **Tribo Legal** durante o **Hackathon Impulso Regional**:

- **`Maycon Cypriano Batestin`**: IA e Desenvolvedor
- **`Cristiane Rodrigues da Silva`** - Design e Negócios
