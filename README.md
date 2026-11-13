# How to Master the Cube — reader examples

Practice code for John Briggs's illustrated book. This package contains no book
manuscript, cover art, customer data or credentials. Python 3.10 or later is the
only requirement; no packages, network connection or API keys are needed.

Download and extract the ZIP, open a terminal in this folder, then run:

```sh
python3 examples/solve_cube.py --scramble "R U F2"
python3 examples/pocket_practice.py --scramble "R U F2"
python3 -m unittest discover -s tests -v
```

The 2×2 pocket practice command prints the complete Chapter 16 worked route.
Its y rows turn the whole puzzle; other letters turn one face. It checks all
24 corner stickers in the final rotated frame. This is a learning route, not
a shortest-solution or competition-speed claim.

The book writes `python` in its sample command. On macOS and Linux, use
`python3`; on Windows, use `python` or `py` if that is what your installer
provides. All refer to the same Python 3 program.

Start with a solved cube, keep yellow up and green front, and make the scramble.
The program returns a legal move sequence; apply that sequence and inspect all
six faces. A different valid solution can be correct. An incomplete result means
the depth or node budget ran out; it does not mean your cube is impossible.

The solver is an educational bounded IDA* implementation for short examples,
not a fast arbitrary-scramble service. src/cube_clarity contains the independent
sticker/cubie models and blindfold planning. data contains tested reference routes.
Project IDs are stable; OLL numbers and PLL names are independently mapped.
Long working constructions are not claims of fastest human execution.

Run `python3 examples/solve_cube.py --help` for options. If Python is not found,
install Python from python.org and reopen the terminal. If a result differs from
your physical cube, first check the reference grip, prime direction and complete
sequence. Keep the book's stated checkpoints beside the experiment.

Copyright © 2026 John Briggs. All rights reserved. No open-source license is
implied. These examples are supplied as educational material without warranties.
