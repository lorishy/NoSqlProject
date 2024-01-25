def aggregation_function_5(collection):
    
    # Moyenne de but par match par pays
    aggregation_query_5 = [
        {"$group": {"_id": "$Country", "total_goals": {"$sum": "$Goals"}, "total_matches": {"$sum": "$Matches_Played"}}},
        {"$project": {"_id": 1, "goals_per_match": {"$divide": ["$total_goals", "$total_matches"]}}},
        {"$sort": {"goals_per_match": -1}},
        {"$limit": 20}
    ]
    result = list(collection.aggregate(aggregation_query_5))
    return result