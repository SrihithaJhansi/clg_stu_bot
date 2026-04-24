import pandas as pd
import os

def load_data():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "colleges.csv")

    df = pd.read_csv(file_path)

    documents = []

    for _, row in df.iterrows():
        text = f"""
{row['College_Name']} is located in {row['District']}, {row['State']}.

Course: {row['Preferred_Course']} ({row['Preferred_Stream']})
UG Fee: {row['UG_Fee']} INR per year
Rating: {row['Ratings']}
Entrance Exam: {row['Entrance_Exam_Name']}
"""

        metadata = {
    "college": str(row["College_Name"]).strip(),
    "city": str(row["District"]).strip().lower(),
    "course": str(row["Preferred_Course"]).strip().lower(),
    "exam": str(row["Entrance_Exam_Name"]).strip().lower(),
    "fee": int(row["UG_Fee"]),
    "rating": float(row["Ratings"]),
    "rank": int(row["Entrance_Exam_Rank"]),
    "percentage": float(row["12th_Percentage"]),
    "scholarship": str(row["Scholarship_Status"]).lower(),
    "placement": int(row["Placement"])
}

        documents.append((text, metadata))

    return documents