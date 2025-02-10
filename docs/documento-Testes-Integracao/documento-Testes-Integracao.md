# Relatorios de testes de integração
---

## APP USERS 

| **Teste**                            | **Descrição**                                                                                               | **Resultado Esperado**                                                                                                                     |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **test_login_get**                   | Testa a renderização da página de login.                                                                     | A página de login deve ser carregada com status 200 e usar o template `login.html`.                                                      |
| **test_login_post_success**          | Testa o login com sucesso.                                                                                   | O usuário deve ser redirecionado para a página `home`.                                                                                     |
| **test_login_post_failure**          | Testa o login com falha.                                                                                     | A página de login deve ser recarregada com status 200 e o template `login.html` deve ser usado.                                           |
| **test_register_get**                | Testa a renderização da página de cadastro para superusuário.                                                | A página de registro deve ser carregada com status 200 e usar o template `register.html`.                                                  |
| **test_register_post_success**       | Testa o envio do formulário de registro com dados válidos.                                                  | O usuário deve ser criado e a resposta deve ter status 200, indicando sucesso no envio do formulário.                                      |
| **test_register_post_failure**       | Testa o envio do formulário de registro com dados inválidos.                                                | A página de erro deve ser renderizada com status 200 e nenhum usuário deve ser criado.                                                    |
| **test_recover_account_post_success**| Testa a recuperação de conta com sucesso.                                                                   | Um email de recuperação deve ser enviado para o usuário e a resposta JSON deve indicar sucesso com a mensagem apropriada.                   |
| **test_recover_account_post_failure**| Testa a recuperação de conta com falha.                                                                     | A resposta JSON deve indicar erro, com a mensagem de que o email não existe no sistema.                                                     |
| **test_edit_user_get**               | Testa a renderização da página de edição de usuário.                                                        | A página de edição deve ser carregada com status 200 e usar o template `pagConfig.html`.                                                   |
| **test_edit_user_post**              | Testa o envio do formulário de edição de usuário.                                                            | As informações do usuário devem ser atualizadas corretamente e o usuário deve ser redirecionado para a página `pagConfig`.                  |

---

## APP STOCK

| **Teste**                             | **Descrição**                                                                                           | **Resultado Esperado**                                                                                                                    |
|---------------------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **test_adicionar_ferramenta**         | Testa a adição de uma ferramenta no estoque.                                                            | A ferramenta deve ser adicionada ao banco de dados, o número de ferramentas deve ser 2, e o redirecionamento para `stock` deve ocorrer. |
| **test_editar_ferramenta**            | Testa a edição de uma ferramenta existente.                                                              | A ferramenta deve ser editada no banco de dados, com o nome alterado para "Martelo de Borracha", e redirecionamento deve ocorrer.       |
| **test_deletar_ferramenta**           | Testa a exclusão de uma ferramenta do estoque.                                                           | A ferramenta deve ser deletada do banco de dados, e o número de ferramentas deve ser 0.                                                  |
| **test_download_pdf**                 | Testa o download do estoque em formato PDF.                                                              | O conteúdo da resposta deve ser do tipo `application/pdf` e o status da resposta deve ser 200.                                          |
| **test_download_csv**                 | Testa o download do estoque em formato CSV.                                                              | O conteúdo da resposta deve ser do tipo `text/csv` e o status da resposta deve ser 200.                                                  |

---

## APP GUEST

| **Teste**                                           | **Descrição**                                                                                                      | **Resultado Esperado**                                                                                                                           |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **test_admission_view_creates_state_if_none_exists** | Testa se um estado de admissão é criado automaticamente caso não exista nenhum.                                     | A resposta deve ser 200, um estado de admissão deve ser criado, e o campo `is_open` deve ser `True`.                                              |
| **test_admission_view_existing_state**              | Testa a visualização de um estado de admissão já existente.                                                        | A resposta deve ser 200, e a página deve conter o link de admissão "http://example.com".                                                        |
| **test_admission_state_model_str**                  | Testa a representação em string do modelo `AdmissionState`.                                                         | A representação deve ser "Aberto" quando `is_open` for `True`, e "Fechado" quando `is_open` for `False`.                                         |
| **test_admin_admission_state_display**              | Testa a exibição do link de admissão no modelo `AdmissionState`.                                                    | O estado de admissão recuperado deve ter o link "http://example.com".                                                                            |

---

## APP MEMBERS

| **Nome do Teste**             | **Descrição**                                                                                                           | **Resultado Esperado**                             |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| `test_create_task`             | Testa a criação de uma tarefa usando o formulário `TaskForm`. Verifica se o formulário é válido e se a tarefa criada tem o título correto e está associada ao membro responsável. | O formulário deve ser válido e a tarefa criada deve ter o título "Nova Tarefa" e o membro responsável associado. |
| `test_create_event`            | Testa a criação de um evento usando o formulário `EventForm`. Verifica se o formulário é válido, salva o evento corretamente e associa o evento ao membro. | O formulário deve ser válido e o evento criado deve ter o título "Novo Evento" e o membro associado. |
| `test_task_view`               | Testa a view `taskBoard`. Verifica se ela responde corretamente (status 200) e se contém o nome da tarefa criada.  | A view deve responder com status 200 e exibir a tarefa "Teste". |
| `test_event_view`              | Testa a view `home`. Verifica se ela responde corretamente (status 200) e se contém o título do evento criado. | A view deve responder com status 200 e exibir o evento "Evento Teste". |

---

## Tabela de Versionamento

| Versão | Data | Descrição da Alteração | Nome(s) Integrante(s) |
| :----: | :--: | :--------------------: | :-------------------: |
| 1.0 | 09/02/2025 | Desenvolvimento do documento de testes de integração | Felipe Duarte |
| 1.1 | 09/02/2025 | Revisão do Documento| Felipe Freire |