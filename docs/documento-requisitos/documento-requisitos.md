# Documento de Requisitos
## 1. Projeto 
Site para a equipe de competição Mamutes do Cerrado.  

## 2. Problema 
<p style="text-align: justify;">
A equipe precisa de uma plataforma centralizada para gerenciar <b>membros, estoques, documentação de voo, registros de reuniões e divulgação de atividades</b>, visando melhorar a eficiência e a organização.
</p>

## 3. Objetivo
### 3.1 Objetivo Geral
<p style="text-align: justify;">
Desenvolver um site que <b>centraliza as operações</b> da equipe, com ferramentas de controle e comunicação para facilitar o <b>gerenciamento de informações, recursos e atividades</b>.
</p>

### 3.2 Objetivos Específicos
<p style="text-align: justify;">
<ul>
<li><b>Páginas de divulgação</b> com história, projetos, informações do processo seletivo e fotos da equipe.  </li>
<li><b>Login com diferentes níveis de acesso</b> (marketing, administração e financeiro).  
<li><b>Controle de estoque</b>.  </li>
<li><b>Documentação de voo e registro de acidentes</b>.  </li>
<li><b>Calendário para organização de tarefas</b>.  </li>
<li><b>Registro de atas e presenças em reuniões</b>.  </li>
<li><b>Espaço de trainees</b>.  </li>
<li><b>Seção de patrocinadores</b>(apenas com logo). </li> 
<li><b>Seção para cases de sucesso</b>.  </li>
<li><b>Seção de FAQ</b>.  </li>
<li><b>Loja virtual</b> (se viável). </li>
</ul> 
</p>

---

## 4. Arquitetura  
A estrutura do sistema deve incluir:

-  **Back-end seguro** para autenticação e controle de dados.  
- **Banco de dados** para gerenciamento das informações.  
- **Front-end responsivo e acessível** para todos os dispositivos.  

---

## 5. Resultados Esperados  
<p style="text-align: justify;">
Disponibilizar uma <b>plataforma completa e intuitiva</b> para gestão da equipe, com funcionalidades que <b>otimizem a logística e a comunicação interna</b>, além de aumentar a <b>visibilidade e o engajamento com o público externo</b>. 
</p> 

---

## Elicitação de Requisitos

### 1. Estrutura Geral e Público-Alvo
- **Público-alvo:**  
    - Membros da equipe (diferentes áreas).  
    - Potenciais patrocinadores.  
    - Interessados no processo seletivo.  
- **Identidade visual:**  
    - Paleta de cores, fontes e ícones padronizados.  
    - Imagens e história da equipe.

---
### 2. Funcionalidades de Divulgação
-  **Conteúdo das páginas:**  
    - História da equipe.  
    - Projetos em andamento.  
    - Quem são os patrocinadores (rodapé).  
- **Aba de trainees:**  
    - Cargos designados por administradores.  
- **Atualizações frequentes:**  
    - Case de sucesso de ex-membros.  

---
### 3. Sistema de Autenticação e Níveis de Acesso
- **Dados coletados no cadastro:**  
    - Cada membro será cadastrado pelo administrador.  
- **Tipos de usuários:**  
    - **Capitão:** SuperUser (acesso total).  
    - **Gerente:** SuperUser (designa tarefas para todas as áreas).  
    - **Líderes:** SuperUser (designa tarefas da própria área).  
    - **Membros:** User (atividades comuns, check em tarefas, etc.).  
    - **Trainees:** User comum.  
-  **Exclusão de contas:**  
    - Apenas administradores podem excluir usuários.  

---
### 4. Controle de Estoque
- **Itens gerenciados:**  
    - Peças de equipamentos, ferramentas, suprimentos.  
- **Informações registradas:**  
    - Nome, código, marca, quantidade, localização, observações.  
- **Relatórios:**  
    - Exportação de documentos em **CSV**.  

---
### 5. Documentação de Voo e Registro de Acidentes
- **Campos do registro de voo:**  
    - Data, nome do piloto, local, membros envolvidos.  
    - Nível de sucesso (5 estrelas).  
    - Objetivo/teste do voo (campo de texto).  
    - Resultados obtidos e melhorias necessárias.  
    - Condições climáticas (vento, pressão atmosférica, peso total).  
    - **Telemetria:** Link para CSV.  
- **Registro de acidentes:**  
    - Data, membros envolvidos, detalhes do acidente.  
    - Código da peça danificada, telemetria, fotos.  
    - Restrito para **membros acima de trainees**.  

---
### 6. Calendário e Organização de Tarefas
- **Eventos registrados:**  
    - Reuniões, tarefas, competições.  
- **Acesso:**  
    - Apenas líderes e cargos superiores podem adicionar eventos.  
- **Kanban:**  
    - Nome do projeto, envolvidos, datas de início e fim.  

---
### 7. Registro de Reuniões e Presenças
- **Registros em formato de formulário**.  
- **Acesso:**  
    - **Editar:** Administração e capitão.  
    - **Visualizar:** Todos os membros.  

---
### 8. Loja Virtual (Se Viável)
- **Produtos vendidos:**  
    - Impressões 3D, chaveiros, camisetas, moletons.  
- **Integração com pagamentos:**  
    - A ser analisada.  
- **Galeria de produtos:**  
    - Links para formulário de compra.  

---
### 9. Arquitetura e Integração
- **Plataformas externas:**  
    - Integração com Google Drive e outras ferramentas, se possível.  

---
## Tabela de Requisitos Funcionais 
<p style="text-align: justify;">
Com base nos requisitos levantados no documento, podemos listá-los como requisitos funcionais com a tabela: 
</p>

<table> <tr> <th>Código</th> <th>Descrição</th> <th>Prioridade</th> </tr> <tr> <td>RF-01</td> <td>Permitir login com diferentes níveis de acesso (admin, financeiro, marketing, membros).</td> <td>Alta</td> </tr> <tr> <td>RF-02</td> <td>Implementar controle de estoque para peças, máquinas e ferramentas.</td> <td>Alta</td> </tr> <tr> <td>RF-03</td> <td>Permitir o cadastro de usuários com permissões específicas.</td> <td>Alta</td> </tr> <tr> <td>RF-04</td> <td>Registrar e documentar voos com informações como data, piloto, velocidade do vento e telemetria.</td> <td>Alta</td> </tr> <tr> <td>RF-05</td> <td>Registrar acidentes e gerar relatórios.</td> <td>Média</td> </tr> <tr> <td>RF-06</td> <td>Permitir o registro de reuniões e atas com presenças.</td> <td>Média</td> </tr> <tr> <td>RF-07</td> <td>Disponibilizar um calendário para organização das tarefas.</td> <td>Média</td> </tr> <tr> <td>RF-08</td> <td>Incluir uma loja virtual para venda de produtos (se viável).</td> <td>Baixa</td> </tr> <tr> <td>RF-09</td> <td>Gerar relatórios em PDF ou CSV sobre estoque, reuniões e atividades.</td> <td>Média</td> </tr> </table>


--- 
## Tabela de Requisitos não Funcionais
<p style="text-align: justify;">
Com base nos requisitos levantados no documento, podemos listá-los como requisitos não funcionais com a tabela: 
</p> 

<table> <tr> <th>Código</th> <th>Descrição</th> <th>Prioridade</th> </tr> <tr> <td>RNF-01</td> <td>O sistema deve ser responsivo e acessível para desktop e mobile.</td> <td>Alta</td> </tr> <tr> <td>RNF-02</td> <td>Deve haver autenticação segura para usuários com níveis de acesso.</td> <td>Alta</td> </tr> <tr> <td>RNF-03</td> <td>Os dados devem ser armazenados de forma segura no banco de dados.</td> <td>Alta</td> </tr> <tr> <td>RNF-04</td> <td>O site deve seguir a identidade visual da equipe Mamutes.</td> <td>Alta</td> </tr> <tr> <td>RNF-05</td> <td>O sistema deve ser capaz de lidar com pelo menos 50 usuários simultâneos.</td> <td>Média</td> </tr> <tr> <td>RNF-06</td> <td>As páginas devem carregar em no máximo 3 segundos.</td> <td>Alta</td> </tr> <tr> <td>RNF-07</td> <td>O sistema deve permitir integração com Google Drive (se possível).</td> <td>Baixa</td> </tr> </table>


--- 
## Prioridades (Negociáveis)
<ol>
<li>Sistema de autenticação;  
<li>Identidade visual;   
<li>Intranet (rastreamento de tarefas);   
<li>Controle de estoque;   
<li>Registro de atas;   
<li>Documentação de voo;   
<li>Calendário;   
<li>Loja virtual;   

</ol>

---
## Tabela de Versionamento

| Versão | Data | Descrição da Alteração | Nome(s) Integrante(s) |
| :----: | :--: | :--------------------: | :-------------------: |
| 1.0 | 09/02/2025 | Criação do documento | Mayara Marques |