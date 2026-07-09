from enum import Enum


class EvidenceLevel(str, Enum):
    RESEARCH = "D"
    HISTORICAL = "C"
    PAPER = "B"
    LIVE = "A"


class ArtifactLifecycle(str, Enum):
    DRAFT = "Draft"
    RESEARCH = "Research"
    VALIDATION = "Validation"
    PAPER_TRADING = "Paper Trading"
    PROMOTION_REVIEW = "Promotion Review"
    LIMITED_CAPITAL = "Limited Capital"
    PRODUCTION = "Production"
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
