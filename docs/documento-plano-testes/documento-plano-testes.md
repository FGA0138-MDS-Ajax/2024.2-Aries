# Plano de Teste

## 1. Introdução

O objetivo deste documento é descrever o plano de testes a ser executado para o projeto **Mamute do cerrado**. Este plano define a estratégia, a abordagem, os recursos necessários e o cronograma de testes para garantir que todos os requisitos do sistema sejam atendidos.

## 2. Objetivos do Teste

- Validar se o sistema atende aos requisitos funcionais e não funcionais.
- Garantir a confiabilidade, performance e segurança do sistema.
- Identificar e corrigir defeitos antes da entrega final.

## 3. Escopo

### 3.1 O que será testado
- Funcionalidade principal do sistema.
- Interação do sistema com outros módulos.
- Performance e carga do sistema.
- Usabilidade e interface com o usuário.
- Segurança (autenticação, autorização).

### 3.2 O que não será testado
- Testes de sistemas de terceiros nã  o integrados diretamente.
- Testes de hardware ou ambiente de produção.

## 4. Requisitos do Sistema

- **Requisitos Funcionais:** 
  - [Requisito 1]
  - [Requisito 2]
  
- **Requisitos Não Funcionais:** 
  - Desempenho mínimo de [x] requisições por segundo.
  - Tempo de resposta inferior a [y] segundos.

## 5. Tipos de Testes

- **Testes funcionais**
  - **Testes Unitários:** Testes de pequenas unidades do código.
  - **Testes de Integração:** Verificação da interação entre diferentes módulos.
  - **Testes de Sistema:** Testes completos para validar a aplicação como um todo.
  - **Testes de Aceitação do Usuário:** Testes realizados pelos stakeholders finais para garantir que o sistema atende às expectativas.

-**Testes não funcionais**
  - **Teste de Performance**
  - **Teste de segurança**


## 6. Estratégia de Teste

- Os testes serão organizados em uma pasta tests, uma única pasta para cada app, e dentro dessa pasta tera outras três pastas cada uma para armazenar um tipo de teste, as pastas de testes serão divididas em:

### Testes Unitários   


| Componente/Funcionalidade              | Descrição do Teste                                                                 | Localização do Teste                             |
|----------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------|
| **Models**                             | Verificar se os métodos do model estão funcionando corretamente.                    | `testes/unitarios/test_models.py`               |
| **Views**                              | Testar se as views estão retornando as respostas corretas (status code, template).  | `testes/unitarios/test_views.py`                |
| **Forms**                              | Verificar se a validação dos formulários está ocorrendo corretamente.               | `testes/unitarios/test_forms.py`                |
| **URLs**                               | Testar se as URLs estão configuradas corretamente e direcionam para as views certas. | `testes/unitarios/test_urls.py`                 |
| **Funções utilitárias**                | Verificar se funções auxiliares estão operando como esperado.                       | `testes/unitarios/test_utils.py`                |


### Testes de Integração

| Componente/Funcionalidade              | Descrição do Teste                                                                 | Localização do Teste                              |
|----------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------|
| **Integração entre Models e Views**    | Verificar se as views interagem corretamente com os models e retornam os dados esperados. | `testes/integracao/test_views_models.py`  |
| **Integração com Banco de Dados**      | Testar se os dados inseridos através das views são corretamente persistidos no banco de dados.|`testes/integracao/test_database_integration.py`|
| **Integração de Formularios com Views**| Testar se o envio de formulários via views resulta na criação ou atualização de dados no banco.|`testes/integracao/test_forms_views.py`|
| **Autenticação e Autorização**         | Testar se os sistemas de login e permissões estão funcionando corretamente.        | `testes/integracao/test_authentication.py`       |
| **Fluxo completo de requisição**       | Verificar o fluxo completo de uma requisição, desde a view até o banco de dados.     | `testes/integracao/test_full_request_flow.py`   |


### Testes de Sistema

| Componente/Funcionalidade              | Descrição do Teste                                                                 | Localização do Teste                              |
|----------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------|
| **Funcionalidade principal**           | Verificar se o sistema como um todo está atendendo aos requisitos funcionais esperados. | `testes/sistema/test_system_functionality.py`|
| **Fluxo completo do usuário**          | Simular o fluxo de ações de um usuário real, incluindo login, navegação e interações. | `testes/sistema/test_user_flow.py`             |
| **Integração com outras APIs**         | Testar a integração com APIs externas ou serviços de terceiros, se aplicável.       | `testes/sistema/test_api_integration.py`         |
| **Testes de UI e Usabilidade**         | Avaliar a interface do usuário para garantir que ela esteja acessível e fácil de usar. | `testes/sistema/test_ui_usability.py`        |
| **Resiliência do Sistema**             | Testar como o sistema reage a falhas simuladas, como queda de serviço ou perda de dados. | `testes/sistema/test_system_resilience.py` |



###  fluxos de execução dos teste
- Os testes unitários são realizados primeiro e serão executados em todos os módulos.
- Após a conclusão dos testes unitários, os testes de integração começam, seguidos pelos testes de sistema.
- A execução de testes de aceitação ocorre depois que os testes funcionais forem validados.

### Registros e Relatórios:

## 7. Ambiente de Teste

- **Configuração do Ambiente de teste:**
A configuração de um ambiente de teste de software envolve várias etapas importantes para garantir que seus testes sejam executados de forma isolada e confiável.
Etapas:
1. Configuração do Ambiente Virtual:
  criação: O primeiro passo foi criar um ambiente virtual isolado usando venv (Python 3). Isso isola as dependências do seu projeto e evita conflitos com outras instalações do Python.
  Instalação de Dependências: foi nescessario instalar o Django e outros pacotes necessários para o projeto, usando o pip.
  unittest e TestCase: O Django usa o módulo unittest do Python como base para os testes.
2. Estrutura do Projeto e Diretório de Testes: 
  Diretório tests/: O Django procura por testes em arquivos chamados tests.py dentro dos app ou em um diretório chamado tests/ que contenha arquivos __init__.py e arquivos de teste (ex: test_models.py, test_views.py). A estrutura tests/ foi escolhida para melhor organização.
3. Banco de Dados de Teste:
  Banco de Dados Separado: O Django automaticamente cria um banco de dados separado para testes, evitando que seus testes modifiquem o banco de dados de desenvolvimento ou produção. Este banco de dados é criado e destruído a cada execução dos testes.
  Configurações: As configurações do banco de dados de teste são definidas no arquivo settings.py. Durante os testes, o Django usa uma cópia dessas configurações com um nome de banco de dados diferente (geralmente com o prefixo test_).
4. Estrutura Básica de Teste Unitário:
  - Definir a classe de teste: A classe de teste herda de TestCase do Django.
  - Métodos de teste: Dentro dessa classe, você define métodos de teste, que são identificados automaticamente por começarem com test_.
  - Asserções: Utiliza métodos como self.assertEqual(), self.assertTrue(), self.assertFalse(), etc., para verificar os resultados esperados.
5.Testes de Integração:
  - Nos testes de integração pretendemos verificar a interação entre modelos e views, como a persistência de dados no banco de dados e o comportamento das respostas HTTP geradas pelas views. Django fornece ferramentas como self.client, self.assertRedirects() e o TestCase, que é uma classe muito útil também para realizar esses testes, especialmente quando se envolve o uso de requisições HTTP e a verificação de dados persistidos no banco de dados.

obs: O planejamento ínicial é fazer os testes na branch teste para mitigar o risco de comprometer o banco de dados ou outras partes importantes do sistema


## 8. Cronograma de Testes

| Data       | Atividade                           | Responsável |
|------------|-------------------------------------|-------------|
| 2025-01-10 | Testes Unitários                    | [Nome]      |
| 2025-01-15 | Testes de Integração                | [Nome]      |
| 2025-01-2 | Testes de Sistema                    | [Nome]      |
| 2025-01-25 | Testes de Aceitação                 | [Nome]      |

## 9. Critérios de Aceitação

Critérios de Aceitação Funcional:
  - Para testes unitários, todos os testes devem passar sem erros de código.
  - Para testes de integração, as interações entre os módulos devem funcionar como esperado (ex: os dados passados entre componentes devem ser corretamente gravados e lidos do banco de dados).
  - Para testes de sistema, a aplicação deve passar em cenários do mundo real e os fluxos dos usuários devem ser validados.

Critérios de Aceitação Não Funcional:
  - Para testes de performance, o sistema deve atender ao tempo de resposta esperado e à carga de requisições sem falhas.
  - Para testes de segurança, as falhas críticas não devem ser encontradas e todas as vulnerabilidades de alto risco devem ser resolvidas.


## 10. Riscos e Mitigações

- **Risco 1:** Falha no ambiente de testes devido à configuração inadequada.
  - **Mitigação:** Garantir que o ambiente de testes esteja preparado com antecedência.
  
- **Risco 2:** Atraso na execução dos testes de integração.
  - **Mitigação:** Definir uma comunicação clara e planos de contingência.

## 11. Aprovação

| Nome               | Cargo         | Assinatura      | Data       |
|--------------------|---------------|-----------------|------------|
| [Nome do Responsável] | [Cargo]      | [Assinatura]    | [Data]     |

