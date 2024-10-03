from dataclasses import dataclass

import swisspair

@dataclass
class Player:
    id: str
    previous_opponents_ids: set[str]
    had_bye: bool
    points: int
    rank: int

    def compile(self) -> swisspair.Player:
        p = swisspair.Player()
        p.id = self.id
        p.previous_opponents_ids = self.previous_opponents_ids
        p.had_bye = self.had_bye
        p.points = self.points
        p.rank = self.rank
        return p

    @staticmethod
    def decompile(player: swisspair.Player) -> "Player":
        return Player(id=player.id, previous_opponents_ids=player.previous_opponents_ids, had_bye=player.had_bye, points=player.points, rank=player.rank)

@dataclass
class Match:
    p1: Player
    p2: Player | None

    @staticmethod
    def decompile(match: swisspair.Match) -> "Match":
        return Match(p1=Player.decompile(match.p1), p2=Player.decompile(match.p2) if not match.is_bye else None)

    @property
    def is_bye(self) -> bool:
        return self.p2 is None

def create_matches(players: list[Player], power_pairing: bool) -> list[Match]:
    matches = swisspair.create_matches([p.compile() for p in players], power_pairing)
    return [Match.decompile(m) for m in matches]
