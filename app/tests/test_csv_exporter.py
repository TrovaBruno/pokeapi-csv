import csv
from app.services.csv_exporter import export_to_csv

def test_export_to_csv(tmp_path):
    data = [
        {"name": "pikachu", "speed": 90},
        {"name": "bulbasaur", "speed": 45}
    ]

    file_path = tmp_path / "pokemon.csv"
    export_to_csv(data, file_path)

    assert file_path.exists()

    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["name"] == "pikachu"
    assert rows[1]["name"] == "bulbasaur"
