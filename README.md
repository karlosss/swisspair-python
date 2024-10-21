# swisspair-python

A python client for https://github.com/karlosss/swisspair - algorithm to pair players according to the Swiss system (not only) for Magic: The Gathering 

## Requirements

- Linux, MacOS 13 (x86_64) or MacOS 14 (arm)
- Python 3.9+ 

## Installation

### Pip installation

- `pip install swisspair`

### Local build & installation

- Requirements: `pybind11`, `gcc`, `cmake`, `gmp`
- Clone the repository
- `python -m build`
- In your project, do `pip install <PATH_TO_THE_CLONED_REPOSITORY>`

### Docker image

You can also use `swisspair` through a dockerized HTTP API. Refer to https://github.com/karlosss/swisspair-python-http-api.

## Usage

For the details of the algorithm, refer to https://github.com/karlosss/swisspair.

A sample usage below. For all available parameters, please refer to [the interface file](https://github.com/karlosss/swisspair-python/blob/a6cc5011aea4942c7b5296947bbf64d317a3f75a/src/swisspair/interface.py).

```python
from swisspair import Player, create_matches

p1 = Player(id="P1", points=3, rank=1, can_get_bye=True, cannot_be_paired_against_ids={"P3"})
p2 = Player(id="P2", points=3, rank=2, can_get_bye=False, cannot_be_paired_against_ids=set())
p3 = Player(id="P3", points=0, rank=3, can_get_bye=True, cannot_be_paired_against_ids={"P1"})

players = [p1, p2, p3]

matches = create_matches(players)

print(matches)
```

## License

MIT, whatever it means. If you like this project, I would be happy for a star :)
