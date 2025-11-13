import re

def nl_to_sql(query):
    query = query.lower()
    sql = "SELECT * FROM students"
    
    conditions = {
        "above": ">",
        "greater than": ">",
        "below": "<",
        "less than": "<",
        "equal": "=",
        "equals": "=",
        "equal to": "=",
        "not equal": "!="
    }

    for key, op in conditions.items():
        if key in query:
            number = re.findall(r'\d+', query)[0]
            sql += f" WHERE marks {op} {number};"
            return sql

    return sql + ";"

queries = [
    "Show all students with marks above 80",
    "List all students with marks less than 50",
    "Find students with marks equal to 90",
    "Get students with marks not equal to 60"
]

for q in queries:
    print("Input:", q)
    print("Output:", nl_to_sql(q))
    print()