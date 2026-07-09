from __future__ import annotations

from framework.artifacts.artifact import Artifact
from framework.artifacts.enums import ArtifactLifecycle
from framework.artifacts.integrity import ArtifactIntegrity


class ArtifactValidator:

    REQUIRED = [
        "id",
        "title",
        "type",
    ]

    VALID_TRANSITIONS = {
        ArtifactLifecycle.DRAFT: (ArtifactLifecycle.RESEARCH,),
        ArtifactLifecycle.RESEARCH: (ArtifactLifecycle.VALIDATION,),
        ArtifactLifecycle.VALIDATION: (ArtifactLifecycle.PAPER_TRADING,),
        ArtifactLifecycle.PAPER_TRADING: (ArtifactLifecycle.PROMOTION_REVIEW,),
        ArtifactLifecycle.PROMOTION_REVIEW: (ArtifactLifecycle.LIMITED_CAPITAL,),
        ArtifactLifecycle.LIMITED_CAPITAL: (ArtifactLifecycle.PRODUCTION,),
        ArtifactLifecycle.PRODUCTION: (ArtifactLifecycle.RETIRED,),
        ArtifactLifecycle.RETIRED: (),
    }

    def validate(self, artifact: Artifact) -> bool:
        self._validate_required_fields(artifact)
        self._validate_lifecycle(artifact)
        self._validate_evidence(artifact)
        self._validate_integrity(artifact)
        return True

    def validate_transition(
        self,
        current: ArtifactLifecycle,
        target: ArtifactLifecycle,
    ) -> bool:
        if target not in self.VALID_TRANSITIONS.get(current, ()):
            raise ValueError(
                f"Invalid lifecycle transition: {current} -> {target}"
            )
        return True

    def _validate_required_fields(self, artifact: Artifact) -> None:
        for field in self.REQUIRED:
            if getattr(artifact, field) is None:
                raise ValueError(f"{field} missing.")

    def _validate_lifecycle(self, artifact: Artifact) -> None:
        if not isinstance(artifact.lifecycle, ArtifactLifecycle):
            raise ValueError("Invalid artifact lifecycle.")

    def _validate_evidence(self, artifact: Artifact) -> None:
        for evidence in artifact.evidence:
            if not evidence.hash:
                raise ValueError("Evidence hash missing.")

    def _validate_integrity(self, artifact: Artifact) -> None:
        if artifact.integrity_hash is None:
            return

        if not ArtifactIntegrity.verify_hash(artifact):
            raise ValueError("Artifact integrity hash mismatch.")
