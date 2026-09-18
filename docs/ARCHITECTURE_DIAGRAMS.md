# Architecture — SYNERGY AI Investment Committee

```mermaid
flowchart LR
A[Market context]-->B[RBAC API]
B-->C[Committee deliberation]
C-->D[Critique / score]
D-->E[Capital Guardian]
E-->F[Decision-support artifact]
F-->G[Audit + request ID]
G-->H[(PostgreSQL)]
G-->I[(ClickHouse)]
F-->J{Customer execution boundary}
```

Primary endpoint: `/enterprise/v1/committee/deliberate`. Committee output is advisory/decision-support evidence, not autonomous authority to place live orders.