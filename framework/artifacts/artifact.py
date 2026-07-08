from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Artifact:

    id: str

    title: str

    type: str

    version: str = "1.0.0"

    status: str = "Draft"

    evidence: str = "D"

    created: datetime = field(default_factory=datetime.utcnow)

    updated: datetime = field(default_factory=datetime.utcnow)

    author: str = "Atlas"

    tags: list[str] = field(default_factory=list)

    relationships: dict[str, list[str]] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    content: dict[str, Any] = field(default_factory=dict)
