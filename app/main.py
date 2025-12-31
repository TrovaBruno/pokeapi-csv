from flask import Flask, jsonify
import logging

from app.services.pokeapi_client import listar_pokemons_service, get_pokemon_detail
from app.config.app_logging import setup_logger

def create_app():
    setup_logger()
    logger = logging.getLogger(__name__)
    logger.info("Inicializando aplicação Flask")

    app = Flask(__name__)

    @app.route("/")
    def index():
        logger.info("Health check acessado")
        return jsonify(status="ok")

    @app.route("/pokemons")
    def pokemons():
        return listar_pokemons_service()

    @app.route("/pokemon/<nome>")
    def pokemon(nome):
        return get_pokemon_detail(nome)

    return app
