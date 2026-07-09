from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from framework.artifacts.enums import ArtifactLifecycle, ArtifactType
from framework.artifacts.evidence import EvidenceRecord


@dataclass(frozen=True, slots=True)
class Artifact:
    id: str
    title: str
    type: ArtifactType
    lifecycle: ArtifactLifecycle = ArtifactLifecycle.DRAFT
    evidence: tuple[EvidenceRecord, ...] = field(default_factory=tuple)
    version: str = "1.0.0"
    schema_version: str = "1.0"
    created: datetime = field(default_factory=datetime.utcnow)
    updated: datetime = field(default_factory=datetime.utcnow)
    author: str = "Atlas"
    relationships: tuple[tuple[str, tuple[str, ...]], ...] = field(default_factory=tuple)
    metadata: tuple[tuple[str, Any], ...] = field(default_factory=tuple)
    content: tuple[tuple[str, Any], ...] = field(default_factory=tuple)
    integrity_hash: str | None = None
    parent_hash: str | None = None
