from synergy_ai_committee.synergy_contracts import CONTRACT_ID, investment_thesis_payload

def test_investment_thesis_is_advisory_and_veto_bounded():
    p=investment_thesis_payload(
        observation_id="obs-1",symbol="eurusd",momentum=.9,volatility=.25,liquidity=1
    )
    assert CONTRACT_ID=="synergy.trading.investment-thesis/v1"
    assert p["action"]=="NO_TRADE"
    assert p["capital_guardian"]=="VETO_VOLATILITY"
    assert p["authorization"] is False
    assert p["requires_domain_validation"] is True
