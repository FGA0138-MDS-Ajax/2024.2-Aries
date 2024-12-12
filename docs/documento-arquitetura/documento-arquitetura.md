
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

O sistema da equipe Mamutes do Cerrado adotará a arquitetura em camadas, alinhada ao padrão Model-View-Template (MVT), utilizado pelo framework Django. Essa abordagem organiza o sistema em três componentes principais, cada um com responsabilidades bem definidas:

</div>

### 2.1.1 Camada de Lógica de Negócios (Model)
Essa camada gerencia os dados e a lógica de negócios da aplicação. No contexto do sistema Mamutes, será responsável por:

Armazenar informações sobre membros, estoques, cronogramas e documentos em um banco de dados relacional.
Gerenciar processos internos, como registro de atividades, cálculo de métricas (presenças e disponibilidade de recursos) e controle de acesso.
Fornecer suporte aos relatórios e indicadores de desempenho da equipe.

### 2.1.2 Camada de Apresentação (View)

Os templates são responsáveis pela renderização de conteúdo dinâmico para o usuário, utilizando HTML integrado com variáveis e expressões do Django Template Language (DTL). Exemplos de funcionalidades nesta camada incluem:

Exibição de dashboards com cronogramas, indicadores-chave e relatórios dinâmicos.
Criação de páginas públicas para divulgar eventos, identidade visual e novidades da equipe.
Interfaces amigáveis e responsivas para facilitar o gerenciamento interno de recursos como estoques e cronogramas.

### 2.1.3 Camada de Apresentação (Template)

As views atuam como intermediárias, processando as solicitações dos usuários e interagindo com o Model e o Template. São responsáveis por:

Receber requisições do usuário e retornar respostas adequadas, como páginas HTML ou dados em formato JSON.
Gerenciar lógica de apresentação dinâmica, como filtrar dados de cronogramas ou estoques com base no perfil do usuário.
Integração com APIs externas, como o Google Maps, para funcionalidades avançadas, como cálculo de rotas.
---

## 2.2 Justificativa

<div style="text-align: justify;">

A escolha da arquitetura MVT, fornecida pelo Django, foi motivada por suas diversas vantagens, que se alinham diretamente às necessidades da equipe Mamutes do Cerrado. Entre os principais benefícios, destacam-se:

</div>

### 2.2.1 Separação de Responsabilidades

A arquitetura MVT separa claramente as funções do sistema, o que:

Facilita a manutenção e a evolução independente de cada componente.
Permite alterações no Template (interface do usuário) sem impactar a lógica de negócios no Model.
Simplifica o desenvolvimento contínuo e modular do sistema.

### 2.2.2 Reutilização de Componentes

<div style="text-align: justify;">

A estrutura dos templates do Django permite a reutilização de layouts e blocos de código, agilizando a criação de páginas consistentes e minimizando redundâncias.

</div>

### 2.2.3 Facilidade de Teste

Com o MVT, as camadas podem ser testadas isoladamente:

- Models podem ser validados com testes unitários para garantir a integridade dos dados.
- Views podem ser testadas para confirmar o comportamento esperado das requisições.
- Templates podem ser revisados para verificar se os dados estão sendo apresentados corretamente.

### 2.2.4 Escalabilidade

A arquitetura MVT é flexível e escalável, permitindo que novas funcionalidades sejam adicionadas ou modificadas com facilidade. Isso é crucial para suportar:

- Expansões futuras, como novos módulos para gerenciamento de eventos ou integração com novos sistemas.
- Adaptações às demandas específicas da equipe Mamutes do Cerrado, como melhorias no controle de estoque e comunicação automatizada.

### 2.2.5 Desenvolvimento Paralelo

A separação em camadas permite que diferentes equipes trabalhem simultaneamente:

- Uma equipe pode desenvolver os Models, configurando o banco de dados e regras de negócio.
- Outra pode focar na criação de Templates e no design das páginas.
- Uma terceira equipe pode trabalhar nas Views, integrando os dados e ajustando a lógica de controle.

### 2.2.6 Alinhamento às Necessidades

<div style="text-align: justify;">

A arquitetura MVT atende perfeitamente à necessidade de um sistema robusto, modular e de fácil manutenção, conectando <strong>gestão interna</strong> (estoques, cronogramas, tarefas) e <strong>divulgação externa</strong> (site público, eventos), permitindo que a Mamutes do Cerrado se organize e cresça de forma sustentável e eficiente.

</div>

---

## 2.3 Detalhamento



---

## 2.4 Metas e restrições arquiteturais


---

## 2.5 Visão de Casos de uso


---

## 2.6 Visão lógica


---

## 2.7 Visão de Implementação


---

## 2.8 Visão de Implantação


---

## 2.9 Restrições adicionais


---

# 3. Bibliografia

OiArquitetura MVC e princípios de projeto https://medium.com/@celionormando/arquitetura-mvc-e-princípios-de-projeto-3d0b278ef910 12/12


---


## Tabela de Versionamento

| Versão | Data | Descrição da Alteração | Nome(s) Integrante(s) |
| :----: | :--: | :--------------------: | :-------------------: |
| 1.0 | 25/11/2024 | Criação inicial e estrutura do artefato | Felipe Freire |
| 1.1 | 12/12/2024 | Desenvolvimento dos artefatos de **proposito**, **escopo**, **definições** e **justificativa** | Felipe Freire |