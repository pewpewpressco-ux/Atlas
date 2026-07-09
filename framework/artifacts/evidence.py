from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import hashlib
import json

from framework.artifacts.enums import EvidenceLevel


@dataclass(frozen=True, slots=True)
class EvidenceRecord:
    source: str
    methodology: str
    level: EvidenceLevel
    confidence: float
    provenance: str
    timestamp: datetime
    hash: str

    @classmethod
    def create(
        cls,
        source: str,
        methodology: str,
        level: EvidenceLevel,
        confidence: float,
        provenance: str,
        timestamp: datetime | None = None,
    ) -> "EvidenceRecord":
        timestamp = timestamp or datetime.utcnow()
        payload = {
            "source": source,
            "methodology": methodology,
            "level": level.value,
            "confidence": confidence,
            "provenance": provenance,
            "timestamp": timestamp.isoformat(),
        }
        digest = hashlib.sha256(
            json.dumps(payload, sort_keys=True).encode("utf-8")
        ).hexdigest()
        return cls(hash=digest, timestamp=timestamp, **payload)
