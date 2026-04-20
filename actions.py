def remediate(event, severity):
    return f"{severity} action executed for {event['resource']}"