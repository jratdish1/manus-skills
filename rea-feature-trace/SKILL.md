---
name: rea-feature-trace
description: Six-step REA gate (pick, trace, challenge, spec, build, break) run BEFORE building any VAO module such as the paper desk, social pipeline, scraper, or Interests tab cards. Docs-only. Produces a spec and a break-test list. Never deploys, installs, or spends.
---

# REA Feature Trace Skill

Status: STUB — SCAFFOLDED_HOLD
Lane: VAO-MODTABS-01
Source: VETS Master Report, VAO Modular Tabs, 2026-10-22 13:45 PDT / 20:45 UTC
Intake card: jratdish1/knowledge-base PR #591

## Mission

Stop hype from becoming code. Before any VAO module is built, run the six steps below and return one written result. If any step fails, the module stays SCAFFOLDED_HOLD.

## When to use

- Before building the paper desk subdomain.
- Before building the social pipeline subdomain.
- Before adding any new Interests tab card.
- Before standing up the scraper or any scheduled job.
- When a post, tool, or repo claims a result that has no ledger.

## The six steps

1. **PICK** — Name one feature. One sentence. One owner. One VAO lane ID.
2. **TRACE** — Trace the real data path: source, transform, storage, display. List every file, service, credential, and network call touched. Mark each as EXISTS / MISSING / UNKNOWN.
3. **CHALLENGE** — Attack the idea. Answer: Is it hype without a ledger? Does it need live money, live keys, or a new install? Does it share credentials or sessions across subdomains? Does a cheaper local method already do it? If any answer is bad, stop and return HOLD.
4. **SPEC** — Write the smallest spec that works: inputs, outputs, isolation boundary, status values, gate name, rollback.
5. **BUILD** — Only the spec. Branch, PR, tests. Local first. Grok only if local quality fails.
6. **BREAK** — Try to break it before calling it done: bad input, missing source, stale data, duplicate run, cross-subdomain access attempt, credential leak scan. Record each result.

## Hard rails

- No live trading keys. No real orders. Paper only.
- No shared cookies, sessions, or credential stores between main VAO and any subdomain.
- No install, no spend, no new connector without a named use and VETS GO.
- No secrets in output.
- Bot never cancels subscriptions. Human cancels.
- ACTIVE_VERIFIED only with GitHub path + FLEET_ADMIN_STATE.json or deploy report with commit SHA.

## Required output format

```
REA FEATURE TRACE
PDT:
UTC:
LANE ID:
FEATURE (PICK):
TRACE:
- item | EXISTS / MISSING / UNKNOWN
CHALLENGE:
- hype/ledger:
- money/keys:
- install/spend:
- isolation:
- cheaper local method:
SPEC:
- inputs:
- outputs:
- isolation boundary:
- gate:
- rollback:
BUILD:
- branch:
- PR:
- tests:
BREAK:
- test | PASS / FAIL
VERDICT:
PROCEED / HOLD / SHELF
STATUS:
SCAFFOLDED_HOLD / DRY_RUN_READY / HUMAN_REVIEW_REQUIRED
```
