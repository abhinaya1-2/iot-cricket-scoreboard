from fetch_score import fetch_live_score


def display_scoreboard():
    match = fetch_live_score()

    team_1 = match["team_1"]
    team_2 = match["team_2"]
    venue = match["venue"]
    status = match["status"]

    score = match["score"]
    batsmen = match["batsmen"]
    bowler = match["bowler"]

    print("=" * 50)
    print("        IoT CRICKET SCOREBOARD")
    print("=" * 50)

    print(f"Match: {team_1} vs {team_2}")
    print(f"Venue: {venue}")
    print(f"Status: {status}")

    print("-" * 50)
    print(f"{score['team']}: {score['runs']}/{score['wickets']} in {score['overs']} overs")

    print("-" * 50)
    print("Current Batsmen:")
    for batsman in batsmen:
        print(f"{batsman['name']} - {batsman['runs']} runs ({batsman['balls']} balls)")

    print("-" * 50)
    print("Current Bowler:")
    print(f"{bowler['name']} - {bowler['overs']} overs, {bowler['wickets']} wickets")

    print("=" * 50)


if __name__ == "__main__":
    display_scoreboard()
