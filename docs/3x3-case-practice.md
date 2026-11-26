# How should I practise a 3×3 case instead of memorizing blindly?

John Briggs · Updated November 25, 2026

Choose one useful pattern, explain its grip, execute the full route and inspect the result. This optional companion contains 41 F2L, 57 OLL and 21 PLL cases with the book’s stable IDs. Conventional OLL numbers and PLL names appear where mapped; an ID is not a skill level or a list to memorize in order.

From the repository root:

```sh
python3 examples/case_practice.py --list --family oll
python3 examples/case_practice.py --case OLL-001 --hide-answer
python3 examples/case_practice.py --case OLL-001
python3 examples/case_practice.py --case F2L-026 --show-setup
```

The tool shows exact face grids in a fixed frame: yellow up, green front and orange right. W/Y/G/B/O/R mean white/yellow/green/blue/orange/red. Each grid looks straight at its own face, including the back. Face letters name positions; color letters name stickers. The displayed case is generated from solved. `--show-setup` reveals practice moves to reproduce it; apply those only to a solved cube. Never add a practice setup to an already mixed solve.

Use [notation and grip](notation.md). On a real mixed cube, match the full relevant pattern before choosing a route. The program does not inspect photographs or identify an arbitrary real cube for you.

## Distinguish a joined pair from pieces that join during an opening

F2L-026 begins with a genuinely joined corner-edge pair. Its setup from solved is `R U R'`; the solution `R U' R'` keeps those pieces joined as it inserts them. Both side colors must agree, not merely touch.

F2L-016 begins with separated pieces. Its setup is `R U' R'` and its solution is `R U R'`. During that solution the first R joins the pieces and temporarily opens the slot; after R alone the right cross edge is displaced. Judge restoration after the complete route, not at that intermediate picture.

`data/learning_transfer_cases.json` records four contrasting practice jobs: joined, join-then-insert, white up and a trapped edge. Choose one, predict the next group’s purpose, then inspect the target and protected work. Group separators add no moves. Some are reading aids without an intermediate-restoration promise; follow the lesson’s exact checkpoint.

## Recognize before executing

On OLL, compare yellow on top and the side fringe. Two cases can have the same corner count and need different responses. On PLL, a yellow top means orientation is complete; side-color relationships still select permutation. Headlight and bar counts alone can fail to distinguish opposite edge cycles. Align a known case with U rather than changing the whole cube’s front without noticing.

Cover the route, name the remaining job, and point to the distinguishing stickers. Reveal the complete move line only after choosing the grip. Revisit two similar patterns together in another session; executing the wrong response quickly is not a successful recognition answer.

## Match a difficulty to a useful drill

| What happened | Practise | Check |
| --- | --- | --- |
| Searching took most of the solve | Find a corner, name its side colors, find only its matching edge | Identify both pieces before turning |
| The setup was wrong | Compare a joined pair with the join-then-insert example | Explain the first opening and what it temporarily disturbs |
| The moves were forgotten | Recall one familiar full line before checking it | Verify recall before executing from the exact setup |
| The wrong last-layer response was chosen | Compare the distinguishing fringe or side colors | Choose the full pattern and grip before the route |
| A known route became slow during a method change | Keep a familiar finish and learn one new phase | Finish accurately on a fresh scramble before timing |

Use fresh scrambles to assess transfer; use repeated examples to diagnose one decision. Record the difficulty, drill, result and next decision. These are practice targets, not measured mastery thresholds or speed guarantees.

The routes are model-checked working choices. Several last-layer routes are informed by [CubeSkills’ original OLL/PLL sheets](https://www.cubeskills.com/uploads/pdf/tutorials/oll-algorithms.pdf); route-specific provenance remains in each JSON record, including the [PLL sheet](https://www.cubeskills.com/uploads/pdf/tutorials/pll-algorithms.pdf). Human ergonomics remain pending. The complete beginner 3×3 course and quick guides are in the book; this repository is optional enrichment.
