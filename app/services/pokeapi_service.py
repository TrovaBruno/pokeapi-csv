import http.client
import json
import logging

logger = logging.getLogger(__name__)

def listar_pokemons(limit=20):
    logger.info("buscando lista de pokemon")

    conn = http.client.HTTPSConnection("pokeapi.co")
    conn.request("GET", f"/api/v2/pokemon?limit={limit}")

    response = conn.getresponse()
    data = response.read().decode()

    json_data = json.loads(data)
    return json_data["results"]

def detalhar_pokemon(nome: str): #Busca detalhes de um Pokémon específico na PokéAPI.
    logger.info(f"Buscando detalhes de um pokemon: {nome}")

    conn = http.client.HTTPSConnection("pokeapi.co")
    conn.request ("GET", f"/api/v2/pokemon/{nome}")

    response = conn.getresponse()
    data = response.read().decode()

    if response.status != 200:
        logger.error(f"Erro ao buscar pokemo{nome}: {response.status}")
        return{"error   ": f"Pokemon{nome} não encontrado"}
    
    json_data = json.loads(data)
        # Extrair alguns campos importantes
    detalhes = {
        "id": json_data["id"],
        "name": json_data["name"],
        "height": json_data["height"],
        "weight": json_data["weight"],
        "types": [t["type"]["name"] for t in json_data["types"]],
        "abilities": [a["ability"]["name"] for a in json_data["abilities"]],
        "sprite": json_data["sprites"]["front_default"],
    }
    return detalhes
