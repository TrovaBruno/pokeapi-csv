import logging
from flask import jsonify

from app.client.pokeapi_client import listar_pokemons, buscar_pokemon
from app.services.pokemon_service import achatar_pokemon
from app.services.csv_exporter import exportar_csv

logger = logging.getLogger(__name__)

def listar_pokemons_service():
    pokemons = listar_pokemons()
    return jsonify(pokemons)

def detalhar_pokemon_service(nome: str):
    try:
        bruto = buscar_pokemon(nome)
        pokemon = achatar_pokemon(bruto)

        exportar_csv([pokemon], "dados/pokedex.csv")

        logger.info("Pokémon %s processado com sucesso", nome)
        return jsonify(pokemon)

    except ValueError as e:
        logger.warning(str(e))
        return jsonify(error=str(e)), 404

    except Exception:
        logger.exception("Erro inesperado")
        return jsonify(error="Erro interno"), 500
