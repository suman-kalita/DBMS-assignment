import re

def nl_to_sql(query):
    query = query.lower()
    sql = "SELECT * FROM students"
    conditions = []

    # Marks conditions
    marks_ops = {
        "above": ">",
        "greater than": ">",
        "below": "<",
        "less than": "<",
        "equal": "=",
        "equals": "=",
        "equal to": "=",
        "not equal": "!="
    }
    for key, op in marks_ops.items():
        if key in query:
            number = re.findall(r'\d+', query)[0]
            conditions.append(f"marks {op} {number}")
            break

    # Age conditions
    if "older than" in query:
        number = re.findall(r'\d+', query)[0]
        conditions.append(f"age > {number}")
    if "younger than" in query:
        number = re.findall(r'\d+', query)[0]
        conditions.append(f"age < {number}")

    # Grade conditions
    if "grade" in query:
        match = re.search(r'grade\s+([a-z])', query)
        if match:
            grade = match.group(1).upper()
            conditions.append(f"grade = '{grade}'")

    # Combine conditions with AND / OR
    if "and" in query:
        sql += " WHERE " + " AND ".join(conditions)
    elif "or" in query:
        sql += " WHERE " + " OR ".join(conditions)
    elif conditions:
        sql += " WHERE " + " AND ".join(conditions)

    sql += ";"
    return sql

queries = [
    "Show students with marks above 80 and older than 20",
    "List students younger than 18 or with grade B",
    "Find students with marks equal to 90 and grade A"
]

for q in queries:
    print("Input:", q)
    print("Output:", nl_to_sql(q))
    print()