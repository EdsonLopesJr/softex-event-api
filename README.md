### Exercício: Request e Response

Criar uma API de cadastro de `Event` (Evento) que use dados do request para validações e retorne uma resposta customizada.

1. Crie um modelo `Event` com os seguintes campos:
    - `name`: Nome do evento
    - `description`: Descrição do evento
    - `start_date`: Data de início do evento
    - `end_date`: Data de fim do evento
2. Implemente uma view `CreateEventView` que:
    - Receba um `POST` request com os dados do evento.
    - Valide que a `end_date` seja maior ou igual à `start_date`.
    - Verifique se o `name` do evento já existe no banco de dados e, caso já exista, retorne um status HTTP `409 CONFLICT` com a mensagem: "Evento já existe com esse nome."
    - Caso o evento seja criado com sucesso, retorne os dados do evento criado com o status HTTP `201 CREATED`.
3. Adicione os endpoints da view no arquivo `urls.py` e teste os cenários de sucesso e erro no cadastro do evento.