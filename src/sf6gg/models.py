from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = "event"
    id: Mapped[int] = mapped_column(primary_key=True)
    start: Mapped[datetime]
    name: Mapped[str]

    phases: Mapped[list["Phase"]] = relationship(back_populates="event")
    entrants: Mapped[list["Entrant"]] = relationship(back_populates="event")
    sets: Mapped[list["Set"]] = relationship(back_populates="event")


class Player(Base):
    __tablename__ = "player"
    id: Mapped[int] = mapped_column(primary_key=True)
    tag: Mapped[str]

    entrants: Mapped[list["Entrant"]] = relationship(back_populates="player")


class Phase(Base):
    __tablename__ = "phase"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"))
    order: Mapped[int]
    name: Mapped[str]

    event: Mapped["Event"] = relationship(back_populates="phases")
    phase_groups: Mapped[list["PhaseGroup"]] = relationship(back_populates="phase")


class PhaseGroup(Base):
    __tablename__ = "phase_group"
    id: Mapped[int] = mapped_column(primary_key=True)
    phase_id: Mapped[int] = mapped_column(ForeignKey("phase.id"))
    url: Mapped[str]
    name: Mapped[str]

    phase: Mapped["Phase"] = relationship(back_populates="phase_groups")
    sets: Mapped[list["Set"]] = relationship(back_populates="phase_group")


class Entrant(Base):
    __tablename__ = "entrant"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"))
    entrant_id: Mapped[int]
    player_id: Mapped[int] = mapped_column(ForeignKey("player.id"))
    placement: Mapped[int]
    name: Mapped[str]

    event: Mapped["Event"] = relationship(back_populates="entrants")
    player: Mapped["Player"] = relationship(back_populates="entrants")

    sets_p1: Mapped[list["Set"]] = relationship(
        "Set", foreign_keys="[Set.p1id]", back_populates="p1"
    )
    sets_p2: Mapped[list["Set"]] = relationship(
        "Set", foreign_keys="[Set.p2id]", back_populates="p2"
    )
    sets_won: Mapped[list["Set"]] = relationship(
        "Set", foreign_keys="[Set.winner_id]", back_populates="winner"
    )


class Set(Base):
    __tablename__ = "set"
    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"))
    phase_group_id: Mapped[int] = mapped_column(ForeignKey("phase_group.id"))
    p1id: Mapped[int] = mapped_column(ForeignKey("entrant.id"))
    p1score: Mapped[int]
    p2id: Mapped[int] = mapped_column(ForeignKey("entrant.id"))
    p2score: Mapped[int]
    winner_id: Mapped[int] = mapped_column(ForeignKey("entrant.id"))
    round: Mapped[int]

    event: Mapped["Event"] = relationship(back_populates="sets")
    phase_group: Mapped["PhaseGroup"] = relationship(back_populates="sets")
    p1: Mapped["Entrant"] = relationship(foreign_keys=[p1id], back_populates="sets_p1")
    p2: Mapped["Entrant"] = relationship(foreign_keys=[p2id], back_populates="sets_p2")
    winner: Mapped["Entrant"] = relationship(
        foreign_keys=[winner_id], back_populates="sets_won"
    )
