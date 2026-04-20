# Security Automation Pipeline (Python)

A lightweight simulation of an end-to-end security/compliance automation system.

This project demonstrates how security events can be:
- Detected
- Enriched with context
- Classified by risk
- Explained using AI-style summarization
- Automatically remediated
- Verified for resolution

---

## Architecture Overview

```text
        ┌────────────────────┐
        │ 1. Event Detection │
        │ generate_event()   │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ 2. Enrichment      │
        │ enrich()           │
        │ (adds context)     │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ 3. Classification  │
        │ classify()         │
        │ (HIGH/MED/LOW)     │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ 4. AI Summary      │
        │ llm_summarize()    │
        │ (human-readable)   │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ 5. Remediation     │
        │ remediate()        │
        │ (fix / ticket / log)
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ 6. Verification    │
        │ verify()           │
        │ (re-scan check)    │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ 7. State Tracking  │
        │ STATE[]            │
        │ (history/logging)  │
        └────────────────────┘