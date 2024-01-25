def aggregation_function_1(collection):
    
    # Nombre de joueurs et de matchs joués par pays

    aggregation_query_1 = [
    {"$group": {"_id": "$Country", "total_players": {"$sum": 1}, "total_matches_played": {"$sum": "$Matches_Played"}}},
    {"$sort": {"total_players": -1, "total_matches_played": -1}}
]
    result = list(collection.aggregate(aggregation_query_1))
    return result