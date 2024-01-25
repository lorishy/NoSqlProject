def aggregation_function_4(collection):
    
    # Moyenne des minutes jouées par joueur
    aggregation_query_4 = [
    {"$group": {"_id": "$Player Names", "avg_minutes_played": {"$avg": "$Mins"}}},
    {"$sort": {"avg_minutes_played": -1}},
    {"$limit": 20} 
]
    result = list(collection.aggregate(aggregation_query_4))
    return result