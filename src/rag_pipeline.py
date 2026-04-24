def get_answer(query, db):

    query_lower = query.lower()

    # Fix typo
    if "bda" in query_lower:
        query_lower = query_lower.replace("bda", "bds")

    # Detect course
    courses = ["bba", "bcom", "bds", "btech", "ece", "civil", "bjmc"]
    detected_course = next((c for c in courses if c in query_lower), None)

    # Detect city
    cities = ["chennai", "jaipur", "noida", "lucknow", "mysore", "ahmedabad"]
    detected_city = next((c for c in cities if c in query_lower), None)

    docs = db.similarity_search(query, k=10)

    filtered_docs = []
    for d in docs:
        if detected_city and detected_city not in d.metadata.get("city", ""):
            continue
        if detected_course and detected_course not in d.metadata.get("course", ""):
            continue
        filtered_docs.append(d)

    if not filtered_docs:
        return "❌ No matching colleges found."

    # 🔥 Intent Handling
    if "exam" in query_lower:
        return format_exam(filtered_docs)

    if "fee" in query_lower or "lowest" in query_lower:
        return format_fees(filtered_docs)

    if "eligibility" in query_lower:
        return format_eligibility(filtered_docs)

    if "scholarship" in query_lower:
        return format_scholarship(filtered_docs)

    if "placement" in query_lower:
        return format_placement(filtered_docs)

    return format_colleges(filtered_docs)
