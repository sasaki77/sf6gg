from datetime import datetime
from pprint import pprint

import click

from sf6gg.crud import (
    add_entrants,
    add_phase,
    add_phase_groups,
    add_players,
    add_sets,
    create_event,
    get_sets_by_player_and_event,
)
from sf6gg.database import db
from sf6gg.ggint import (
    get_event_entrants,
    get_event_phase,
    get_event_phase_group,
    get_event_sets,
    get_tournament_events,
)


@click.group()
@click.version_option(package_name="sf6gg", message="%(prog)s %(version)s")
def cli():
    pass


@cli.command()
@click.argument("slug")
def tournament(slug):
    data = get_tournament_events(slug)

    tournament = data["data"]["tournament"]
    print(tournament)
    print(f"Tournament ID: {tournament['id']}")
    print(f"Tournament Name: {tournament['name']}")
    print(f"Tournament Start Date: {datetime.fromtimestamp(tournament['startAt'])}")
    print("Events:")
    for event in tournament["events"]:
        print(
            f" - {event['id']}, {datetime.fromtimestamp(event['startAt'])}, {event['numEntrants']}, {event['name']}"
        )


@cli.command()
@click.option("--page", "-p", "page", type=int, default=1)
@click.option("--pagePage", "-P", "per_page", type=int, default=100)
@click.argument("id", type=int)
def standing(id, page, per_page):
    data = get_event_entrants(id, page, per_page)

    event = data["data"]["event"]
    print(f"Event name: {event['name']}")
    print("Standings:")
    for standing in event["standings"]["nodes"]:
        print(standing)


@cli.command()
@click.argument("id", type=int)
def phase(id):
    data = get_event_phase(id)

    event = data["data"]["event"]
    print(f"Event name: {event['name']}")
    print("Standings:")
    for phase in event["phases"]:
        print(phase)


@cli.command()
@click.option("--page", "-p", "page", type=int, default=1)
@click.option("--pagePage", "-P", "per_page", type=int, default=100)
@click.argument("event_id", type=int)
@click.argument("phase_id", type=int)
def phaseGroup(event_id, phase_id, page, per_page):
    data = get_event_phase_group(event_id, phase_id, page, per_page)

    event = data["data"]["event"]
    print(f"Event name: {event['name']}")
    pprint(event)


@cli.command()
@click.option("--page", "-p", "page", type=int, default=1)
@click.option("--pagePage", "-P", "per_page", type=int, default=100)
@click.argument("id", type=int)
def sets(id, page, per_page):
    data = get_event_sets(id, page, per_page)

    event = data["data"]["event"]
    print(f"Event name: {event['name']}")
    print("Sets:")
    for set in event["sets"]["nodes"]:
        pprint(set)


@cli.command()
@click.argument("url", type=str)
def init(url):
    db.init_engine(url)
    db.init()


@cli.command()
@click.argument("url", type=str)
@click.argument("event", type=int)
@click.argument("player", type=int)
def test(url, event, player):
    db.init_engine(url)
    session = db.get_session()
    if session is None:
        raise
    sets = get_sets_by_player_and_event(session, event, player)
    for s in sets:
        print(
            f"Round {s.round}: Entrant {s.p1.name} vs {s.p2.name} → Score {s.p1score}-{s.p2score} (Winner: {s.winner.name})"
        )


@cli.command()
@click.argument("url", type=str)
def mock(url):
    db.init_engine(url)
    session = db.get_session()
    if session is None:
        raise

    # イベント
    event = create_event(
        session, id=1, name="Mock Championship", start=datetime(2025, 8, 1, 12, 0)
    )

    # プレイヤー
    pdata = [
        {"id": 1, "tag": "Falcon"},
        {"id": 2, "tag": "Zeta"},
        {"id": 3, "tag": "Nova"},
        {"id": 4, "tag": "Echo"},
    ]
    players = add_players(session, pdata)

    # エントラント
    entrants_list = []
    for i, p in enumerate(pdata, start=1):
        entrant = {
            "id": i,
            "entrant_id": i,
            "event_id": event.id,
            "player_id": p["id"],
            "placement": i,
            "name": f"Team {p['tag']}",
        }
        entrants_list.append(entrant)
    entrants = add_entrants(session, entrants_list)

    # フェーズ
    phase1 = add_phase(session, event_id=event.id, order=1, name="予選")
    phase2 = add_phase(session, event_id=event.id, order=2, name="決勝")

    # フェーズグループ
    phases = [
        {
            "id": 1,
            "phase_id": phase1.id,
            "name": "Group A",
            "url": "https://mock.gg/groupA",
        },
        {
            "id": 2,
            "phase_id": phase2.id,
            "name": "Group B",
            "url": "https://mock.gg/groupB",
        },
    ]
    p = add_phase_groups(session, phases)
    group_a, group_b = p

    # 試合（Set）
    sets = [
        {
            "id": 1,
            "event_id": event.id,
            "phase_group_id": group_a.id,
            "p1id": entrants[0].id,
            "p1score": 2,
            "p2id": entrants[1].id,
            "p2score": 1,
            "winner_id": entrants[0].id,
            "round": 1,
        },
        {
            "id": 2,
            "event_id": event.id,
            "phase_group_id": group_b.id,
            "p1id": entrants[2].id,
            "p1score": 0,
            "p2id": entrants[3].id,
            "p2score": 1,
            "winner_id": entrants[3].id,
            "round": 1,
        },
    ]
    add_sets(session, sets)

    session.close()


if __name__ == "__main__":
    cli()
