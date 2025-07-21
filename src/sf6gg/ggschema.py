from sgqlc.types import ID, Arg, Field, Input, Schema, Type, list_of


class Standing(Type):
    id = ID
    placement = Field(int)


class PageInfo(Type):
    total = Field(int)
    totalPages = Field(int)
    page = Field(int)
    perPage = Field(int)
    sortBy = Field(str)
    filter = Field(str)


class StandingConnection(Type):
    pageInfo = Field(PageInfo)
    nodes = Field(list_of(Standing))


class StandingPaginationQuery(Input):
    page = Field(int)
    perPage = Field(int)
    sortBy = Field(str)


class Event(Type):
    id = ID
    name = Field(str)
    standings = Field(StandingConnection, args={"query": Arg(StandingPaginationQuery)})


class Tournament(Type):
    id = ID
    name = Field(str)
    events = Field(list_of(Event))


class Query(Type):
    tournament = Field(Tournament, args={"slug": str})
    event = Field(Event, args={"id": ID})


def get_schema():
    schema = Schema()
    schema.query_type = Query
    return schema
