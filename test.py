from interface import Player, create_matches

players = []

for i in range(100):
    players.append(
        Player(
            id="P" + str(i),
            previous_opponents_ids=set(),
            had_bye=False,
            points=i % 20,
            rank=i+1,
        )
    )

matches = create_matches(players, False)

for table_number, match in enumerate(matches):
    print(table_number+1, match)
