from dataclasses import field, dataclass
import json
import os
from typing import List

from models.planet import Planet


@dataclass
class Errors:
    no_results: List[str] = field(default_factory=list)
    json_error: List[str] = field(default_factory=list)


class PlanetaryArchive:
    """
    A paginator representing a planet archive.
    Every page is a list of planets.
    """
    def __init__(self, archive_path: os.PathLike):
        self.dir_path = os.path.abspath(archive_path)
        self._pages = None
        self.errors = Errors()
        if not os.path.exists(archive_path):
            raise FileNotFoundError(f"Path {archive_path} does not exist")
    
    def __len__(self):
        if self._pages is not None:
            return self._pages
        
        for _, _, filenames in os.walk(self.dir_path):
            self._pages = len(filenames)

        return self._pages
    
    def __iter__(self):
        self.errors = Errors()
        self._pages = None
        for root, _, filenames in os.walk(self.dir_path):
            for filename in sorted(filenames):
                with open(os.path.join(root, filename), "r") as file:
                    raw_file = file.read()
                try:
                    json_file = json.loads(raw_file)
                    results = json_file.get("results", None)
                    if results is None:
                        self.errors.no_results.append(filename)
                        continue
                    yield (Planet.from_dict(planet) for planet in results)
                except json.JSONDecodeError:
                    self.errors.json_error.append(filename)
                    continue
