from contextlib import contextmanager
import csv
import time
from typing import Iterable, List

import click

from planetary_archive import PlanetaryArchive


class PlanetaryScanner:
    def __init__(self, headers = None):
        self.terrains = None
        self.headers = headers or ["name", "terrain", "population"]

    @property
    def filename(self) -> str:
        if self.terrains is None:
            return None
        return f"planets_{('_').join(self.terrains) if self.terrains else 'all'}.csv"

    def scan(self, terrains: List[str], archive: PlanetaryArchive, throttle=0) -> None:
        self.terrains = terrains
        with open(self.filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.headers, delimiter="|")
            writer.writeheader()
            writer = csv.DictWriter(csvfile, fieldnames=self.headers, delimiter="|", quoting=csv.QUOTE_NONNUMERIC)
            with self.progressbar(archive) as bar:
                for page in bar:
                    for planet in page:
                        if terrains and not any(t in planet.terrain for t in terrains):
                            continue
                        planet_dict = dict(planet)
                        planet_dict["terrain"] = ", ".join(planet_dict["terrain"])
                        writer.writerow(planet_dict)
                        if throttle:
                            time.sleep(throttle)

    @contextmanager
    def progressbar(self, iterable: Iterable, label: str = None, length: int = None):
        with click.progressbar(iterable, label=label or "Scanning planets", length=length) as bar:
            yield bar


    
