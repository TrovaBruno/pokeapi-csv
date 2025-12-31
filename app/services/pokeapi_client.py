import logging
import requests
from flask import jsonify
from app.services.pokemon_service import flatten_pokemon
from app.services.csv_exporter import export_to_csv

logger = logging.getLogger(__name__)

# Função que lista pokémons da API
def listar_pokemons():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10")
    if response.status_code != 200:
        raise ValueError("Erro ao listar pokémons")
    return response.json().get("results", [])

# Função que busca detalhes de um Pokémon
def buscar_pokemon(nome: str):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome}")
    if response.status_code != 200:
        raise ValueError(f"Pokémon {nome} não encontrado")
    return response.json()

# Função de serviço que retorna lista de pokémons como JSON
def listar_pokemons_service():
    pokemons = listar_pokemons()
    return jsonify(pokemons)

# Função de serviço que retorna detalhe de um Pokémon, grava CSV e retorna JSON
def get_pokemon_detail(nome: str):
    try:
        bruto = buscar_pokemon(nome)
        pokemon = flatten_pokemon(bruto)

        export_to_csv([pokemon], "dados/pokedex.csv")

        logger.info("Pokémon %s processado com sucesso", nome)
        return jsonify(pokemon)

    except ValueError as e:
        logger.warning(str(e))
        return jsonify(error=str(e)), 404

    except Exception:
        logger.exception("Erro inesperado")
        return jsonify(error="Erro interno"), 500
