import csv
import os
import time
import re
from typing import Iterable, List

import click

from .planetary_archive import PlanetaryArchive


class PlanetaryScanner:
    """
    Scans a PlanetaryArchive and writes a CSV file
    """

    def __init__(self, output_dir=None, headers=None):
        self.terrains = None
        self.output_dir = output_dir or "."
        self.headers = headers or ["name", "terrain", "population"]

    @property
    def filename(self) -> str:
        if self.terrains is None:
            return None
        return os.path.join(
            self.output_dir,
            f"planets_{('_').join(self.terrains) if self.terrains else 'all'}.csv",
        )
    
    def __escape_bad_chars(self, s: str) -> str:
        return re.sub(r'["|]', '_', s)
        
    def __escape_bad_chars_in_planet(self, planet: dict) -> dict:
        return {k: self.__escape_bad_chars(v) for k, v in planet.items()}

    def scan(self, terrains: List[str], archive: PlanetaryArchive, throttle=0) -> None:
        self.terrains = terrains

        with open(self.filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.headers, delimiter="|")
            writer.writeheader()
            writer = csv.DictWriter(
                csvfile, fieldnames=self.headers, delimiter="|", quoting=csv.QUOTE_ALL,
            )
            with self.progressbar(archive) as bar:
                for planet in bar:
                    
                    if throttle:
                        time.sleep(throttle)
                    if terrains and not any(t in planet.terrain for t in terrains):
                        continue
                    planet_dict = dict(planet)
                    planet_dict["terrain"] = ", ".join(planet_dict["terrain"])
                    planet_dict = self.__escape_bad_chars_in_planet(planet_dict)
                    writer.writerow(planet_dict)

    def progressbar(self, iterable: Iterable, label: str = None, length: int = None):
        return click.progressbar(
            iterable, label=label or "Scanning planets", length=length
        )
