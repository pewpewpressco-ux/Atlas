from datetime import datetime

import pytest

from framework.artifacts.artifact import Artifact
from framework.artifacts.enums import ArtifactType, EvidenceLevel
from framework.artifacts.evidence import EvidenceRecord
from framework.artifacts.validator import ArtifactValidator


def test_valid_evidence_record_passes_validation():
    evidence = EvidenceRecord.create(
        source="test",
        methodology="unit test",
        level=EvidenceLevel.RESEARCH,
        confidence=0.9,
        provenance="pytest",
        timestamp=datetime.utcnow(),
    )

    artifact = Artifact(
        id="1",
        title="Evidence Test",
        type=ArtifactType.REPORT,
        evidence=(evidence,),
    )

    assert ArtifactValidator().validate(artifact)


def test_missing_evidence_hash_fails_validation():
    evidence = EvidenceRecord(
        source="test",
        methodology="unit test",
        level=EvidenceLevel.RESEARCH,
        confidence=0.9,
        provenance="pytest",
        timestamp=datetime.utcnow(),
        hash="",
    )

    artifact = Artifact(
        id="1",
        title="Evidence Test",
        type=ArtifactType.REPORT,
        evidence=(evidence,),
    )

    with pytest.raises(ValueError):
        ArtifactValidator().validate(artifact)
