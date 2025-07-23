import os

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from sgqlc.types import ID, Arg, String, Variable

from sf6gg.ggschema import ggschema


def get_schema():
    return ggschema


def run_endpoint(op, variables=None):
    url = "https://api.start.gg/gql/alpha"
    api_key = os.environ["SF6GG_API_KEY"]
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    endpoint = HTTPEndpoint(url, headers)
    data = endpoint(op, variables=variables)

    return data


def get_tournament_events(slug: str):
    schema = get_schema()
    variables = {"slug": slug}

    op = Operation(
        schema.Query,
        variables={
            "slug": Arg(String),
        },
    )
    tournament = op.tournament(slug=Variable("slug"))
    tournament.__fields__("id", "name", "start_at")
    events = tournament.events
    events.__fields__("id", "name", "start_at", "num_entrants")  # type: ignore

    return run_endpoint(op, variables)


def get_event_phase(id: str):
    schema = get_schema()
    variables = {"id": id}

    op = Operation(
        schema.Query,
        variables={
            "id": Arg(ID),
        },
    )
    event = op.event(id=Variable("id"))
    event.__fields__("id", "name")
    phases = event.phases  # type: ignore
    phases.__fields__("id", "phase_order", "name")

    return run_endpoint(op, variables)


def get_event_phase_group(event_id: str, phase_id: str, page: int, per_page: int):
    schema = get_schema()
    variables = {
        "eventId": event_id,
        "phaseId": phase_id,
        "page": page,
        "perPage": per_page,
    }

    op = Operation(
        schema.Query,
        variables={
            "eventId": Arg(ID),
            "phaseId": Arg(ID),
            "page": int,
            "perPage": int,
        },
    )
    event = op.event(id=Variable("eventId"))
    event.__fields__("id", "name")
    phases = event.phases(phase_id=Variable("phaseId"))  # type: ignore
    phases.__fields__("id", "phase_order", "name")
    phase_groups = phases.phase_groups(
        query={"page": Variable("page"), "perPage": Variable("perPage")}
    )
    nodes = phase_groups.nodes
    nodes.__fields__("id", "display_identifier", "bracket_url")  # type: ignore
    print(op)

    return run_endpoint(op, variables)


def get_event_entrants(id: str, page=1, per_page=100):
    schema = get_schema()
    variables = {"id": id}

    op = Operation(
        schema.Query,
        variables={
            "id": Arg(ID),
        },
    )
    event = op.event(id=Variable("id"))
    event.__fields__("id", "name")
    standings = event.standings(query={"page": page, "perPage": per_page})  # type: ignore
    # entrants = standings.entrants
    nodes = standings.nodes
    nodes.__fields__("id", "placement")  # type: ignore
    entrant = nodes.entrant  # type: ignore
    entrant.__fields__("id", "name")
    player = nodes.player  # type: ignore
    player.__fields__("id", "gamer_tag", "prefix")

    return run_endpoint(op, variables)


def get_event_sets(id: str, page=1, per_page=100):
    schema = get_schema()
    variables = {"id": id}

    op = Operation(
        schema.Query,
        variables={
            "id": Arg(ID),
        },
    )
    event = op.event(id=Variable("id"))
    event.__fields__("id", "name")
    sets = event.sets(page=page, per_page=per_page)  # type: ignore
    nodes = sets.nodes
    nodes.__fields__("id", "full_round_text", "winner_id", "display_score", "round")  # type: ignore
    # game = nodes.game
    # game.__fields__("id")
    phase_group = nodes.phase_group  # type: ignore
    phase_group.__fields__("id", "display_identifier", "bracket_url")
    phase = phase_group.phase
    phase.__fields__("id", "phase_order", "name")
    slots = nodes.slots  # type: ignore
    slots.__fields__("id")
    entrant = slots.entrant
    entrant.__fields__("id", "name")
    print(op)

    return run_endpoint(op, variables)
