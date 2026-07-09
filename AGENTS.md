# Atlas Repository AI Development Guide

## Purpose

This document defines repository-level operating instructions for AI-assisted development on Atlas.

GitHub is the canonical source of truth.

Do not rely on conversation history when repository state can be verified directly.

---

# Session Workflow

Every Atlas engineering session must follow this sequence:

1. Synchronize with the repository.
2. Review this AGENTS.md file.
3. Review docs/HANDOFF.md.
4. Review docs/CONSTITUTION.md.
5. Review docs/ARCHITECTURE.md.
6. Review docs/ROADMAP.md.
7. Review docs/DECISIONS.md.
8. Understand the existing implementation before changing it.
9. Produce an implementation plan before significant changes.
10. Implement.
11. Verify.
12. Update documentation affected by changes.
13. Update docs/HANDOFF.md at session close.

---

# Engineering Priorities

Prioritize decisions in this order:

1. Architectural integrity
2. Correctness
3. Capital preservation
4. Reproducibility
5. Maintainability
6. Simplicity
7. Extensibility
8. Performance

Do not sacrifice architecture for short-term implementation speed.

---

# Atlas Principles

Atlas is a production-grade, evidence-driven autonomous trading platform.

The system must prioritize:

- evidence before capital
- validation before promotion
- deterministic behavior
- reproducibility
- explicit interfaces
- immutable state transitions
- clear ownership boundaries

---

# Architecture Rules

## Artifact-Centric Design

Artifacts are the primary communication boundary between Atlas components.

Services should follow:

Input Artifact

↓

Processing

↓

Output Artifact

Do not introduce hidden shared state between services.

---

## Immutability

Prefer immutable data structures.

Do not silently mutate historical records.

Changes to evidence, validation, or lifecycle state should create new versions or new artifacts.

---

## Dependency Design

Prefer:

- composition over inheritance
- dependency inversion
- explicit interfaces
- small cohesive components
- strongly typed models

Avoid:

- global mutable state
- magic values
- duplicated abstractions
- parallel implementations
- hidden coupling

---

# Evidence Standards

Atlas is evidence-driven.

Any recommendation, promotion decision, or capital allocation process should be supported by measurable evidence.

Avoid opinion-based system behavior.

Evidence should maintain:

- provenance
- reproducibility
- validation history
- confidence information

---

# Capital and Strategy Governance

No trading strategy should advance based only on implementation readiness.

Strategies must progress through documented evidence gates.

Capital allocation authority belongs to the governance layer defined by the Atlas Constitution.

---

# Documentation Requirements

Documentation is part of the product.

Update relevant documents when architecture changes:

```
docs/
├── CONSTITUTION.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── DECISIONS.md
└── HANDOFF.md
```

Important architectural decisions must be recorded in DECISIONS.md.

---

# Testing Expectations

New functionality should include appropriate verification.

Prioritize tests for:

- domain contracts
- artifact integrity
- validation logic
- serialization
- lifecycle transitions
- persistence boundaries

---

# Change Discipline

Before adding new functionality:

1. Verify whether an existing abstraction already solves the problem.
2. Avoid creating duplicate systems.
3. Prefer refactoring existing architecture over adding parallel paths.
4. Document significant tradeoffs.

---

# Current Known Priority

The next major engineering effort is strengthening the Artifact Framework.

Required direction:

- immutable Artifact model
- structured Evidence model
- typed Artifact lifecycle
- validation pipeline
- artifact integrity verification
- test foundation

Do not expand higher-level services until these foundations are stable.
