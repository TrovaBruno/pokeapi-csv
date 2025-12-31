import pytest
from unittest.mock import Mock
from app.services.pokeapi_client import buscar_pokemon

def test_get_pokemon_detail_success(mocker):
    fake_response = {"name": "pikachu", "id": 25}

    # Patch correto para requests.get dentro do módulo pokeapi_client
    mocker.patch(
        "app.services.pokeapi_client.requests.get",
        return_value=Mock(
            status_code=200,
            json=lambda: fake_response
        )
    )

    result = buscar_pokemon("pikachu")

    assert result["name"] == "pikachu"
    assert result["id"] == 25
