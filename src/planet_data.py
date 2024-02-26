import json
import os

from models.planet import Planet


class PlanetData:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        if not self.__path_exists(dir_path):
            raise FileNotFoundError(f"Path {dir_path} does not exist")

    def __iter__(self):
        for root, _, filenames in os.walk(self.dir_path):
            for filename in sorted(filenames):
                with open(os.path.join(root, filename), "r") as file:
                    raw_file = file.read()
                try:
                    json_file = json.loads(raw_file)
                    results = json_file.get("results", None)
                    if results is None:
                        print(f"Error getting results from {filename}")
                        continue
                    for result in results:
                        planet = Planet.from_dict(result)
                        yield planet
                except json.JSONDecodeError:
                    print(f"Error decoding {filename}")
                    continue

    @staticmethod
    def __path_exists(path):
        return os.path.exists(path)
