# AI Investment Committee V3 Final Product Design

**Version:** 3.0.0  
**Branch:** `production/v3.0.0`  
**Status:** architecture specification for human review

## Goal
Convert the deterministic three-agent scoring demo into a governed AI decision-support product with versioned committee definitions, model/prompt provenance, immutable votes, deterministic Guardian policies and explicit human/risk approval.

## Current gap
Current agents are hard-coded classes and the endpoint returns one transient Thesis. No session lifecycle, model/prompt registry, approval resource or persistent vote provenance exists.

## Durable resources
- CommitteeDefinition
- AgentDefinition
- ModelReference
- PromptVersion
- GuardianPolicy
- CommitteeSession
- VoteArtifact
- DecisionArtifact
- HumanApproval

## Core invariants
1. Model and prompt versions are pinned for every session.
2. Every vote has agent/model/prompt provenance.
3. Deterministic Guardian executes outside mutable agent reasoning.
4. AI output cannot directly create live execution authority.
5. Required approval cannot be bypassed.
6. Provider/model failure cannot disable Guardian controls.
7. Session replay is possible from stored inputs/provenance subject to provider determinism limitations.
8. Sensitive prompts/provider secrets are never logged.

## Session lifecycle
CREATED -> DELIBERATING -> GUARDIAN_REVIEW -> APPROVAL_REQUIRED -> APPROVED | REJECTED
with FAILED terminal branch.

## V3 API
- `POST /enterprise/v3/committees`
- `GET /enterprise/v3/committees/{id}`
- `POST /enterprise/v3/sessions`
- `GET /enterprise/v3/sessions/{id}`
- `POST /enterprise/v3/sessions/{id}/approve`
- `POST /enterprise/v3/sessions/{id}/reject`
- `GET /enterprise/v3/decisions/{id}`

## Provider abstraction
Support deterministic built-in agents and optional external LLM provider adapters via injected interface. Provider credentials come only from secret manager/environment boundary.

## Persistence
PostgreSQL:
- committee_definitions
- agent_definitions
- model_references
- prompt_versions
- guardian_policies
- committee_sessions
- vote_artifacts
- decision_artifacts
- human_approvals
- idempotency_keys
- audit_events

## Acceptance gates
- decision stores complete provenance;
- Guardian veto cannot be bypassed by agent output;
- approval-required decision cannot progress without approval;
- provider timeout becomes explicit FAILED/partial state;
- restart preserves session;
- tenant isolation;
- readiness 503 on DB outage;
- V2 tests remain green.
