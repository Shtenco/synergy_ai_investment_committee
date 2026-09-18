# API examples — SYNERGY AI Investment Committee

`POST /enterprise/v1/committee/deliberate` — roles **researcher, risk**.

```json
{"symbol":"BTCUSDT","momentum":0.4,"volatility":0.05,"valuation":0.0,"liquidity":0.9}
```

Expected: `action`, `capital_guardian`, `score`, `request_id`. Canonical schema: `/docs`.