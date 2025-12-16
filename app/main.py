from flask import Flask
import logging

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
    
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)