# 2024.2 Aries - Projeto Mamutes do Cerrado

<p align="center">
  <img src="./docs/view/img/logoMamutes.PNG" height='300px' style={{ display: 'block', margin: 'auto', marginTop: '100px' }} />
</p>

# Sobre

Este projeto visa o desenvolvimento de um aplicativo web, concebido para atender às necessidades da equipe de competição Mamutes do Cerrado da UnB - FCTE. A proposta é oferecer uma plataforma unificada que atenda dois pilares principais: divulgação da equipe e gerenciamento interno, otimizando a organização e a visibilidade da equipe.

## Objetivos do Sistema

1. **Divulgação da Equipe**
   - Uma página inicial que apresente a identidade visual dos Mamutes do Cerrado, seus integrantes, competições e informações essenciais, como o processo seletivo para novos membros.

2. **Gerenciamento Interno**
   - **Gerência de Tarefas e Eventos:** Uma interface com quadro Kanban para organização de tarefas e um calendário que consolida os compromissos da equipe.
   - **Gerência de Estoque:** Controle detalhado de peças e materiais, incluindo quantidades disponíveis e status atualizado.
   - **Gerência de Reuniões:** Registro de atas e controle de presença nas reuniões, promovendo transparência e acompanhamento das decisões.
   - **Gerência de Documentos:** Administração centralizada de arquivos relacionados à equipe, como documentos de voo e outros correlatos.

# Documentação

Link para a documentação do projeto: [MkDocs - Aries 2024.2](https://fga0138-mds-ajax.github.io/2024.2-Aries/) <br><br>

# Equipe

<table align="center">
  <tr>
    <td align="center">
      <img src="./docs/view/img/marinaMello.jpeg" width=100><br>
      <b><a href="https://www.linkedin.com/in/marina-mello-1a679a312/">Marina Mello</a></b><br>
      Product Owner
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/134105981?v=4" width=100><br>
      <b><a href="https://github.com/caioduart3">Caio Duarte</a></b><br>
      Scrum Master
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/91512745?v=4" width=100><br>
      <b><a href="https://github.com/ludmilaaysha">Ludmila Aysha</a></b><br>
      Ponto Focal - Front End
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/179030119?" width=100><br>
      <b><a href="https://github.com/RafaelSchadt">Rafael Schadt</a></b><br>
      Ponto Focal - Back End
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/62055315?v=4" width=100><br>
      <b><a href="https://github.com/FelipeFreire-gf">Felipe Freire</a></b><br>
      Ponto Focal - Banco de Dados
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/173021374?v=4" width=100><br>
      <b><a href="https://github.com/Felipej3ds">Felipe Duarte</a></b><br>
      Ponto Focal - Testes
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/128251768?v=4" width=100><br>
      <b><a href="https://github.com/mandicrz">Amanda Cruz</a></b><br>
      DEV
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/144369305?v=4" width=100><br>
      <b><a href="https://github.com/maymarquee">Mayara Marques</a></b><br>
      DEV
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/149620306?v=4" width=100><br>
      <b><a href="https://github.com/bolzanMGB">Othavio Bolzan</a></b><br>
      DEV
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/69173517?v=4" width=100><br>
      <b><a href="https://github.com/vinialves2020">Vinicíus Alves</a></b><br>
      DEV
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/145882190?v=4" width=100><br>
            <b><a href="https://github.com/isaqzin">Isaque Camargos</a></b><br>
      DEV
    </td>
  </tr>
</table>

## Pré-requisitos 
Para rodar o projeto, é necessário que essas dependências estejam instaladas na sua máquina: 
- Python 3.10.0 (ou superior)
- SQLite 3.45.1
- Virtualenv

## Como rodar o projeto?
### 1. Clone o repositório
Para clonar o repositório, você pode rodar esse comando pelo terminal:

```
git clone https://github.com/FGA0138-MDS-Ajax/2024.2-Aries.git
```
### 2. Ative o ambiente virtual
Crie/ative o ambiente virtual com esses comandos:

```
# Para criar o ambiente virtual caso não tenha:
python3 -m venv venv

# Ative-o:
# No Windows:
venv/Scripts/activate

# No Mac/Linux:
source venv/bin/activate
```
### 3. Instale dependências
Acesse o repositório do projeto com o comando:

```
cd 2024.2-Aries
```

Após ativar/criar o ambiente virtual, instale as dependências do projeto executando:

```
pip install -r requirements.txt
```
### 4. Inicie o servidor:
Caminhe até a aplicação do projeto com o comando:

```
cd mamutes
```
Após acessar o app mamutes, execute:

```
python manage.py runserver
```
Acesse a aplicação em <http://127.0.0.1:8000/>.



