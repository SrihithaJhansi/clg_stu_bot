import pandas as pd

def load_data():
    df = pd.read_csv("data/colleges.csv")

    documents = []

    for _, row in df.iterrows():
        text = f"""
College: {row['College Name']}
Course: {row['Course']}
Location: {row['Location']}

Fees: {row['Fees (INR/year)']}
Ranking: {row['Ranking']}
Average Package: {row['Average Package (LPA)']} LPA
Placement: {row['Average Placement %']}%

This college offers {row['Course']} in {row['Location']} with fees {row['Fees (INR/year)']}.
"""

        metadata = {
            "college": row["College Name"],
            "course": row["Course"]
        }

        documents.append((text, metadata))

    return documents