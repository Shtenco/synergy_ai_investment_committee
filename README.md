# SYNERGY AI Investment Committee

> **Auditable multi-agent investment decision support with deterministic Capital Guardian boundary**

Version: `2.0.0`

**Enterprise v2.0.0** · FastAPI/OpenAPI · Docker/Compose · RBAC/JWT · PostgreSQL/ClickHouse audit

**Designed for:** Quant funds, asset managers, research teams and AI-native investment desks  
**Primary endpoint:** `POST /enterprise/v1/committee/deliberate`

> [!IMPORTANT]
> Decision-support infrastructure only. AI deliberation is not autonomous execution authority; deterministic risk/Capital Guardian controls remain separate.

## Verification
**20 tests passed** · health smoke **80/80 200** · local p95 **79.3 ms** (~549 req/s). Health smoke only.

## Quick start
```bash
pip install -e '.[dev,enterprise]'
pytest -q
python -m synergy_ai_committee.api
```

## CTO package
[Due diligence](docs/CTO_DUE_DILIGENCE.md) · [Architecture](docs/ARCHITECTURE_DIAGRAMS.md) · [API](docs/API_EXAMPLES.md) · [Security](SECURITY.md) · [Benchmarks](docs/BENCHMARKS_AND_ACCEPTANCE.md) · [SLA/SLO](docs/SLA_SLO.md) · [Deployment](docs/DEPLOYMENT_CHECKLIST.md) · [Pilot](docs/CUSTOMER_PILOT.md)
