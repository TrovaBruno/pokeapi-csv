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