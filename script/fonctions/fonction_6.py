def aggregation_function_6(collection):
    
    # Moyenne de but par match par joueurs
    aggregation_query_6 = [
        {"$group": {"_id": "$Player Names", "total_goals": {"$sum": "$Goals"}, "total_matches": {"$sum": "$Matches_Played"}}},
        {"$project": {"_id": 1, "goals_per_match": {"$divide": ["$total_goals", "$total_matches"]}}},
        {"$sort": {"goals_per_match": -1}},
        {"$limit": 20}
    ]
    result = list(collection.aggregate(aggregation_query_6))
    return result