# Poke API

Este projeto é um mini-experimento para praticar **Python**, **Flask**, **consumo de APIs REST**, manipulação de **JSON aninhado**, criação de **logs em arquivo**, uso de **Makefile** e geração de **CSV** utilizando a [PokéAPI v2](https://pokeapi.co/docs/v2).

O objetivo é, ao final, ter:

- Um pequeno microserviço em Flask  
- Um cliente HTTP que se comunica com a PokéAPI  
- Um processo que extrai dados detalhados de Pokémon e “achata” JSONs complexos  
- Geração de arquivos **CSV** estruturados com informações úteis  
- Automação de tarefas com **Makefile** (linter, testes)  
- Logs salvos em arquivos dentro de uma pasta ignorada pelo Git  

> Priorize fazer funcionar primeiro e depois polir a implementação.

---

## Objetivos do projeto

- [ ] Criar um repositório organizado em camadas: `models`, `services`, `views`.  
- [ ] Expor uma rota simples com **Flask** para testar a geração de dados.  
- [ ] Configurar **logging** em arquivos dentro de uma pasta não versionada (`/dados/logs`).  
- [ ] Criar um **Makefile** para rodar o linter e testes automatizados.  
- [ ] Escrever **testes unitários** com `pytest`.  
- [ ] Consumir dados da **PokéAPI** via HTTP e navegar em JSONs aninhados.  
- [ ] Transformar os dados em uma forma “flat” e gerar arquivos **CSV**.

---

## Requisitos

- Python 3.10 ou superior  
- Git instalado  
- Virtualenv ou outra ferramenta de ambiente virtual (`python -m venv`)  
- Conexão com a internet (para acessar a PokéAPI)

Bibliotecas Python recomendadas:

- `flask`  
- `requests`  
- `pytest`  
- `ruff` ou `flake8`  

---

## Estrutura sugerida do projeto

```bash
pokeapi-csv/
├── .gitignore
├── README.md
├── Makefile
├── requirements.txt
├── dados/
│   └── logs/           # logs não versionados
├── app.py
├── main.py          # ponto de entrada do Flask
├── models/
│   └── pokemon.py      # definição de modelos/datatypes
├── services/
│   ├── pokeapi_client.py   # funções para consumir a PokéAPI
│   ├── pokeapi_service.py  # funções para processar/achatar dados
│   └── csv_exporter.py     # funções para exportar CSV
├── views/
│   └── pokedex_view.py     # rotas Flask (controllers/views)
└── tests/
    ├── test_pokeapi_client.py
    ├── test_pokemon_service.py
    └── test_csv_exporter.py

