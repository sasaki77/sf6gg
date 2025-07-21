from sgqlc.types import Field, Schema, Type, list_of


class Event(Type):
    id = Field(int)
    name = Field(str)


class Tournament(Type):
    id = Field(int)
    name = Field(str)
    events = Field(list_of(Event))


class Query(Type):
    tournament = Field(Tournament, args={"slug": str})


def get_schema():
    schema = Schema()
    schema.query_type = Query
    return schema
