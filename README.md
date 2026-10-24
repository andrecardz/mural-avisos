# Mural de Avisos Acadêmicos

Laboratório de Programação Full Stack — Atividade prática extra dos Encontros 1 e 2.
Back-end FastAPI construído para o front-end fornecido. Os avisos ficam em uma lista
Python, sem banco de dados.

## Como executar

Back-end (primeiro terminal):

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Front-end (segundo terminal, sem encerrar o Uvicorn):

```powershell
cd frontend
python -m http.server 5500
```

- Interface: http://localhost:5500
- Swagger: http://127.0.0.1:8000/docs

## Grupo

| Integrante | Matrícula | Contribuição |
|---|---|---|
| André Ávila Cardoso | 202411312 | `models.py` e validações do Pydantic |
| Daniel Monteiro de Oliveira | 202411308 | rota GET /api/avisos |
| Fabrício de Lima Rodrigues Monteiro | 202411276 | rota POST /api/avisos e código 201 |
| Kevin Teixeira Paula | 202411265 | configuração do CORS e ambiente virtual |
| Samuel Ribeiro Soares | 202411296 | testes mínimos e evidências |
| Thiago Araújo Brites | 202411274 | documentação e organização do repositório |

## Contrato da API

| Operação | Método e rota | Resposta |
|---|---|---|
| listar avisos | GET /api/avisos | 200 e lista JSON |
| publicar aviso | POST /api/avisos | 201 e aviso criado |

Campos do corpo do POST:

| Campo | Tipo | Regra |
|---|---|---|
| titulo | string | obrigatório, de 4 a 60 caracteres |
| mensagem | string | obrigatório, de 10 a 300 caracteres |
| autor | string | obrigatório, de 3 a 50 caracteres |
| prioridade | string | obrigatório, apenas `normal` ou `importante` |

Os limites acompanham os atributos `minlength` e `maxlength` do formulário em
`index.html`. Os campos `id` e `publicado_em` são gerados pela API.

Exemplo de envio:

```json
{
  "titulo": "Monitoria de programação",
  "mensagem": "A monitoria ocorrerá no laboratório 3 às 18 horas.",
  "autor": "Coordenação",
  "prioridade": "importante"
}
```

Resposta 201:

```json
{
  "titulo": "Monitoria de programação",
  "mensagem": "A monitoria ocorrerá no laboratório 3 às 18 horas.",
  "autor": "Coordenação",
  "prioridade": "importante",
  "id": 1,
  "publicado_em": "2026-10-23T02:46:56.312644"
}
```

Resposta 422, com prioridade fora das opções:

```json
{
  "detail": [
    {
      "type": "literal_error",
      "loc": ["body", "prioridade"],
      "msg": "Input should be 'normal' or 'importante'",
      "input": "urgente"
    }
  ]
}
```

## Arquivos do back-end

| Arquivo | Responsabilidade |
|---|---|
| backend/models.py | contratos de entrada e de saída, com os limites de texto e a prioridade restrita |
| backend/main.py | aplicação, CORS para a porta 5500, lista de avisos e as duas rotas |
| backend/requirements.txt | dependências do ambiente virtual |

## Testes realizados

| Caso | Resultado obtido |
|---|---|
| GET antes de publicar | 200 e lista vazia |
| POST com dados válidos | 201 e objeto com `id` e `publicado_em` |
| GET após publicar | 200 e o aviso na lista |
| prioridade `urgente` | 422, `Input should be 'normal' or 'importante'` |
| mensagem com menos de 10 caracteres | 422, `String should have at least 10 characters` |
| mensagem ausente | 422, `Field required` |

## Evidências

As capturas estão na pasta `evidencias/`:

- `evidencia-1-interface-com-aviso.png` — interface exibindo ao menos um aviso
- `evidencia-2-swagger-rotas.png` — Swagger mostrando as duas rotas
- `evidencia-3-network-get-200-post-201.png` — Network com o GET 200 e o POST 201
- `evidencia-4-swagger-422.png` — resposta 422 provocada pelo Swagger
