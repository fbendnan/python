data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
            "region": "north",
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
            "region": "east",
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4,
            "region": "east",
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7,
            "region": "east",
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1,
            "region": "north",
        },
    },
    "sessions": [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 2361,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 2985,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 34,
            "score": 1285,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 1238,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 1555,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 92,
            "score": 2754,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 98,
            "score": 1102,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 39,
            "score": 2721,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 46,
            "score": 329,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 56,
            "score": 1196,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 1388,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 118,
            "score": 2733,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 22,
            "score": 1110,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 79,
            "score": 1854,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "charlie",
            "duration_minutes": 33,
            "score": 666,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 101,
            "score": 292,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 25,
            "score": 2887,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 53,
            "score": 2540,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 115,
            "score": 147,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 118,
            "score": 2299,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 97,
            "score": 1178,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 18,
            "score": 2661,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 761,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 46,
            "score": 2101,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1359,
            "mode": "casual",
            "completed": True,
        },
    ],
    "game_modes": ["casual", "competitive", "ranked"],
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer",
    ],
}


def active_players_analytics():
    high_players = []
    scorers_doubled = []
    active_players = []
    for player, info in data["players"].items():
        if info["total_score"] > 2000:
            high_players += [player]
        if info["sessions_played"] > 25:
            active_players += [player]
        scorers_doubled += [info["total_score"] * 2]

    return high_players, scorers_doubled, active_players


def list_comprehension_ex():
    print("=== List Comprehension Examples ===")
    high_players, scorers_doubled, active_players = active_players_analytics()
    print(f"High scorers (>2000): {high_players}")
    print(f"Scores doubled: {scorers_doubled}")
    print(f"Active players: {active_players}")
    return sum(scorers_doubled) / 2


def dict_comprehension_ex():
    players_scores = {}
    players_achievement_count = {}
    score_categories = {"high": 0, "medium": 0, "low": 0}
    for player, info in data["players"].items():
        players_scores[player] = info["total_score"]
        players_achievement_count[player] = info["achievements_count"]

    for player, score in players_scores.items():
        if score > 5000:
            score_categories["high"] += 1
        elif score > 2000:
            score_categories["medium"] += 1
        else:
            score_categories["low"] += 1

    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {players_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {players_achievement_count}")
    return players_scores


def set_comprehension_ex():
    print("=== Set Comprehension Examples ===")
    unique_players = set()
    unique_achievement = set()
    active_region = set()
    for player, info in data["players"].items():
        unique_players.add(player)
        active_region.add(info["region"])

    for achievement in data["achievements"]:
        unique_achievement.add(achievement)

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievement}")
    print(f"Active regions: {active_region}")


def game_dashboard():
    print("=== Game Analytics Dashboard ===")
    print()
    total_scorers = list_comprehension_ex()
    print()
    players_scores = dict_comprehension_ex()
    print()
    set_comprehension_ex()
    print()
    print("=== Combined Analysis ===")
    total_players = len(data["players"])
    average_score = total_scorers / total_players
    sorted_players_scores = dict(
        sorted(players_scores.items(), key=lambda item: item[1], reverse=True)
    )
    name_player = list(sorted_players_scores)
    print(sorted_players_scores)
    print(
        f"Total players: {total_players}\n"
        f"Total unique achievements: {len(data["achievements"])}\n"
        f"Average score: {average_score:.1f}\n"
        f"Top performer: {name_player[0]} "
        f"({sorted_players_scores[name_player[0]]} points, "
        f"{data['players'][name_player[0]]["achievements_count"]} "
        f"achievements)\n"
    )


def main():
    game_dashboard()


main()
