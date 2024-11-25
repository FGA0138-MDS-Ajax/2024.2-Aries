
# Visão do Produto e Projeto

Este documento será usado como guia para registrar as informações gerais do produto e projeto. Ele será refinado e atualizado ao longo do ciclo de vida do desenvolvimento, conforme o padrão ABNT para documentos técnicos.

---

## Problema

### Contexto do Problema
A equipe de competição **Mamutes do Cerrado**, da Universidade de Brasília (UnB) - FCTE, enfrenta desafios significativos em dois pilares centrais: **divulgação externa** e **gestão interna**. Como uma equipe acadêmica e técnica que busca representar a instituição em competições de alto nível, é crucial manter uma forte presença pública para atrair novos membros, patrocinadores e reconhecimento institucional. Simultaneamente, a organização interna é essencial para otimizar processos, garantir transparência e alcançar um desempenho competitivo.

Atualmente, a equipe carece de ferramentas integradas que unifiquem a gestão de seus recursos (como estoque e finanças), tarefas (calendários e reuniões) e documentos essenciais.

### Problema Encontrado
O principal problema enfrentado pelos **Mamutes do Cerrado** é a falta de uma **plataforma centralizada** que conecte as necessidades de **divulgação externa** e **gestão interna**. Isso resulta em:
- **Baixa visibilidade externa**: Falta de uma identidade visual unificada e dificuldade em atrair novos membros e patrocinadores.
- **Desorganização interna**: A ausência de ferramentas adequadas para gerenciar tarefas, compromissos, recursos materiais e financeiros gera atrasos, retrabalho e perda de eficiência.
- **Risco de perda de informações**: O armazenamento descentralizado de documentos e atas compromete a transparência e dificulta o acesso às informações essenciais.

A necessidade de um software surge como uma oportunidade de resolver esses gargalos, otimizando processos internos e fortalecendo a presença externa da equipe.

### Diagrama de Ishikawa (Espinha de Peixe)
O diagrama abaixo identifica as causas do problema central: **Ineficiência na gestão e divulgação da equipe**.

**Problema Central:** Ineficiência na gestão e divulgação  
1. **Pessoas**: Falta de integração entre os membros; dificuldade em acompanhar tarefas e reuniões.  
2. **Processos**: Gestão manual ou uso de ferramentas dispersas; ausência de um padrão de operação.  
3. **Tecnologia**: Inexistência de uma plataforma única e dedicada às necessidades específicas da equipe.  
4. **Finanças**: Controle inadequado de entradas e saídas financeiras, dificultando o planejamento.  
5. **Comunicação**: Divulgação fragmentada, impactando o alcance do público-alvo e a captação de recursos.

(Diagrama visual pode ser incluído aqui com as categorias listadas acima conectadas ao problema central.)

### Solução Proposta
A solução sugerida é o desenvolvimento de um **aplicativo web unificado**, que aborde as duas dimensões centrais do problema:
1. **Divulgação Externa**: Uma página inicial atraente e funcional, destacando a identidade visual dos Mamutes do Cerrado, informações sobre os integrantes, competições e o processo seletivo.
2. **Gestão Interna**: Módulos dedicados para:
   - **Calendário e Tarefas**: Organização visual das atividades com quadro Kanban e calendário consolidado.
   - **Estoque**: Controle preciso de materiais e peças.
   - **Reuniões**: Registro de atas e controle de presença.
   - **Documentos**: Centralização e fácil acesso a arquivos importantes.
   - **Finanças**: Rastreamento de entradas e saídas financeiras, garantindo maior planejamento.

### Justificativa da Solução
O aplicativo proposto oferece uma abordagem centralizada, promovendo:
- **Eficiência operacional**: Reduzindo o tempo gasto em tarefas administrativas e possibilitando maior foco nas atividades das competições.
- **Transparência e organização**: Com dados centralizados e acessíveis aos membros.
- **Engajamento externo**: Aumentando a visibilidade da equipe e atraindo talentos e recursos estratégicos.

Espera-se que a solução não só resolva os problemas atuais, mas também proporcione um ambiente mais estruturado e motivador para os integrantes, contribuindo diretamente para o sucesso da equipe.

---

### Declaração de Posição do Produto

| **Para**       | Mamutes do Cerrado           |
|---------|--------------------------------|
| **Necessidade**       | Centralizar a gestão e melhorar a visibilidade da equipe. |
| **O Produto**       | Uma aplicação web chamada *Mamutes Gestão*.     | 
| **Que**       | Oferece ferramentas de organização interna e divulgação externa.     | 
| **Ao Contrário**       | De soluções dispersas ou inexistentes.     | 
| **Nosso Produto**       | Integra gestão e divulgação em um único ambiente acessível.     | 

---

### Objetivos do Produto
- **Principal**: Otimizar a gestão interna e fortalecer a presença externa da equipe.  
- **Secundários**: 
  - Automatizar tarefas administrativas.  
  - Facilitar a comunicação interna e externa.  
  - Garantir acessibilidade aos documentos e recursos da equipe.  

---

### Tecnologias a Serem Utilizadas

- **Linguagem**: Python  
- **Framework**: Django  
- **Banco de Dados**: MySQL  
- **Front-End**: HTML, CSS, Bootstrap  
- **Ferramentas**: Visual Studio Code, Astah, Git e GitHub  
- **Metodologia**: Scrum e XP  

---

## Visão Geral do Projeto

### Ciclo de Vida do Projeto
O desenvolvimento será dividido em sprints, com entregas claras e incrementais:  

| Sprint  | Produto (Entrega)              | Data Início  | Data Fim      | % Conclusão |
|---------|--------------------------------|--------------|---------------|-------------|
| 1       | Definição do Produto           | dd/mm/aaaa   | dd/mm/aaaa    | 0%          |
| 2       | MVP e Planejamento do Projeto  | dd/mm/aaaa   | dd/mm/aaaa    | 0%          |
| 3       | Funcionalidades A, B, C, D     | dd/mm/aaaa   | dd/mm/aaaa    | 0%          |

---

### Organização do Projeto
| Papel                | Atribuições                                                 | Responsáveis                |
|----------------------|------------------------------------------------------------|-----------------------------|
| **Cliente**          | Fornecer feedback e acompanhar o progresso                 | Equipe Mamutes              |
| **Scrum Master**  | Atualizar escopo e validar entregas                        | Caio Duarte    |
| **Líderes de Squad**    |                       |    |
| **Desenvolvedores**    | Codificar e realizar implementações                      |    |
| **Analistas de Qualidade** | Garantir qualidade e execuctar testes de software                   |   |


---

### Planejamento das Fases
As fases serão detalhadas e adaptadas em cada sprint, com priorização do backlog.  

---

### Matriz de Comunicação
| Descrição                             | Área/Envolvidos      | Periodicidade | Produtos Gerados              |
|---------------------------------------|----------------------|---------------|--------------------------------|
| Acompanhamento das Atividades         | Equipe do Projeto    | Semanal       | Ata de Reunião, Relatório      |
| Situação do Projeto                   | Equipe/Prof/Monitor  | Quinzenal     | Relatório de Situação          |

---

## Gerenciamento de Riscos
| Risco                      | Grau de Exposição | Mitigação                    | Plano de Contingência          |
|----------------------------|-------------------|------------------------------|--------------------------------|
| Atrasos no cronograma      | Alto              | Reorganização do backlog     | Redistribuir tarefas           |
| Perda de dados             | Médio             | Backup semanal               | Recuperação de backups         |

---

## Processo de Desenvolvimento de Software
O processo seguirá metodologias ágeis (Scrum e XP), com fluxos organizados de atividades para garantir eficiência e colaboração.

---

## Declaração de Escopo do Projeto

**Backlog do Produto**:  
- Requisitos obrigatórios (*Must*): Módulos de gestão e divulgação.  
- Requisitos desejáveis (*Should/Could*): Customização e integração com redes sociais.  

| Cenário   | Requisito       | Sprint | Priorização | Tipo de Requisito   | Descrição                    |
|-----------|-----------------|--------|-------------|---------------------|------------------------------|
| Gestão    | Calendário      | 2      | Must        | Funcional           | Gerenciamento de tarefas     |
| Divulgação| Página inicial  | 1      | Must        | Funcional           | Apresentar a equipe          |

---

## Tabela de Versionamento

| Versão | Data | Descrição da Alteração | Nome(s) Integrante(s) |
| :----: | :--: | :--------------------: | :-------------------: |
| 1.0 | 25/11/2024 | Criação inicial e estrutura do artefato | Felipe Freire |
| 1.0 | 25/11/2024 | Desenvolvimento do artefato **contexto do problema**, **declaração do produto**, **objetivo do produto** e **tecnologias a serem utilizadas**   | Felipe Freire |