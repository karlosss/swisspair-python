def GivenSwisspairLibrary_WhenImported_ThenNoError():
    import swisspair

    assert swisspair.__all__


def GivenTwoPlayers_WhenMatchesCreated_ThenPaired():
    import swisspair
    players = [swisspair.Player("P1", points=3, rank=1), swisspair.Player("P2", points=0, rank=2)]

    matches = swisspair.create_matches(players)

    assert len(matches) == 1
    assert matches[0].p1 == players[0]
    assert matches[0].p2 == players[1]
