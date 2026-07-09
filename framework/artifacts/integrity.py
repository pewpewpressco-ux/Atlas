from __future__ import annotations

import hashlib
import json

from framework.artifacts.artifact import Artifact


class ArtifactIntegrity:
    """Deterministic artifact integrity calculation and verification."""

    @staticmethod
    def canonical_payload(artifact: Artifact) -> dict:
        return {
            "id": artifact.id,
            "title": artifact.title,
            "type": artifact.type.value,
            "lifecycle": artifact.lifecycle.value,
            "evidence": [evidence.hash for evidence in artifact.evidence],
            "content": artifact.content,
            "metadata": artifact.metadata,
            "relationships": artifact.relationships,
            "version": artifact.version,
            "schema_version": artifact.schema_version,
        }

    @classmethod
    def calculate_hash(cls, artifact: Artifact) -> str:
        payload = cls.canonical_payload(artifact)
        return hashlib.sha256(
            json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
        ).hexdigest()

    @classmethod
    def verify_hash(cls, artifact: Artifact) -> bool:
        if artifact.integrity_hash is None:
            return False
        return cls.calculate_hash(artifact) == artifact.integrity_hash
