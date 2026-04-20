def classify(event):
    if event.get("data") == "PII":
        return "HIGH"
    return "LOW"