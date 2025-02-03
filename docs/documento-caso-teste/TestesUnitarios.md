
# Relatório de Testes Unitários

## App: Users

### `tests_views.py`

|Teste|Descrição|Resultado Esperado|
|---|---|---|
|test_login_page_loads_correctly|Testa se a página de login carrega corretamente.|Status 200 e template `login.html`|
|test_login_with_valid_credentials|Testa o login com credenciais válidas.|Status 302, redirecionamento para `/home/`|
|test_login_with_invalid_credentials|Testa o login com credenciais inválidas.|Status 200 e template `login.html`|
|test_login_without_credentials|Testa o login sem enviar credenciais.|Status 200 e template `login.html`|

### `test_models.py`

|Teste|Descrição|Resultado Esperado|
|---|---|---|
|test_area_creation|Testa a criação de uma instância do modelo `Area`.|Nome da área "Área de Teste"|
|test_str_method|Testa o método `__str__` do modelo `Area`.|Resultado esperado: "Área de Teste"|
|test_function_creation_with_valid_name|Testa a criação de uma instância do modelo `Function`.|Nome da função "Desenvolvedor"|
|test_function_str_method_returns_correct_name|Testa o método `__str__` do modelo `Function`.|Resultado esperado: "Desenvolvedor"|
|test_membro_creation|Testa a criação de uma instância de `MembroEquipe` com dados válidos.|Usuário "johndoe", nome completo "John Doe", email "[johndoe@example.com](mailto:johndoe@example.com)" e telefone "1234567890"|
|test_membro_str_method|Testa o método `__str__` do modelo `MembroEquipe`.|Resultado esperado: "johndoe"|
|test_membro_creation_without_required_fields|Testa a criação de `MembroEquipe` sem campos obrigatórios.|Lança `IntegrityError`|

### `tests_forms.py`

|Teste|Descrição|Resultado Esperado|
|---|---|---|
|test_form_valid_data|Testa se o formulário é válido com dados corretos.|Formulário válido|
|test_form_invalid_data|Testa se o formulário é inválido quando as senhas não coincidem.|Formulário inválido|
|test_fields_in_form|Verifica se os campos adicionais (áreas e funções) estão presentes no formulário.|Campos 'areas' e 'functions' presentes no formulário|
|test_form_no_areas_or_functions|Testa o formulário sem áreas ou funções.|Formulário válido|
|test_form_invalid_area|Testa o formulário com uma área inválida (ID inexistente).|Formulário inválido|
|test_form_invalid_function|Testa o formulário com uma função inválida (ID inexistente).|Formulário inválido|

## App: Stock

### `tests_views.py`

|Teste|Descrição|Resultado Esperado|
|---|---|---|
|test_stock_view|Testa se a visualização da página de estoque retorna o status 200 e exibe o template correto.|Status 200 e template `stock.html` com nome da ferramenta "Furadeira"|
|test_adicionar_ferramenta|Testa a adição de uma nova ferramenta no sistema.|Status 302, redirecionamento e ferramenta "Martelo" salva no banco de dados|
|test_editar_ferramenta|Testa a edição de uma ferramenta existente.|Status 302, redirecionamento e alterações na ferramenta "Furadeira Alterada"|
|test_deletar_ferramenta|Testa a exclusão de uma ferramenta.|Status 302, redirecionamento e ferramenta removida do banco de dados|

### tests_url.py`

|Teste|Descrição|Resultado Esperado|
|---|---|---|
|test_stock_url|Testa se a URL de estoque carrega corretamente.|Status 200 para URL `/stock/`|
|test_editar_ferramenta_url|Testa se a URL de editar ferramenta redireciona corretamente.|Status 302, redirecionamento para `/stock/` após edição da ferramenta|
|test_deletar_ferramenta_url|Testa se a URL de deletar ferramenta redireciona corretamente.|Status 302 após confirmação de exclusão|
|test_download_pdf_url|Testa se a URL para download do PDF carrega corretamente.|Status 200 para URL `/download_pdf/`|
|test_download_csv_url|Testa se a URL para download do CSV carrega corretamente.|Status 200 para URL `/download_csv/`|

### `tests_models.py`

|Teste|Descrição|Resultado Esperado|
|---|---|---|
|test_tool_creation|Testa a criação de uma instância do modelo Tool.|Ferramenta criada corretamente com nome "Hammer", marca "XYZ", etc.|
|test_str_method|Testa o método `__str__` do modelo Tool.|Retorno esperado: "Hammer"|
|test_tool_default_values|Testa se os valores padrões do modelo Tool estão funcionando corretamente.|Campos `observation` como `None` e `being_used` como `False`|


## APP: REPORT

### `tests_forms.py`

| Teste                                       | Descrição                                                                                 | Resultado Esperado                                                      |
| ------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| test_form_is_valid                          | Testa se o formulário é válido quando todos os dados fornecidos são corretos.             | O formulário deve ser validado corretamente                             |
| test_form_is_invalid_missing_required_field | Testa se o formulário é inválido quando um campo obrigatório está ausente.                | O formulário não deve ser válido sem campos obrigatórios                |
| test_form_save                              | Testa se os dados são salvos corretamente no banco de dados quando o formulário é válido. | Voo salvo corretamente no banco de dados                                |
| test_flight_success_rating_validation       | Testa a validação do campo 'flight_success_rating', que deve estar entre 1 e 5.           | O formulário deve ser inválido para valores fora do intervalo permitido |
| test_invalid_date_format                    | Testa se o campo 'date' aceita apenas datas válidas.                                      | O formulário deve ser inválido para valores de data incorretos          |
| test_invalid_time_format                    | Testa se o campo 'start_time' aceita apenas horários válidos.                             | O formulário deve ser inválido para valores de horário incorretos       |


### `tests_views.py`

| **Teste**                   | **Descrição**                                                                                       | **Resultado Esperado**                                                                                                                                   |
|-----------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **test_flight_list_view**    | Verifica se a lista de voos é carregada corretamente.                                                | A resposta deve conter o nome do piloto do voo registrado, confirmando que a lista de voos foi carregada corretamente.                                 |
| **test_flight_create_view**  | Verifica se a página de criação de voo carrega corretamente e se o voo é criado ao enviar o formulário. | O template correto (`flight_form.html`) deve ser utilizado. Após enviar os dados do voo, a resposta deve redirecionar para a lista de voos (`flight_list`) com status 302.  |
| **test_flight_edit_view**    | Verifica se a página de edição de voo carrega corretamente e se o voo é atualizado após a edição.     | O template correto (`flight_form.html`) deve ser utilizado. Após enviar os dados de edição, a resposta deve redirecionar para a lista de voos (`flight_list`) com status 302. O voo deve ser atualizado no banco de dados. |
| **test_flight_delete_view**  | Verifica se a página de exclusão de voo carrega corretamente e se o voo é excluído após confirmação.  | O template correto (`flight_confirm_delete.html`) deve ser utilizado. Após enviar a solicitação de exclusão, o voo deve ser excluído e a resposta deve redirecionar para a lista de voos (`flight_list`) com status 302. |


### `Tests_urls.py`

| **Teste**                   | **Descrição**                                                                                       | **Resultado Esperado**                                                                                                                                    |
|-----------------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **test_flight_list_url**     | Verifica se a URL para a lista de voos está acessível e retorna o código de status 200.            | A resposta deve ter o status code 200, indicando que a página da lista de voos foi carregada corretamente.                                              |
| **test_flight_create_url**   | Verifica se a URL para a criação de voos está acessível e retorna o código de status 200.           | A resposta deve ter o status code 200, indicando que a página de criação de voo foi carregada corretamente.                                              |


### `Tests_models.py`

| **Teste**                          | **Descrição**                                                                                    | **Resultado Esperado**                                                                                                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **test_minutes_creation**          | Testa a criação de uma instância do modelo `Minutes` e verifica se os campos estão corretos.     | O objeto `Minutes` deve ser salvo corretamente com os campos `date`, `title`, `content` e `responsible` correspondendo aos dados fornecidos.                                     |
| **test_string_representation**     | Testa se a representação em string do modelo `Minutes` está correta.                             | A representação em string deve ser `'Reunião de Teste'`, que é o valor do campo `title`.                                                                                         |
| **test_responsible_field**         | Testa se o campo `responsible` está associado corretamente a um objeto `MembroEquipe`.           | O campo `responsible` deve estar corretamente associado ao membro da equipe, e os campos `fullname`, `email` e `phone` devem ser os mesmos definidos para o membro.              |
| **test_flight_log_creation**       | Testa a criação de um `FlightLog` e verifica se os campos estão corretos.                        | O objeto `FlightLog` deve ser salvo corretamente no banco de dados, com todos os campos correspondendo aos dados fornecidos, incluindo o campo `occurred_accident` como `False`. |
| **test_default_occurred_accident** | Testa o valor padrão do campo `occurred_accident` para garantir que ele seja `False` por padrão. | O campo `occurred_accident` deve ter o valor `False` após a criação de um `FlightLog`, a menos que seja explicitamente alterado.                                                 |



## APP: GUEST


### `tests_views.py`

| **Teste**                   | **Descrição**                                                                                       | **Resultado Esperado**                                                                                                                                    |
|-----------------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **test_index_view**          | Testa se a view 'index' renderiza o template correto.                                               | A resposta deve ter o status code 200 e o template `index.html` deve ser usado.                                                                         |
| **test_competition_view**    | Testa se a view 'competition' renderiza o template correto.                                          | A resposta deve ter o status code 200 e o template `comp.html` deve ser usado.                                                                          |

### `Tests_models.py`

| **Teste**                   | **Descrição**                                                                                       | **Resultado Esperado**                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **test_create_admission_state** | Testa a criação de um novo `AdmissionState`.                                                         | O estado de admissão deve ser criado corretamente, e o valor de `is_open` deve ser `True`.                      |
| **test_default_admission_state** | Testa se o valor default do campo `is_open` em `AdmissionState` é `True`.                           | O estado de admissão deve ser criado com o valor padrão `is_open=True`.                                          |
