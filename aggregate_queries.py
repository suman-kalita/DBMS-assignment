def nl_to_sql_v4(query):
    query = query.lower()
    agg_map = {
        "average": "AVG",
        "avg": "AVG",
        "maximum": "MAX",
        "highest": "MAX",
        "minimum": "MIN",
        "lowest": "MIN",
        "count": "COUNT"
    }
    for word, sql_func in agg_map.items():
        if word in query:
            if sql_func == "COUNT":
                return "SELECT COUNT(*) FROM students;"
            else:
                return f"SELECT {sql_func}(marks) FROM students;"
    return "Unsupported aggregation query."