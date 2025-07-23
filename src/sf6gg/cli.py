from datetime import datetime
from pprint import pprint

import click

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


if __name__ == "__main__":
    cli()
