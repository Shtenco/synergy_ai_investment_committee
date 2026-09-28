from __future__ import annotations
from typing import Any

from .core import MarketContext, deliberate

CONTRACT_ID = "synergy.trading.investment-thesis/v1"
AUTHORITY = "investment_committee"


def investment_thesis_payload(
    *,
    observation_id: str,
    symbol: str,
    momentum: float,
    volatility: float,
    valuation: float = 0.0,
    liquidity: float = 1.0,
    risk_veto_vol: float = .20,
) -> dict[str, Any]:
    if not observation_id.strip():
        raise ValueError("observation_id required")
    thesis = deliberate(
        MarketContext(
            symbol=symbol.upper(),
            momentum=float(momentum),
            volatility=float(volatility),
            valuation=float(valuation),
            liquidity=float(liquidity),
        ),
        risk_veto_vol=float(risk_veto_vol),
    )
    payload = thesis.to_dict()
    payload.update({
        "observation_id": observation_id,
        "authorization": False,
        "requires_domain_validation": True,
    })
    return payload
