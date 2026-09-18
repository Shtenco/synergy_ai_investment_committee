from __future__ import annotations
from dataclasses import dataclass,asdict
from typing import Protocol

@dataclass(frozen=True)
class MarketContext:
    symbol:str; momentum:float; volatility:float; valuation:float=0.0; liquidity:float=1.0
@dataclass(frozen=True)
class Vote:
    role:str; score:float; reason:str
@dataclass(frozen=True)
class Thesis:
    symbol:str; score:float; action:str; votes:tuple[Vote,...]; capital_guardian:str
    def to_dict(self):return {"symbol":self.symbol,"score":self.score,"action":self.action,"votes":[asdict(v) for v in self.votes],"capital_guardian":self.capital_guardian}

class Agent(Protocol):
    def vote(self,c:MarketContext)->Vote:...
class MomentumAgent:
    def vote(self,c):return Vote('Market Observer',max(-1,min(1,c.momentum)),f'momentum={c.momentum:.3f}')
class RiskAgent:
    def vote(self,c):return Vote('Risk Officer',-min(1,c.volatility*5),f'volatility={c.volatility:.3f}')
class LiquidityAgent:
    def vote(self,c):return Vote('Liquidity Analyst',max(-1,min(1,c.liquidity-0.5)),f'liquidity={c.liquidity:.3f}')

def deliberate(c:MarketContext,agents=None,risk_veto_vol=.20)->Thesis:
    agents=agents or [MomentumAgent(),RiskAgent(),LiquidityAgent()]
    votes=tuple(a.vote(c) for a in agents);score=sum(v.score for v in votes)/len(votes)
    if c.volatility>=risk_veto_vol:return Thesis(c.symbol,score,'NO_TRADE',votes,'VETO_VOLATILITY')
    action='BUY' if score>.2 else 'SELL' if score<-.2 else 'NO_TRADE'
    return Thesis(c.symbol,score,action,votes,'PASS')
