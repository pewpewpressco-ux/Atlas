from dataclasses import asdict
from enum import Enum

import yaml


class ArtifactSerializer:

    def _normalize(self, value):
        if isinstance(value, Enum):
            return value.value
        if isinstance(value, tuple):
            return [self._normalize(item) for item in value]
        if isinstance(value, dict):
            return {key: self._normalize(val) for key, val in value.items()}
        if hasattr(value, "__dataclass_fields__"):
            return self._normalize(asdict(value))
        return value

    def dump(self, artifact):
        return yaml.safe_dump(
            self._normalize(artifact),
            sort_keys=False,
        )
