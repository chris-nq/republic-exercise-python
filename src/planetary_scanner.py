import csv
import os
import time
from typing import Iterable, List

import click

from .planetary_archive import PlanetaryArchive


class PlanetaryScanner:
    """
    Scans a PlanetaryArchive and writes a CSV file
    """

    def __init__(self, headers=None, output_dir=None):
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

    def scan(self, terrains: List[str], archive: PlanetaryArchive, throttle=0) -> None:
        self.terrains = terrains

        with open(self.filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.headers, delimiter="|")
            writer.writeheader()
            writer = csv.DictWriter(
                csvfile, fieldnames=self.headers, delimiter="|", quoting=csv.QUOTE_ALL
            )
            with self.progressbar(archive) as bar:
                for planet in bar:
                    if throttle:
                        time.sleep(throttle)
                    if terrains and not any(t in planet.terrain for t in terrains):
                        continue
                    planet_dict = dict(planet)
                    planet_dict["terrain"] = ", ".join(planet_dict["terrain"])
                    writer.writerow(planet_dict)

    def progressbar(self, iterable: Iterable, label: str = None, length: int = None):
        return click.progressbar(
            iterable, label=label or "Scanning planets", length=length
        )
