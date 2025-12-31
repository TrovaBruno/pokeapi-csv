import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def export_to_csv(pokemons: list[dict], path: str) -> None:
    if not pokemons:
        raise ValueError("Lista de pokémons vazia")

    arquivo = Path(path)
    arquivo.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = pokemons[0].keys()

    with arquivo.open(mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(pokemons)

    logger.info("CSV gerado com sucesso em %s", arquivo)
