from pathlib import Path

PREFIXES = {

    "strategy": "STRAT",

    "experiment": "EXP",

    "review": "REV",

    "report": "RPT",

    "research": "RS",

    "workflow": "WF"

}


def build(prefix: str, number: int):

    return f"{PREFIXES[prefix]}-{number:04d}"
