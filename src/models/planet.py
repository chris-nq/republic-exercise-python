from dataclasses import dataclass, asdict
import re
from typing import Any, Sequence, Dict


@dataclass
class Planet:
    name: str
    terrain: Sequence[str]
    population: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Planet":
        get_val = lambda key: data.get(key, "")
        terrain = re.split(r",\s*", get_val("terrain"))
        return cls(get_val("name"), terrain, get_val("population"))
    
    def __iter__(self):
        for key, value in asdict(self).items():
            yield key, value