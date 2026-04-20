import random

# -------------------------
# 1. EVENT GENERATION
# -------------------------
def generate_event():
    events = [
        {"type": "S3_PUBLIC_ACCESS", "resource": "bucket-123"},
        {"type": "IAM_UNUSED_KEY", "resource": "user-abc"},
        {"type": "K8S_PRIVILEGED_POD", "resource": "cluster-a"}
    ]
    return random.choice(events)


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
# 4. ACTION ENGINE
# -------------------------
def remediate(event, severity):
    if severity == "HIGH":
        return f"AUTO-FIX applied to {event['resource']}"
    elif severity == "MEDIUM":
        return f"Ticket created for {event['resource']}"
    else:
        return f"Logged {event['resource']} for review"


# -------------------------
# 5. VERIFICATION
# -------------------------
def verify(event):
    # simulate re-scan
    if event["type"] == "S3_PUBLIC_ACCESS":
        return False  # fixed
    return True


# -------------------------
# 6. LOOP
# -------------------------
def run():
    event = generate_event()
    enriched = enrich(event)
    severity = classify(enriched)
    action = remediate(enriched, severity)
    still_exists = verify(enriched)

    print("\nEVENT:", enriched)
    print("SEVERITY:", severity)
    print("ACTION:", action)
    print("RE-SCAN RESULT:", "STILL EXISTS" if still_exists else "RESOLVED")
    print("-" * 50)


if __name__ == "__main__":
    for _ in range(5):
        run()