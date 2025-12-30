import http.client
import json
import logging

logger = logging.getLogger(__name__)

BASE_HOST = "pokeapi.co"

def listar_pokemons(limit=20):
    logger.info("Buscando lista de pokémons na PokéAPI")

    conn = http.client.HTTPSConnection(BASE_HOST)
    conn.request("GET", f"/api/v2/pokemon?limit={limit}")

    response = conn.getresponse()
    data = response.read().decode()

    if response.status != 200:
        raise RuntimeError("Erro ao buscar lista de pokémons")

    json_data = json.loads(data)
    return json_data["results"]

def buscar_pokemon(nome: str):
    logger.info("Buscando Pokémon %s na PokéAPI", nome)

    conn = http.client.HTTPSConnection(BASE_HOST)
    conn.request("GET", f"/api/v2/pokemon/{nome}")

    response = conn.getresponse()
    data = response.read().decode()

    if response.status != 200:
        raise ValueError(f"Pokémon {nome} não encontrado")

    return json.loads(data)
