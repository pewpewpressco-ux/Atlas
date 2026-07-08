from enum import Enum


class EvidenceLevel(str, Enum):

    RESEARCH = "D"

    HISTORICAL = "C"

    PAPER = "B"

    LIVE = "A"


class ArtifactStatus(str, Enum):

    DRAFT = "Draft"

    ACTIVE = "Active"

    ARCHIVED = "Archived"

    RETIRED = "Retired"


class ArtifactType(str, Enum):

    REPORT = "Report"

    STRATEGY = "Strategy"

    EXPERIMENT = "Experiment"

    REVIEW = "Review"

    RESEARCH = "Research"

    REGIME = "Regime"

    PORTFOLIO = "Portfolio"

    WORKFLOW = "Workflow"

    FAILURE = "Failure"
