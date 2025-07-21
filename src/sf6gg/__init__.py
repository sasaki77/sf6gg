from sf6gg.ggint import get_tournament_events


def main() -> None:
    data = get_tournament_events("evo-japan-2025-presented-by-levtech")

    tournament = data["data"]["tournament"]
    print(f"Tournament ID: {tournament['id']}")
    print(f"Tournament Name: {tournament['name']}")
    print("Events:")
    for event in tournament["events"]:
        print(f" - {event['name']}")
        print(f" - {event['id']}")
