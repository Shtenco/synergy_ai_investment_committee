from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from .core import MarketContext,deliberate
app=FastAPI(title='SYNERGY AI Investment Committee',version='2.0.0')
class Req(BaseModel):symbol:str;momentum:float;volatility:float;valuation:float=0;liquidity:float=1
@app.get('/health')
def health():return {'ok':True,'service':'ai-investment-committee'}
@app.post('/v1/deliberate')
def go(req:Req):return deliberate(MarketContext(**req.model_dump())).to_dict()

# Enterprise v2 control/data plane
from .enterprise.service import EnterpriseRuntime, build_enterprise_router, install_observability
from .enterprise.product import build_product_router
enterprise_runtime=EnterpriseRuntime.from_env(service_name='synergy-ai-investment-committee')
install_observability(app,enterprise_runtime)
app.include_router(build_enterprise_router(enterprise_runtime))
app.include_router(build_product_router(enterprise_runtime))

if __name__=='__main__':uvicorn.run(app,host='0.0.0.0',port=8000)
