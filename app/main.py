from flask import Flask
import logging

from app.services.pokeapi_service import listar_pokemons, detalhar_pokemon
from app.config.app_logging import setup_logger

def create_app():
    setup_logger()
    logger = logging.getLogger(__name__)
    logger.info("Inicializando aplicação Flask")

    app = Flask(__name__)

    @app.route("/")
    def index():
        logger.info("Rota / acessada")
        return "API Pokemon rodando!"
    @app.route("/pokemons")
    def pokemons():
        return listar_pokemons()
    @app.route("/pokemon/<nome>")
    def pokemon(nome):
        return detalhar_pokemon(nome)
    
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

