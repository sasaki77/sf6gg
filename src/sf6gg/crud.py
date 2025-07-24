from datetime import datetime

from sqlalchemy.orm import Session, joinedload

from sf6gg.models import Entrant, Event, Phase, PhaseGroup, Player, Set


def create_event(db: Session, id: int, name: str, start: datetime):
    event = Event(id=id, name=name, start=start)
    db.add(event)
    db.commit()
    return event


def add_players(db: Session, players: list):
    # players_data = [Player(id=player["id"], tag=player["tag"]) for player in players]
    ret = []
    for player in players:
        p = Player(id=player["id"], tag=player["tag"])
        ret.append(p)
        db.add(p)
    db.commit()
    return ret


def add_entrants(db: Session, entrants: list):
    entrtrants_data = []
    for entrant in entrants:
        e = Entrant(
            id=entrant["id"],
            event_id=entrant["event_id"],
            entrant_id=entrant["entrant_id"],
            player_id=entrant["player_id"],
            placement=entrant["placement"],
            name=entrant["name"],
        )
        print(e)
        entrtrants_data.append(e)
        db.add(e)
    db.commit()
    return entrtrants_data


def add_phase(db: Session, event_id: int, order: int, name: str):
    phase = Phase(event_id=event_id, order=order, name=name)
    db.add(phase)
    db.commit()
    return phase


def add_phase_groups(db: Session, groups):
    phase_groups = []
    for group in groups:
        g = PhaseGroup(
            id=group["id"],
            phase_id=group["phase_id"],
            name=group["name"],
            url=group["url"],
        )
        phase_groups.append(g)
        db.add(g)
    db.commit()
    return phase_groups


def add_sets(db: Session, sets):
    sets_data = []
    for set in sets:
        s = Set(
            id=set["id"],
            event_id=set["event_id"],
            phase_group_id=set["phase_group_id"],
            p1id=set["p1id"],
            p1score=set["p1score"],
            p2id=set["p2id"],
            p2score=set["p2score"],
            winner_id=set["winner_id"],
            round=set["round"],
        )
        sets_data.append(s)
        db.add(s)
    db.commit()
    return sets_data


def get_sets_by_player_and_event(db: Session, player_id: int, event_id: int):
    return (
        db.query(Set)
        .options(
            joinedload(Set.p1),
            joinedload(Set.p2),
            joinedload(Set.winner),
        )
        .join(
            Entrant,
            (
                (Set.p1id == Entrant.id)
                | (Set.p2id == Entrant.id)
                | (Set.winner_id == Entrant.id)
            ),
        )
        .filter(Entrant.player_id == player_id)
        .filter(Set.event_id == event_id)
        .all()
    )
