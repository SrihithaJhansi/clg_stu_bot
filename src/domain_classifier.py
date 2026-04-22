def detect_domain(query):
    q = query.lower()

    if any(word in q for word in ["mbbs", "neet", "medical"]):
        return "medical"
    elif any(word in q for word in ["btech", "engineering", "jee"]):
        return "engineering"
    else:
        return "general"