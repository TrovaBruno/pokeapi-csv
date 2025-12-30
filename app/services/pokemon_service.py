import logging

logger = logging.getLogger(__name__)

def achatar_pokemon(pokemon_json: dict) -> dict:
    logger.debug("Achatando Pokémon %s", pokemon_json.get("name"))

    pokemon_flat = {
        "id": pokemon_json.get("id"),
        "name": pokemon_json.get("name"),
        "height": pokemon_json.get("height"),
        "weight": pokemon_json.get("weight"),
        "base_experience": pokemon_json.get("base_experience"),
        "sprite": pokemon_json.get("sprites", {}).get("front_default"),
    }

    pokemon_flat["types"] = ", ".join(
        t["type"]["name"] for t in pokemon_json.get("types", [])
    )

    pokemon_flat["abilities"] = ", ".join(
        a["ability"]["name"] for a in pokemon_json.get("abilities", [])
    )

    for stat in pokemon_json.get("stats", []):
        pokemon_flat[stat["stat"]["name"]] = stat["base_stat"]

    return pokemon_flat
