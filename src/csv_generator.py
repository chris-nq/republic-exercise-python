import csv
from typing import Any, Dict, List, Sequence

from models.planet import Planet


class CSVGenerator:
    def __init__(self):
        self.data = []
        self.headers = ["name", "terrain", "population"]

    def generate(self, terrains: List[str], data: Sequence[Planet]) -> None:
        fname = f"planets_{('_').join(terrains) if terrains else 'all'}.csv"
        with open(fname, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.headers, delimiter="|")
            writer.writeheader()
            writer = csv.DictWriter(csvfile, fieldnames=self.headers, delimiter="|", quoting=csv.QUOTE_NONNUMERIC)
            for planet in data:
                if terrains and not any(t in planet.terrain for t in terrains):
                    continue
                planet_dict = dict(planet)
                planet_dict["terrain"] = ", ".join(planet_dict["terrain"])
                writer.writerow(planet_dict)