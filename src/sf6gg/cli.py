import click

from sf6gg.ggint import get_event, get_tournament_events


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
    print("Events:")
    for event in tournament["events"]:
        print(f" - {event['id']}, {event['name']}")


@cli.command()
@click.argument("id", type=int)
def event(id):
    data = get_event(id)

    event = data["data"]["event"]
    print(f"Event name: {event['name']}")
    print("Standings:")
    for standing in event["standings"]["nodes"]:
        print(f" - {standing['id']}, {standing['placement']}")


if __name__ == "__main__":
    cli()
