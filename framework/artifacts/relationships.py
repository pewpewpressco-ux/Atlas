from dataclasses import dataclass


@dataclass(slots=True)

class Relationship:

    source: str

    target: str

    relationship: str
