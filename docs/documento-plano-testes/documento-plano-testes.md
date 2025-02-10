# Plano de Teste

## 1. Introdução

O objetivo deste documento é descrever o plano de testes a ser executado para o projeto **Mamute do cerrado**. Este plano define a estratégia, a abordagem, os recursos necessários e o cronograma de testes para garantir que todos os requisitos do sistema sejam atendidos.

## 2. Objetivos do Teste

- Validar se o sistema atende aos requisitos funcionais e não funcionais.
- Garantir a confiabilidade, performance e segurança do sistema.
- Identificar e corrigir defeitos antes da entrega final.

## 3. Tipos de Testes

- **Testes funcionais**
  - **Testes Unitários:** Testes de pequenas unidades do código.
  - **Testes de Integração:** Verificação da interação entre diferentes módulos.
  - **Testes de Sistema:** Testes completos para validar a aplicação como um todo.
  - **Testes de Aceitação do Usuário:** Testes realizados pelos stakeholders finais para garantir que o sistema atende às expectativas.

-**Testes não funcionais**
  - **Teste de Performance**
  - **Teste de Usabilidade**
  - **Teste de segurança**

## 4 Escopo

### 4.1 O que será testado
- **Funcionalidade principal do sistema** 
  - *Testes Unitários*
    - Testar os métodos dos Models
    - Testar as Views
    - Testar a validação dos Forms
    - Testar o mapeamento das URLs para as Views.
    - Testar as funções utilitárias.
  - *Testes de Integração*
    - Testar a interação entre Models e Views.
    - Testar a persistência de dados no banco de dados.
    - Testar o processamento de formulários através das Views.
    - Testar os mecanismos de Autenticação e Autorização
    - Testar o fluxo completo de uma requisição HTTP  (desde a URL até o banco de dados e a resposta).
  - *Testes de Sistema*
    - Testar os fluxos de usuário ponta a ponta
    - Testes de UI e Usabilidade
    - Testar a resiliência do sistema a falhas
  - *Testes de Aceitação do Usuário (UAT)*
    - Validar se o sistema atende às expectativas dos usuários finais em cenários de uso.
- **Performance e carga do sistema:**
  - Testar o tempo de resposta do sistema sob diferentes cargas de usuários.
  - Testar a capacidade do sistema de lidar com picos de tráfego.
  - Testar o consumo de recursos (CPU, memória) sob diferentes cargas.
- **Usabilidade e interface com o usuário.**
  - Testar a facilidade de uso da interface. 
  - Testar a responsividade da interface em diferentes dispositivos 
- **Segurança.**
  - Testar a segurança da autenticação.
  - Testar a autorização
  - Testar vulnerabilidades comuns de segurança web

### 4.2 O que não será testado
- Testes de sistemas de terceiros não integrados diretamente.
- Testes de hardware ou ambiente de produção.


## 5. Estratégia de Teste

### Organização Dos testes:

- Os testes serão organizados em uma pasta tests, com uma única subpasta para cada app. Dentro dessa subpasta, haverá outras três pastas, cada uma destinada a armazenar um tipo de teste. As pastas de testes serão divididas conforme exemplificado na tabela abaixo. No entanto, dependendo do tamanho de cada app ou da completude de cada arquivo de teste, as pastas de testes podem conter menos arquivos:

- Testes Unitários  

| Componente/Funcionalidade              | Descrição do Teste                                                                 | Localização do Teste                             |
|----------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------|
| **Models**                             | Verificar se os métodos do model estão funcionando corretamente.                    | `testes/unitarios/test_models.py`               |
| **Views**                              | Testar se as views estão retornando as respostas corretas (status code, template).  | `testes/unitarios/test_views.py`                |
| **Forms**                              | Verificar se a validação dos formulários está ocorrendo corretamente.               | `testes/unitarios/test_forms.py`                |
| **URLs**                               | Testar se as URLs estão configuradas corretamente e direcionam para as views certas. | `testes/unitarios/test_urls.py`                 |
| **Funções utilitárias**                | Verificar se funções auxiliares estão operando como esperado.                       | `testes/unitarios/test_utils.py`                |


- Testes de Integração

| Componente/Funcionalidade              | Descrição do Teste                                                                 | Localização do Teste                              |
|----------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------|
| **Integração entre Models, Views e forms**    | Verificar se as views interagem corretamente com os models e forms e retornam os dados esperados. | `testes/integracao/test_views_models.py`  |
| **Integração com Banco de Dados**      | Testar se os dados inseridos através das views são corretamente persistidos no banco de dados.|`testes/integracao/test_database_integration.py`|


- Testes de Sistema

| Componente/Funcionalidade              | Descrição do Teste                                                                 | Localização do Teste                              |
|----------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------|
| **Fluxo completo do usuário**          | Simular o fluxo de ações de um usuário real, incluindo login, navegação e interações. | `testes/sistema/test_user_flow.py`             |
| **Testes de UI e Usabilidade**         | Avaliar a interface do usuário para garantir que ela esteja acessível e fácil de usar. | `testes/sistema/test_ui_usability.py`        |


###  fluxos de execução dos teste
- Os testes unitários são realizados primeiro e serão executados em todos os módulos.
- Após a conclusão dos testes unitários, os testes de integração começam, seguidos pelos testes de sistema.
- A execução de testes de aceitação ocorre depois que os testes funcionais forem validados.

### Arquivação dos testes

- A documentação dos testes será consolidada em um arquivo específico, onde cada teste será detalhado, incluindo sua descrição/objetivo, e resultados esperados. Essa prática assegura uma compreensão clara do propósito de cada teste e dos critérios de sucesso, facilitando a identificação de falhas e garantindo que o software atenda aos requisitos estabelecidos. Além disso, uma documentação bem estruturada promove a rastreabilidade e a colaboração entre as equipes de desenvolvimento e teste, servindo como referência para futuras manutenções e melhorias no sistema.

### Outras formas de testes:

- Após a identificação de um problema, o código é modificado e os testes são repetidos até que apresentem os resultados esperados. Além disso, uma parte significativa dos testes é realizada por meio de abordagens conhecidas como testes exploratórios.

- Os testes exploratórios são uma abordagem de teste de software que enfatiza a aprendizagem simultânea, o design e a execução dos testes. Nessa metodologia, os testadores exploram o sistema de forma dinâmica, adaptando suas estratégias conforme descobrem comportamentos inesperados ou áreas de risco. Essa flexibilidade permite a identificação de defeitos que podem não ser detectados por testes tradicionais baseados em scripts. 

- Ao adotar os testes exploratórios, a equipe de desenvolvimento assegura que os problemas sejam identificados e corrigidos de maneira proativa, contribuindo para a qualidade e a estabilidade do software.

## 7. Ambiente de Teste

- **Configuração do Ambiente de teste:**
A configuração de um ambiente de teste de software envolve várias etapas importantes para garantir que os testes sejam executados de forma isolada e confiável.
Etapas:
1. Configuração do Ambiente Virtual:
  criação: O primeiro passo é criar um ambiente virtual isolado usando venv (Python 3). Isso isola as dependências do projeto e evita conflitos com outras instalações do Python.
  Instalação de Dependências: nescessario instalar o Django e outros pacotes necessários para o projeto, usando o pip.
  unittest e TestCase: Modulos príncipais do Django usados para os testes.
2. Estrutura do Diretório de Testes: 
  Diretório tests/: O Django procura por testes em arquivos chamados tests.py dentro dos app ou em um diretório chamado tests/ que contenha arquivos __init__.py e arquivos de teste (ex: test_models.py, test_views.py). A estrutura tests/ foi escolhida para melhor organização.
3. Banco de Dados de Teste:
  Banco de Dados Separados: O Django automaticamente cria um banco de dados separado para testes, evitando que seus testes modifiquem o banco de dados de desenvolvimento ou produção. Este banco de dados é criado e destruído a cada execução dos testes.
  Configurações: As configurações do banco de dados de teste são definidas no arquivo settings.py. Durante os testes, o Django usa uma cópia dessas configurações com um nome de banco de dados diferente.
4. Estrutura Básica de Teste Unitário:
  - Definir a classe de teste: A classe de teste herda de TestCase do Django.
  - Métodos de teste: Dentro dessa classe, definiremos métodos de teste, que são identificados automaticamente por começarem com test_.
  - Asserções: Utiliza métodos como self.assertEqual(), self.assertTrue(), self.assertFalse(), etc., para verificar os resultados esperados.
5.Testes de Integração:
  - Nos testes de integração pretend

obs: O planejamento ínicial é fazer os testes na branch teste para mitigar o risco de comprometer o banco de dados ou outras partes importantes do sistemaemos verificar a interação entre modelos e views, como a persistência de dados no banco de dados e o comportamento das respostas HTTP geradas pelas views. Django fornece ferramentas como self.client, self.assertRedirects() e o TestCase, que é uma classe muito útil também para realizar testes que envolve o uso de requisições HTTP e a verificação de dados no banco de dados.


## 8. Cronograma de Testes

| Data       | Atividade                           | Responsável |
|------------|-------------------------------------|-------------|
| 2025-01-10 | Testes Unitários                    | Equipe      |
| 2025-01-15 | Testes de Integração                | Equipe      |
| 2025-02-04 | Testes de Sistema                   | Equipe      |
| 2025-02-08 | Testes de Aceitação                 | Equipe      |

## 9. Critérios de Aceitação

Critérios de Aceitação Funcional:
  - Para testes unitários, todos os testes devem passar sem erros de código.
  - Para testes de integração, as interações entre os módulos devem funcionar como esperado, os dados passados entre componentes devem ser corretamente gravados e lidos do banco de dados.
  - Para testes de sistema, a aplicação deve passar em cenários do mundo real e os fluxos dos usuários devem ser validados.

Critérios de Aceitação Não Funcional:
  - Para testes de performance, o sistema deve atender ao tempo de resposta esperado e à carga de requisições sem falhas.
  - Para testes de segurança, as falhas críticas não devem ser encontradas e todas as vulnerabilidades de alto risco devem ser resolvidas.


## 10. Riscos e Mitigações

- **Risco 1:** Falha no ambiente de testes devido à configuração inadequada.
  - *Mitigação:* Garantir que o ambiente de testes esteja preparado com antecedência.
  
- **Risco 2:** Atraso na execução dos testes de integração.
  - *Mitigação:* Definir uma comunicação clara e planos de contingência.

## 11. Tabela de Versionamento

| Versão | Data | Descrição da Alteração | Nome(s) Integrante(s) |
| :----: | :--: | :--------------------: | :-------------------: |
| 1.0 | 09/02/2025 | Desenvolvimento do plano de testes  | Felipe Duarte |
| 1.1 | 09/02/2025 | Revisão do Documento| Felipe Freire |
