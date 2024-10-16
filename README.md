# swisspair-python

A python client for https://github.com/karlosss/swisspair - algorithm to pair players according to the Swiss system (not only) for Magic: The Gathering 

## Requirements

- `pybind11`
- `gcc`
- `cmake`
- `gmp`

## Installation

### Pip installation

- `pip install swisspair`

At the moment works only on Linux.

### Local installation

- Requirements: `pybind11`, `gcc`, `cmake`, `gmp`
- Clone the repository
- `python -m build`
- In your project, do `pip install <PATH_TO_THE_CLONED_REPOSITORY>`

### Docker image

If you are on MacOS, you can still use `swisspair` through a dockerized HTTP API. Refer to https://github.com/karlosss/swisspair-python-http-api.

## Usage

The basic interface is as follows:

```python
from swisspair import Player, create_matches

players = [Player(id="P1", points=3, rank=1), Player(id="P2", points=0, rank=2)]

matches = create_matches(players)

print(matches)
```

For all available parameters, please refer to [the interface file](https://github.com/karlosss/swisspair-python/blob/a6cc5011aea4942c7b5296947bbf64d317a3f75a/src/swisspair/interface.py).

## License

MIT, whatever it means. If you like this project, I would be happy for a star :)
