# ShopFlow

**ShopFlow** é uma aplicação de e-commerce desenvolvida para gerenciar produtos, categorias, tipos de produto e atributos personalizados. A estrutura do projeto é altamente flexível, permitindo que os usuários cadastrem produtos com múltiplas variações, atribuam imagens aos produtos e organizem eventos sazonais.

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação e Configuração](#instalação-e-configuração)
- [Usando Docker](#usando-docker)
- [Modelos do Banco de Dados](#modelos-do-banco-de-dados)
- [Funcionalidades](#funcionalidades)
- [Licença](#licença)

## Sobre o Projeto

O **ShopFlow** foi desenvolvido para ser uma solução de e-commerce personalizável, focada em permitir a gestão de produtos com variações de atributos e eventos sazonais. Cada produto pode ter diversas linhas (variações de SKU), associar imagens e vincular a atributos predefinidos. A aplicação também permite a organização de produtos por categorias e tipos.

## Tecnologias Utilizadas

Este projeto utiliza as seguintes tecnologias:

- **Flask**: Framework web principal para criar rotas, views e lógica de negócio.
- **SQLAlchemy**: ORM para gerenciar o banco de dados e os relacionamentos.
- **PostgreSQL**: Banco de dados relacional para armazenar os dados de produtos, categorias e atributos.
- **Pandas**: Utilizado para processar dados em massa, como importar/exportar produtos em formato de planilhas.

## Instalação e Configuração

Siga os passos abaixo para configurar o projeto em sua máquina local:

1. Clone o repositório:
    ```bash
    git clone https://github.com/LucasDiasTavares/flask-shop-flow
    cd flask-shop-flow
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash 
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências do projeto:
    ```bash 
   pip install -r requirements.txt
    ```

4. Configure o banco de dados no arquivo config.py e aplique as migrações:
    ```bash 
   flask db init
    flask db migrate
    flask db upgrade
    ```

5. Inicie o servidor Flask:
    ```bash 
   flask run
    ```

6. A aplicação estará disponível em http://127.0.0.1:5000/.

## Usando Docker
Também é possível executar o projeto usando Docker, o que facilita a configuração do ambiente e a execução da aplicação sem a necessidade de instalar dependências manualmente.

### Passos para rodar o projeto com Docker:
1. Certifique-se de que o Docker e o Docker Compose estão instalados na sua máquina.
2. Execute o Docker Compose para construir as imagens e iniciar os contêineres:
   ```bash
   docker-compose up --build
   ```
3. O serviço Flask estará rodando em `http://127.0.0.1:5000/` e o banco de dados PostgreSQL em `localhost:5432`.
4. Para rodar migrações de banco de dados com Docker, utilize o seguinte comando: 
   ```bash
   docker-compose exec web flask db upgrade
   ```

### Variáveis de Ambiente
- **FLASK_ENV**: Define o ambiente de execução do Flask (development ou production).
- **POSTGRES_USER**: Usuário do banco de dados PostgreSQL.
- **POSTGRES_PASSWORD**: Senha do banco de dados PostgreSQL.
- **POSTGRES_DB**: Nome do banco de dados PostgreSQL.

## Modelos do Banco de Dados

A estrutura de dados do flask-shop-flow inclui as seguintes tabelas e relacionamentos:

- **Product**: Armazena os dados principais de cada produto, como nome, descrição, status (ativo/inativo) e associação com categorias e tipos de produtos.
- **ProductLine**: Representa as diferentes variações de um produto, cada linha possui preço, SKU, estoque e peso.
- **Attribute**: Define os atributos que podem ser associados aos produtos, como cor, tamanho, etc.
- **AttributeValue**: Armazena os valores correspondentes a cada atributo.
- **Category**: Organiza os produtos em diferentes categorias.
- **ProductType**: Define o tipo de produto (ex: Eletrônicos, Roupas).
- **SeasonalEvents**: Permite a criação de eventos sazonais, que podem estar associados a categorias de produtos (ex: Black Friday).

## Funcionalidades

As principais funcionalidades do ShopFlow incluem:

- **Gestão de Produtos**: Adicionar, editar, remover e listar produtos e suas variações.
- **Atributos Personalizados**: Definir e associar atributos aos produtos.
- **Categorias**: Organizar produtos por categorias com hierarquia.
- **Eventos Sazonais**: Criar eventos especiais, como Black Friday, e associar produtos a esses eventos.
- **Gestão de Imagens**: Upload de múltiplas imagens para diferentes linhas de produto.
