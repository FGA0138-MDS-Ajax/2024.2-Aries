
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

O sistema da equipe <strong>Mamutes do Cerrado</strong> adotará a arquitetura em camadas, alinhada ao padrão <strong>Model-View-Controller (MVC)</strong>, para atender às demandas de gerenciamento interno e divulgação externa. Essa abordagem organiza o sistema em três camadas principais, cada uma com responsabilidades bem definidas: <br>

</div>

### 2.1.1 Camada de Lógica de Negócios (Model)

Essa camada gerencia os dados e a lógica de negócios da aplicação. No contexto do sistema Mamutes, será responsável por: 

- Armazenar informações sobre membros, estoques, cronogramas e documentos;
- Gerenciar os processos de registro de atividades e cálculo de métricas, como presenças e disponibilidade de recursos; 
- Fornecer as bases para relatórios e indicadores de desempenho da equipe.

### 2.1.2 Camada de Apresentação (View)

Responsável pela interface com o usuário, esta camada exibirá os dados de maneira organizada e acessível. Exemplos de funcionalidades nesta camada incluem:

- Exibição de dashboards com cronogramas e indicadores-chave; 
- Páginas públicas para a divulgação da identidade visual e eventos da equipe; 
- Interfaces intuitivas para o gerenciamento de recursos internos, como estoques e tarefas.

### 2.1.3 Camada de Controle (Controller)

<div style="text-align: justify;">

Atuando como intermediária, essa camada processará as solicitações dos usuários, interagindo com o <strong>Model</strong> para acessar ou atualizar dados e definindo como essas informações serão exibidas na <strong>View</strong>. Exemplos incluem: 

</div>

- Controle de login e permissões de acesso para diferentes perfis (administrador, capitão, membro, trainee e visitante); 
- Processamento de entradas de dados para o cadastro de novos membros ou alterações no estoque; 
- Integração com APIs externas. 

---

## 2.2 Justificativa

<div style="text-align: justify;">

A escolha da arquitetura <strong>MVC</strong> foi motivada por suas diversas vantagens, especialmente no contexto da <strong>Mamutes do Cerrado</strong>, que requer um sistema eficiente, modular e de fácil manutenção. Entre os principais benefícios estão:

</div>

### 2.2.1 Separação de Responsabilidades

A divisão em três camadas permite:

- Manutenção independente de cada componente;
- Alterações na interface do usuário (View) sem impactar a lógica de negócios (Model);
- Facilitação do desenvolvimento e aprimoramento contínuo do sistema.

### 2.2.2 Facilidade de Teste

<div style="text-align: justify;">

Com o <strong>MVC</strong>, cada camada pode ser testada de forma isolada, garantindo a identificação rápida de erros e sua resolução eficiente, algo crucial para atender às demandas da equipe.

</div>

### 2.2.3 Escalabilidade

<div style="text-align: justify;">

A arquitetura permite que novas funcionalidades sejam adicionadas sem comprometer o funcionamento do sistema existente. Isso será útil para futuras expansões, como integração com novos sistemas ou adição de novas áreas de gerenciamento.

</div>

### 2.2.4 Desenvolvimento Paralelo

O padrão permite que equipes distintas trabalhem simultaneamente em diferentes partes do sistema, aumentando a eficiência do desenvolvimento. Por exemplo:

- Uma equipe pode se concentrar no desenvolvimento da prototipação das páginas do site;
- Outra pode trabalhar na lógica de negócios para o gerenciamento de estoques.

### 2.2.5 Alinhamento às Necessidades

<div style="text-align: justify;">

Essa arquitetura atende à necessidade de um sistema modular, que conecte <strong>gestão interna</strong> (estoque, cronogramas, tarefas) e <strong>divulgação externa</strong> (site público, eventos), permitindo que a Mamutes do Cerrado cresça e se organize de forma sustentável.

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


---


## Tabela de Versionamento

| Versão | Data | Descrição da Alteração | Nome(s) Integrante(s) |
| :----: | :--: | :--------------------: | :-------------------: |
| 1.0 | 25/11/2024 | Criação inicial e estrutura do artefato | Felipe Freire |
| 1.1 | 12/12/2024 | Desenvolvimento dos artefatos de **proposito**, **escopo**, **definições** e **justificativa** | Felipe Freire |