import os

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from sgqlc.types import ID, Arg, String, Variable

from sf6gg.ggschema import get_schema


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
    op.tournament(slug=Variable("slug"))

    return run_endpoint(op, variables)


def get_event(id: str):
    schema = get_schema()
    variables = {"id": id}

    op = Operation(
        schema.Query,
        variables={
            "id": Arg(ID),
        },
    )
    op.event(id=Variable("id")).__fields__(
        id=True, name=True, standings={"query": {"page": 1, "perPage": 10}}
    )

    return run_endpoint(op, variables)
