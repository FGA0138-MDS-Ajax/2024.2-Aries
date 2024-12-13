
# 1. Introdução

## 1.1 Propósito

<div style="text-align: justify;">

Este documento apresenta a arquitetura do sistema desenvolvido para o sistema web para a equipe de competição Mamutes do Cerrado da Universidade de Brasília (UnB). O objetivo é descrever detalhadamente as funcionalidades, integrações e especificações técnicas, fornecendo uma visão abrangente para desenvolvedores, testadores e demais envolvidos no projeto. O sistema busca aprimorar a gestão interna e aumentar a visibilidade externa da equipe, alinhando-se às suas necessidades e objetivos estratégicos. <br> <br>

</div>

---

## 1.2 Escopo

<div style="text-align: justify;">

O sistema desenvolvido para os Mamutes do Cerrado busca melhorar a organização interna da equipe e aumentar sua visibilidade externa. Ele contará com ferramentas para gerenciar calendários, inventário, documentos e tarefas, além de oferecer perfis de acesso personalizados para diferentes membros. <br> <br>
Também terá um site público para divulgar a equipe, suas conquistas, projetos e informações sobre o processo seletivo. Internamente, o sistema inclui funcionalidades de comunicação automatizada e registro de dados importantes, como voos e acidentes. <br> <br>
Com isso, o objetivo é otimizar processos, centralizar informações e destacar a equipe em competições e no meio acadêmico.
Demais detalhes com relação ao escopo do projeto, se encontram no documento “Documento de Visão - Aries”, na seção 4.

</div>

---

# 2. Representação Arquitetural

## 2.1 Definições

<div style="text-align: justify;">

O sistema da equipe Mamutes do Cerrado adotará a arquitetura em camadas, alinhada ao padrão Model-View-Template (MVT), utilizado pelo framework Django. Essa abordagem organiza o sistema em três componentes principais, cada um com funções bem definidas.

</div>

---

## 2.2 Justificativa

<div style="text-align: justify;">

A escolha da arquitetura MVT, fornecida pelo Django, foi motivada por suas diversas vantagens, que se alinham diretamente às necessidades do desenvolvimento do sistema Web. Entre os principais benefícios, destacam-se:

</div>

### 2.2.1 Separação de Responsabilidades

<div style="text-align: justify;">

A arquitetura MVT separa claramente as funções do sistema, o que:

</div>

- Facilita a manutenção e a evolução independente de cada componente.
- Permite alterações no Template (interface do usuário) sem impactar a lógica de negócios no Model.
- Simplifica o desenvolvimento contínuo e modular do sistema.

### 2.2.2 Reutilização de Componentes

<div style="text-align: justify;">

A estrutura dos templates do Django permite a reutilização de layouts e blocos de código, agilizando a criação de páginas consistentes e minimizando redundâncias.

</div>

### 2.2.3 Facilidade de Teste

<div style="text-align: justify;">

Com o MVT, as camadas podem ser testadas isoladamente:

</div>

- Models podem ser validados com testes unitários para garantir a integridade dos dados.
- Views podem ser testadas para confirmar o comportamento esperado das requisições.
- Templates podem ser revisados para verificar se os dados estão sendo apresentados corretamente.

### 2.2.4 Desenvolvimento Paralelo

<div style="text-align: justify;">

A separação em camadas permite que diferentes equipes trabalhem simultaneamente:

</div>

- Uma equipe pode desenvolver os Models, configurando o banco de dados e regras de negócio.
- Outra pode focar na criação de Templates e no design das páginas.
- Uma terceira equipe pode trabalhar nas Views, integrando os dados e ajustando a lógica de controle.

### 2.2.5 Escalabilidade e Adaptação

<div style="text-align: justify;">

A arquitetura MVT é flexível e escalável, permitindo que novas funcionalidades sejam adicionadas ou modificadas com facilidade. Isso é crucial para suportar:

</div>

- Expansões futuras, como novos módulos para gerenciamento de eventos ou integração com novos sistemas.
- Adaptações às demandas específicas da equipe Mamutes do Cerrado, como melhorias no controle de estoque e comunicação automatizada.

### 2.2.6 Alinhamento às Necessidades

<div style="text-align: justify;">

A arquitetura MVT atende perfeitamente à necessidade de um sistema robusto, modular e de fácil manutenção, conectando <strong>gestão interna</strong> (estoques, cronogramas, tarefas) e <strong>divulgação externa</strong> (site público, eventos), permitindo que a Mamutes do Cerrado se organize e cresça de forma sustentável e eficiente.

</div>

---

## 3 Detalhamento

<div style="text-align: justify;">

O padrão arquitetural utilizado será em camadas, implementado com o framework Django, seguindo o design <strong>Model-View-Template (MVT)</strong>. Cada componente do MVT desempenhará funções específicas, assegurando as vantagens descritas no item 2.2 deste documento. Abaixo, detalha-se o papel de cada camada no sistema da equipe:

</div>

## 3.1 Camada de Lógica de Negócios (Model)

<div style="text-align: justify;">

Essa camada gerencia os dados e a lógica de negócios da aplicação. No contexto do sistema Mamutes, será responsável por:

</div>

- Armazenar informações sobre membros, estoques, cronogramas e documentos em um banco de dados relacional.
- Gerenciar processos internos, como registro de atividades, cálculo de métricas (presenças e disponibilidade de recursos) e controle de acesso.
- Fornecer suporte aos relatórios e indicadores de desempenho da equipe.

## 3.2 Camada de Apresentação (Template)

<div style="text-align: justify;">

Os templates são responsáveis pela renderização de conteúdo dinâmico para o usuário, utilizando HTML integrado com variáveis e expressões do Django Template Language (DTL). Exemplos de funcionalidades nesta camada incluem:

</div>

- Exibição de dashboards com cronogramas, indicadores-chave e relatórios dinâmicos.
- Criação de páginas públicas para divulgar eventos, identidade visual e novidades da equipe.
- Interfaces amigáveis e responsivas para facilitar o gerenciamento interno de recursos como estoques e cronogramas.

## 3.3 Camada de Controle (View)

<div style="text-align: justify;">

As views atuam como intermediárias, processando as solicitações dos usuários e interagindo com o Model e o Template. São responsáveis por:

</div>

- Receber requisições do usuário e retornar respostas adequadas, como páginas HTML ou dados em formato JSON.
- Gerenciar lógica de apresentação dinâmica, como filtrar dados de cronogramas ou estoques com base no perfil do usuário.
- Integração com APIs externas, como o Google Maps, para funcionalidades avançadas, como cálculo de rotas.	

## 3.4 Benefícios do Padrão MVT no Contexto do Sistema

- Organização Modular: Cada camada desempenha um papel distinto, facilitando manutenção e futuras expansões.
- Reutilização e Consistência: Templates reutilizáveis para páginas públicas e privadas garantem consistência visual.
- Escalabilidade: Novas funcionalidades podem ser integradas sem grandes reestruturações.
- Desenvolvimento Colaborativo: Permite que diferentes equipes trabalhem simultaneamente nas três camadas, otimizando o tempo de desenvolvimento.

A figura abaixo ilustra a arquitetura MVT utilizada no desenvolvimento do sistema Mamutes do Cerrado, destacando a interação entre os componentes e suas responsabilidades:

![Esquema MVT](https://raw.githubusercontent.com/FGA0138-MDS-Ajax/2024.2-Aries/refs/heads/main/docs/view/img/mvt.png)

<div style="text-align: justify;">

Figura 1. Esquema da arquitetura MVT adaptada ao sistema Mamutes do Cerrado

</div>

---

## 4 Metas e restrições arquiteturais

## Metas Arquiteturais

<div style="text-align: justify;">

As metas arquiteturais do nosso sistema foram definidas para atender às necessidades funcionais e não funcionais da aplicação, garantindo eficiência, segurança e escalabilidade:

</div>

### 4.1 Tempo de Resposta

<div style="text-align: justify;">

O sistema deve responder a 95% das consultas de usuários em até 2 segundos para garantir uma experiência fluida. <br>

Justificativa: Tempos de resposta rápidos são essenciais para o uso eficiente do sistema, especialmente em situações de alta demanda, como o acesso simultâneo por diversos membros da equipe.

</div>

### 4.2 Padrão de API

<div style="text-align: justify;">

Todas as APIs do sistema devem seguir o padrão RESTful, implementando autenticação com tokens JWT para maior segurança.<br>

Justificativa: O padrão RESTful é amplamente adotado e facilita a interoperabilidade com sistemas externos, enquanto a autenticação JWT garante segurança em comunicações de dados sensíveis.

</div>

### 4.3 Escalabilidade Horizontal

<div style="text-align: justify;">

O sistema deve suportar a adição de servidores para aumentar a capacidade de processamento em cenários de crescimento da equipe ou de dados.<br>

Justificativa: Escalabilidade horizontal garante que o sistema possa crescer sem a necessidade de reformulações arquiteturais.

</div>

### 4.4 Manutenibilidade Modular

<div style="text-align: justify;">

Novas funcionalidades devem ser integradas ao sistema sem impactar componentes existentes, graças à separação de responsabilidades proporcionada pelo padrão MVT.<br>

Justificativa: A arquitetura modular simplifica a adição de novos recursos e facilita correções de erros ou atualizações de componentes.

</div>

### 4.5 Segurança de Dados

<div style="text-align: justify;">

Os dados sensíveis dos membros e da gestão de recursos devem ser armazenados de forma criptografada, com suporte a TLS 1.2 ou superior para comunicações seguras.<br>

Justificativa: Proteção de dados é essencial para evitar vazamentos e garantir a conformidade com regulamentações como a LGPD (Lei Geral de Proteção de Dados).
Restrições Arquiteturais

</div>

## Restrições Arquiteturais

### 4.6  Compatibilidade Multiplataforma

<div style="text-align: justify;">

O sistema deve ser compatível com navegadores modernos (Chrome, Firefox, Edge, Safari) e dispositivos móveis com tela mínima de 5 polegadas.<br>

Justificativa: Garantir o acesso universal é essencial para que todos os membros possam usar o sistema sem barreiras tecnológicas.

</div>

### 4.7 Uso do Framework Django

<div style="text-align: justify;">

Todo o desenvolvimento backend será baseado no Django 4.2 LTS, incluindo o suporte ao padrão MVT e ORM nativo.<br>

Justificativa: O Django é robusto, oferece ferramentas integradas para desenvolvimento ágil e segue boas práticas de segurança e escalabilidade.

</div>

### 4.8 Armazenamento e Banco de Dados

<div style="text-align: justify;">

O sistema deve utilizar --- como banco de dados principal, com suporte a armazenamento de até 1 TB de dados no primeiro ano.<br>

Justificativa: --- oferece alto desempenho e suporte para operações complexas, além de ser escalável e compatível com o Django.

</div>

---

## 5 Visão de Casos de uso


---

## 6 Visão lógica


---

## 7 Visão de Implementação


---

## 8 Visão de Implantação


---

## 9 Restrições adicionais


---

# 10. Bibliografia

OiArquitetura MVC e princípios de projeto https://medium.com/@celionormando/arquitetura-mvc-e-princípios-de-projeto-3d0b278ef910 12/12


---

## Tabela de Versionamento

| Versão | Data | Descrição da Alteração | Nome(s) Integrante(s) |
| :----: | :--: | :--------------------: | :-------------------: |
| 1.0 | 25/11/2024 | Criação inicial e estrutura do artefato | Felipe Freire |
| 1.1 | 12/12/2024 | Desenvolvimento dos artefatos de **proposito**, **escopo**, **definições**, **justificativa**, **detalhamento** e **metas e restrições arquiteturais** | Felipe Freire |