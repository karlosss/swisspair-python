import sys
sys.path.append("src/pyswisspair")

from src.pyswisspair import Player, create_matches

players = []

n = 9999

for i in range(n):
    players.append(
        Player(
            id="P" + str(i),
            can_get_bye=True,
            points=n-i // 20,
            rank=i+1,
        )
    )

import time
start = time.time()
matches = create_matches(players, False)
duration = time.time()-start

for table_number, match in enumerate(matches):
    print(table_number+1, match)

print(duration)
