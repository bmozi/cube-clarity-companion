# How to Master the Cube — companion lessons and practice

Learn the 2×2, explore blindfold solving, investigate cube mathematics, or run checked practice examples. These optional lessons extend **How to Master the Cube** by **John Briggs**. The book contains its complete 3×3 courses and quick guides; this repository is not required to finish them.

Updated **November 25, 2026**. Canonical public companion: [github.com/bmozi/cube-clarity-companion](https://github.com/bmozi/cube-clarity-companion).

## What can I learn here without installing anything?

| Your next interest | Start here | What is included |
| --- | --- | --- |
| Solve a 2×2 | [Complete beginner course](docs/2x2-course.md) | Color frame, insertion, yellow orientation, corner order, eight original illustrations, full worked trace and recovery |
| Solve from memory | [Blindfold course](docs/blindfold-course.md) | Separate letter maps, all 43 directed target rows, parity bridge and three worked examples |
| Understand mathematical limits and shorter routes | [Mathematics and shorter solutions](docs/mathematics-and-shorter-solutions.md) | Move order, inverses, legal-state constraints, counting and a checked superflip demonstration |
| Understand computer solvers | [Computer-solving lesson](docs/computer-solving.md) | Cubie representation, validation, bounded IDA*, heuristics and two-phase architecture |
| Explore controlled changes | [Conjugates and three-cycles](docs/controlled-changes.md) | Exact experiments, protected-work checks and limits of transferring a sequence |
| Improve case practice | [Recognition and diagnostic practice](docs/3x3-case-practice.md) | Full-pattern comparison, joined versus joining pairs, recall, drills and transfer |

Start with [notation and grip](docs/notation.md) if needed. All lessons and images can be read on GitHub or downloaded for offline reading. The complete 2×2 course is here rather than in the reader editions of the book. Later blindfold methods such as M2 and three-style are introduced as next interests, not complete courses or interchangeable algorithms.

## How do I run the optional examples?

Install Python **3.10 or later** if needed. Download and extract the repository ZIP, open a terminal at its root, and run:

```sh
python3 examples/pocket_practice.py --scramble "R U F2"
python3 examples/case_practice.py --list --family pll
python3 examples/case_practice.py --case F2L-026 --show-setup
python3 examples/blindfold_practice.py --scramble "F"
python3 examples/solve_cube.py --scramble "R U F2"
python3 -m unittest discover -s tests -v
```

On Windows use `python` or `py` if that is your installed launcher. No additional packages, API keys or network connection are needed after download. Run commands from this folder, not from `src`. Each script supports `--help`.

Start solved in the stated grip before applying an example’s scramble or setup. Never add a practice setup to a cube that is already mixed. A whole-cube y changes the reference frame; a U turn moves only the top layer. A different valid solution can also be correct.

The 2×2 example prints every step of the lesson’s worked route and checks all 24 corner stickers in the final rotated frame. The blindfold example checks all 54 stickers after edges, the parity bridge when needed, and corners. The case tool reveals the complete route only after you inspect its pattern; use `--hide-answer` for recognition practice.

The computer solver is bounded educational IDA* for short examples. Exhausting its depth or node budget means **incomplete search**, not an impossible cube. It is not a practical fast solver for arbitrary long scrambles. The two-phase lesson explains a stronger architecture; this repository does not implement a production two-phase backend.

## What is checked, and what remains untested?

Tests replay moves and protected work, exercise all 119 case routes, all directed blindfold targets, randomized complete 2×2 and blindfold solves, legality constraints and shallow search comparisons. Stable project IDs coexist with conventional OLL numbers and PLL names. Several last-layer routes use source-attributed reference choices; provenance is retained in the data.

Model correctness is separate from comfortable hand execution, teaching effectiveness and speed. Independent physical ergonomics and learner trials remain pending. No fastest-route, competition result or guaranteed learning-time claim is made. Keep each lesson’s grip, full sequence, stopping rule and recovery together. Do not force turns or twist pieces; stop if turning hurts.

## Authorship, sources and corrections

Lessons, original diagrams and project code are by John Briggs, with AI assistance in drafting, illustration development and computational verification. John Briggs is responsible for the published material. [Sources and provenance](docs/sources-and-provenance.md) distinguish original project work from research and algorithm references. [Changes](CHANGELOG.md) describe companion maintenance without implying a new book edition.

Report a problem through [repository issues](https://github.com/bmozi/cube-clarity-companion/issues). Include the lesson or case ID, starting grip, exact scramble and moves, expected checkpoint and observed result. Do not include personal information. A physical execution report is useful even if the model replay passes.

Copyright © 2026 John Briggs. All rights reserved. No open-source license is implied. Supplied as educational material without warranties. This public companion contains selected, author-authorized standalone lessons, instructional figures, practice code and reference data; it does not include the private print/Kindle manuscript, covers, production tools or review files.
