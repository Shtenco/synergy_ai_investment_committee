from __future__ import annotations
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..core import MarketContext, deliberate
from .models import Principal, Role
from .service import EnterpriseRuntime, principal_dependency, request_id_header

class CommitteeRequest(BaseModel): symbol:str; momentum:float; volatility:float; valuation:float=0.0; liquidity:float=1.0

def build_product_router(runtime:EnterpriseRuntime)->APIRouter:
    router=APIRouter(prefix="/enterprise/v1/committee",tags=["enterprise-ai-committee"])
    @router.post("/deliberate")
    async def run(req:CommitteeRequest, principal:Principal=Depends(principal_dependency(runtime,{Role.RESEARCHER,Role.RISK})), request_id:str=Depends(request_id_header)):
        result=deliberate(MarketContext(**req.model_dump())).to_dict();result["request_id"]=request_id
        runtime.record(principal,action="committee.deliberate",request_id=request_id,payload={"symbol":req.symbol,"action":result["action"],"capital_guardian":result["capital_guardian"],"score":result["score"]})
        return result
    return router
