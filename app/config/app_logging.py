import logging  # importa o modulo de monitoramento do programa
from pathlib import Path

LOG_DIR = Path("dados/logs") # cria um objeto Path apontando para o diretório dados/logs
LOG_DIR.mkdir(parents=True, exist_ok=True) #cria a pasta dados/logs se ea já existir, não gera erro

LOG_FILE = LOG_DIR / "app.log" #cria caminho para o arquivo de log, dentro da pasta dados/logs

def setup_logger():
    logging.basicConfig( #configura o log padrão do python
        level=logging.INFO, #define o nivel de severidade da mensagem
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s", #define o formato das mensagens, hora, nivel, nome do logger, a mensagem
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"), 
            logging.StreamHandler()
        ]#define para onde o log vai, para a pasta app.log e para a console do terminal
    )
    