import pytest

from framework.artifacts.enums import ArtifactLifecycle
from framework.artifacts.validator import ArtifactValidator


@pytest.mark.parametrize(
    "current,target",
    [
        (ArtifactLifecycle.DRAFT, ArtifactLifecycle.RESEARCH),
        (ArtifactLifecycle.RESEARCH, ArtifactLifecycle.VALIDATION),
        (ArtifactLifecycle.VALIDATION, ArtifactLifecycle.PAPER_TRADING),
        (ArtifactLifecycle.PAPER_TRADING, ArtifactLifecycle.PROMOTION_REVIEW),
        (ArtifactLifecycle.PROMOTION_REVIEW, ArtifactLifecycle.LIMITED_CAPITAL),
        (ArtifactLifecycle.LIMITED_CAPITAL, ArtifactLifecycle.PRODUCTION),
    ],
)
def test_valid_lifecycle_transitions(current, target):
    assert ArtifactValidator().validate_transition(current, target)


@pytest.mark.parametrize(
    "current,target",
    [
        (ArtifactLifecycle.PRODUCTION, ArtifactLifecycle.DRAFT),
        (ArtifactLifecycle.RETIRED, ArtifactLifecycle.PRODUCTION),
    ],
)
def test_invalid_lifecycle_transitions(current, target):
    with pytest.raises(ValueError):
        ArtifactValidator().validate_transition(current, target)
