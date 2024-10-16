from dataclasses import dataclass, field

from ._swisspair import Player as _Player, Match as _Match, create_matches as _create_matches

@dataclass
class Player:
    id: str
    points: int
    rank: int
    can_get_bye: bool = True
    cannot_be_paired_against_ids: set[str] = field(default_factory=set)

    def compile(self) -> _Player:
        p = _Player()
        p.id = self.id
        p.cannot_be_paired_against_ids = self.cannot_be_paired_against_ids
        p.can_get_bye = self.can_get_bye
        p.points = self.points
        p.rank = self.rank
        return p

    @staticmethod
    def decompile(player: _Player) -> "Player":
        return Player(id=player.id, cannot_be_paired_against_ids=player.cannot_be_paired_against_ids, can_get_bye=player.can_get_bye, points=player.points, rank=player.rank)

@dataclass
class Match:
    p1: Player
    p2: Player | None

    @staticmethod
    def decompile(match: _Match) -> "Match":
        return Match(p1=Player.decompile(match.p1), p2=Player.decompile(match.p2) if not match.is_bye else None)

    @property
    def is_bye(self) -> bool:
        return self.p2 is None


def _validate_players(players: list[Player]) -> None:
    id_to_player = {p.id: p for p in players}
    assert len(id_to_player) == len(players), "Player IDs must be unique"

    for i in range(len(players)):
        assert players[i].rank == i+1, "Players must be ranked 1, 2, 3, ..."

        if i > 0:
            assert players[i].points <= players[i-1].points, "Points must not increase as the ranks decrease"

        for cannot_id in players[i].cannot_be_paired_against_ids:
            assert cannot_id in id_to_player, "Nonexistent player ID in cannot-be-paired-against set"
            assert players[i].id in id_to_player[cannot_id].cannot_be_paired_against_ids, "cannot-be-paired-against must be symmetric"


def create_matches(players: list[Player], power_pairing: bool = False) -> list[Match]:
    _validate_players(players)
    matches = _create_matches([p.compile() for p in players], power_pairing)
    return [Match.decompile(m) for m in matches]
