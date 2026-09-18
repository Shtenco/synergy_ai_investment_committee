from synergy_ai_committee.core import *

def test_guardian_veto():
    t=deliberate(MarketContext('BTC',1,.5))
    assert t.action=='NO_TRADE' and t.capital_guardian.startswith('VETO')

def test_auditable_votes():
    t=deliberate(MarketContext('EURUSD',.8,.02,liquidity=1.0))
    assert len(t.votes)==3
