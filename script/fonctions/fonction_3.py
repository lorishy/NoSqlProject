def aggregation_function_3(collection):
    
    # Nombre total de buts par ligue

    aggregation_query_3 = [
    {"$group": {"_id": "$League", "total_goals": {"$sum": "$Goals"}}}
]
    result = list(collection.aggregate(aggregation_query_3))
    return result