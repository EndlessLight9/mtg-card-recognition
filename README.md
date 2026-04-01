# mtg-card-recognition
Little fun project for uploading and recognizing MTG cards, adding a camera functionality in the future


# 👁️ Reconhecimento de Cartas MTG com Visão Computacional

Este repositório contém uma aplicação prática de **Visão Computacional Clássica** desenvolvida para identificar cartas do jogo *Magic: The Gathering* através de busca por similaridade geométrica. 

O projeto foi construído como parte de um relatório acadêmico que abordaga programação em Python (OpenCV).

## 🚀 Tecnologias Utilizadas
* **Python 3**
* **OpenCV (`cv2`)**: Para processamento de imagens e extração de características.
* **Algoritmo ORB**: Para detecção de *keypoints* e computação de descritores matemáticos.
* **API do Scryfall**: Para consumo e download automatizado do banco de dados oficial de imagens.
* **Pandas & Requests**: Para manipulação e ingestão dos dados em lote (*batch processing*).

## 🧠 Como Funciona o Motor Visual?
Diferente de modelos de *Deep Learning* que exigem treinamento massivo e são "caixas-pretas", este projeto utiliza **Feature Matching** (Correspondência de Características). 
1. O algoritmo analisa a carta de teste e encontra pontos de alto contraste (quinas, bordas, detalhes da arte).
2. Ele gera uma assinatura matemática para esses pontos.
3. Em seguida, varre o banco de dados cruzando essas assinaturas. A carta do banco que tiver a maior quantidade de correspondências exatas (*matches*) é declarada a vencedora.

---

## ⚙️ Instalação e Configuração (Setup)
1. Clone o repositório
2. Instale as dependências

## Como Usar

Projeto está divido em duas etapas principais: Download do banco de dados e rodar o script de reconhecimento

### Etapa 1: Preparar o banco de Dados

Antes de identificar uma carta precisamos ter a nossa imagem de referência, escolhimos usar informações
de scryfall nesse caso e estarão salvas na pasta 'scryfall_data/'.
Temos duas opções, uma é fazer download uma quantidade aleatória e unica de cartas usando o script 'scryfall_data.py' onde será feito download de 100 cartas únicas e todas serão salvas na pasta mencionada anteriormente.
A segunda opção é fazer download de cartas especificas, caso seja de interesse pro usuário, usando o script 'scryfall_card.py' onde será feito download somente de uma lista de cartas mencionadas.

Cabe dizer que atualmente estamos limitando o uso a upload de imagens de cartas de arte única e em inglês, já que o propósito do projeto não é ter a base de dados completa de scryfall, que seriam mais de 8 GB de dados.

### Etapa 2: Reconhecer a carta

Colocaremos a foto da carta que queremos que seja reconhecida dentro da pasta 'images/', lembre de se cerficiar que o gabarito da carta esteja disponivel na pasta 'scryfall_data'. 
Abra o arquivo script/main.py e execute o script principal, o terminal exibirá a varredura cruzada e informará o nome da imagem que está sendo comparada e o nome da carta identificada.



