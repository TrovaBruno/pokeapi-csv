# tests/test_pokemon_service.py

from app.services.pokemon_service import flatten_pokemon

def test_flatten_pokemon():
    data = {
        "name": "pikachu",
        "height": 4,
        "weight": 60,
        "stats": [
            {"stat": {"name": "speed"}, "base_stat": 90}
        ]
    }

    flat = flatten_pokemon(data)

    assert flat["name"] == "pikachu"
    assert flat["height"] == 4
    assert flat["weight"] == 60
    assert flat["speed"] == 90
