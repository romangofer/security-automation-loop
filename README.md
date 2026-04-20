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

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/roman-gofer/security-automation-loop.git
cd security-automation-loop

<!-- 2. (Optional) Create a virtual environment

python -m venv venv

Activate it:

Mac/Linux
source venv/bin/activate

Windows
venv\Scripts\activate

3. Run the program
python main.py -->

## Architecture Overview

```plaintext
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