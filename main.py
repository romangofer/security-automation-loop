import random
import time

# -------------------------
# GLOBAL STATE (Upgrade 2)
# -------------------------
STATE = []

# -------------------------
# 1. EVENT GENERATION
# -------------------------
def generate_event():
    events = [
        {"type": "S3_PUBLIC_ACCESS", "resource": "bucket-123"},
        {"type": "IAM_UNUSED_KEY", "resource": "user-abc"},
        {"type": "K8S_PRIVILEGED_POD", "resource": "cluster-a"}
    ]

    event = random.choice(events)

    # add timestamp
    event["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

    return event


# -------------------------
# 2. ENRICHMENT
# -------------------------
RESOURCE_DB = {
    "bucket-123": {"owner": "payments", "env": "prod", "data": "PII"},
    "user-abc": {"owner": "security", "env": "dev", "data": "none"},
    "cluster-a": {"owner": "platform", "env": "prod", "data": "infra"}
}

def enrich(event):
    context = RESOURCE_DB.get(event["resource"], {})
    return {**event, **context}


# -------------------------
# 3. DECISION ENGINE
# -------------------------
def classify(event):
    if event["type"] == "S3_PUBLIC_ACCESS" and event.get("data") == "PII":
        return "HIGH"
    if event.get("env") == "prod":
        return "MEDIUM"
    return "LOW"


# -------------------------
# 4. LLM SUMMARY (Upgrade 4)
# -------------------------
def llm_summarize(event, severity):
    return (
        f"{event['resource']} is classified as {severity} risk "
        f"due to {event.get('data', 'unknown data exposure')}."
    )


# -------------------------
# 5. ACTION ENGINE
# -------------------------
def remediate(event, severity):
    if severity == "HIGH":
        return f"AUTO-FIX applied to {event['resource']}"
    elif severity == "MEDIUM":
        return f"Ticket created for {event['resource']}"
    else:
        return f"Logged {event['resource']} for review"


# -------------------------
# 6. VERIFICATION
# -------------------------
def verify(event):
    # simulate re-scan
    if event["type"] == "S3_PUBLIC_ACCESS":
        return False  # resolved
    return True


# -------------------------
# 7. MAIN LOOP (Upgrades 2,3,5)
# -------------------------
def run():
    print("\n[STAGE 1] Detecting event...")
    event = generate_event()

    print("[STAGE 2] Enriching event...")
    enriched = enrich(event)

    print("[STAGE 3] Classifying risk...")
    severity = classify(enriched)

    # LLM summary AFTER classification
    summary = llm_summarize(enriched, severity)

    print("[STAGE 4] Taking action...")
    action = remediate(enriched, severity)

    print("[STAGE 5] Verifying remediation...")
    still_exists = verify(enriched)

    # Store in state
    STATE.append({
        "event": enriched,
        "severity": severity,
        "summary": summary,
        "action": action,
        "status": "open" if still_exists else "resolved"
    })

    # -------------------------
    # FORMATTED OUTPUT (Upgrade 3)
    # -------------------------
    print("\n==============================")
    print("🚨 SECURITY EVENT DETECTED")
    print("==============================")

    print(f"Time: {enriched['timestamp']}")
    print(f"Type: {enriched['type']}")
    print(f"Resource: {enriched['resource']}")
    print(f"Owner: {enriched.get('owner', 'unknown')}")
    print(f"Environment: {enriched.get('env', 'unknown')}")

    print(f"\nSeverity: {severity}")
    print(f"AI Summary: {summary}")
    print(f"Action: {action}")

    print("\nVerification:",
          "❌ STILL VULNERABLE" if still_exists else "✅ RESOLVED")

    print("==============================\n")


# -------------------------
# ENTRY POINT
# -------------------------
if __name__ == "__main__":
    for _ in range(5):
        run()