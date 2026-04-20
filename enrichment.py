RESOURCE_DB = {
    "bucket-123": {"owner": "payments", "env": "prod", "data": "PII"},
}

def enrich(event):
    return {**event, **RESOURCE_DB.get(event["resource"], {})}