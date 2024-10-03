import sys
sys.path.append("src/pyswisspair")

from src.pyswisspair import Player, create_matches

players = []

for i in range(100):
    players.append(
        Player(
            id="P" + str(i),
            previous_opponents_ids=set(),
            had_bye=False,
            points=i,
            rank=i+1,
        )
    )

import time
start = time.time()
matches = create_matches(players, True)
duration = time.time()-start

print(duration)

for table_number, match in enumerate(matches):
    print(table_number+1, match)
