# Deployment checklist — SYNERGY AI Investment Committee

- [ ] Pin code/model/prompt revisions and rerun tests.
- [ ] Customer TLS + OIDC/mTLS/JWKS and KMS secrets.
- [ ] Separate AI reasoning from deterministic Capital Guardian/risk authority.
- [ ] Configure audit store and model/prompt change control.
- [ ] Exercise `/enterprise/v1/committee/deliberate` on frozen customer scenarios.
- [ ] Prove roles **researcher, risk** and viewer denial.
- [ ] Test malformed/extreme inputs and failure/rollback paths.
- [ ] Keep execution separately gated and human/risk approved.