# swisspair-python

A python client for https://github.com/karlosss/swisspair.

## Requirements

- `pybind11`
- `gcc`
- `cmake`
- `gmp`

## Installation

### Local installation

- Clone the repository
- In your project, do `pip install <PATH_TO_THE_CLONED_REPOSITORY>`

### Pip installation

- `pip install swisspair`

### Docker image

Because `pybind11` can be pain on some distributions (looking at you, Ubuntu), there is a docker image based on
ArchLinux with python and swisspair module.

TODO publish the image

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
