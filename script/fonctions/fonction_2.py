def aggregation_function_2(collection):

    # Nombre total de buts marqués par club

    aggregation_query_2 = [
        {"$group": {"_id": {"Club": "$Club", "Country": "$Country"}, "total_goals": {"$sum": "$Goals"}}},
        {"$sort": {"total_goals": -1}},
        {"$limit": 20} 
    ]
    result = list(collection.aggregate(aggregation_query_2))
    return result
