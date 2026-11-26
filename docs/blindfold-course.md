# Solve from a remembered plan

> John Briggs · How to Master the Cube companion · Updated November 25, 2026. Optional learning beyond the book’s self-contained 3×3 courses. Model checks do not establish physical comfort or learner comprehension.

Read [notation and grip](notation.md). This is a complete teaching buffer system with its own letter maps, setup tables, parity bridge and worked examples below. Start with eyes-open execution; code is optional.

Blindfolded solving is real. You study the scrambled cube, remember what must happen, then carry out that plan without looking. In official World Cube Association (WCA) blindfolded events, memorization is part of the timed attempt. The rules separate memorization and blindfolded execution; they do not allow a written solution to be consulted. [S10]

Begin with your eyes open. Your first success is planning one exchange on paper, performing it and checking that the intended piece arrived. Covering the cube comes after you can plan and carry out the moves reliably.

You do not start by remembering a photograph of 54 colored squares. You learn to name where each piece belongs and send it there with a controlled exchange. This beginner course uses the buffer-swap idea associated with Stefan Pochmann. It provides its own exact sticker map, setup routes and verified worked examples. Other tutorials can use different buffers or exchanges, so do not mix their tables into this system. [S11]

## A place to hold the next passenger

A buffer is a fixed working address. Our edge buffer is UR: the edge between the up and right faces. We read its U-facing sticker. Our corner buffer is ULB: the corner touching up, left and back. We read its U-facing sticker too.

Imagine holding a passenger at a small delivery desk. Find that passenger’s home, exchange it with the occupant there, and bring the next passenger back to the desk. One useful exchange puts the chosen passenger home. The passenger brought back tells you the next destination.

There is a catch. Legal cube turns cannot exchange only two edges while leaving everything else fixed. Our edge exchange also swaps the two right-hand upper corners. Every second edge exchange cancels that corner side effect. The corner exchange similarly swaps the UL and UB edges. We will count these effects and handle the odd case explicitly.

## Give stickers short names

Hold yellow up and green front. The letter map below assigns A to X separately to edges and to corners. An edge letter and a corner letter are different targets even when they use the same character. Keep the two lists separate.

Read each face straight on. On an edge, its four letters run top, right, bottom, left around that face. On a corner, they run top-left, top-right, bottom-right, bottom-left. The face order in the map is U, L, F, R, B, D. Do not imagine the back face as seen through the front: look at its outside.

An address such as FU means the front-facing sticker square of the UF edge. UF means the up-facing square of that same edge. They name different sticker targets on one piece. A corner address starts with the face carrying the named sticker; the other two letters identify its corner. RDF is the right-facing sticker of the bottom-front-right corner.

On this map, edge B is the U-facing buffer sticker and edge M is its partner on R. Corner A is the U-facing buffer sticker; E and R are the other stickers of that corner. None of those buffer letters appears as a target in its own family’s setup table.

## The complete sticker maps

Read each face from outside; the address, not its position in a browser table, identifies the exact sticker. Letters repeat between families.

### Edge letters

| Letter | Sticker address |
| --- | --- |
| A | UB |
| B | UR |
| C | UF |
| D | UL |
| E | LU |
| F | LF |
| G | LD |
| H | LB |
| I | FU |
| J | FR |
| K | FD |
| L | FL |
| M | RU |
| N | RB |
| O | RD |
| P | RF |
| Q | BU |
| R | BL |
| S | BD |
| T | BR |
| U | DF |
| V | DR |
| W | DB |
| X | DL |

### Corner letters

| Letter | Sticker address |
| --- | --- |
| A | ULB |
| B | URB |
| C | URF |
| D | ULF |
| E | LUB |
| F | LUF |
| G | LDF |
| H | LDB |
| I | FUL |
| J | FUR |
| K | FDR |
| L | FDL |
| M | RUF |
| N | RUB |
| O | RDB |
| P | RDF |
| Q | BUR |
| R | BUL |
| S | BDL |
| T | BDR |
| U | DLF |
| V | DRF |
| W | DRB |
| X | DLB |

## Learn the two exchange engines

The edge engine is the T sequence printed below. Here its exact job matters: it exchanges UR and UL, with the U-facing sticker at UR going to the U-facing square at UL. It also exchanges the upper front-right and upper back-right corners. All other pieces and all centers return.

R U R′ U′ R′ F R2 U′ R′ U′ R U R′ F′

The corner engine exchanges the U-facing sticker at ULB with the right-facing sticker at DFR. It also exchanges the UL and UB edges. This is a modified Y-style exchange, not the complete ordinary Y PLL. Do not replace it with a similar-looking algorithm from memory.

R U′ R′ U′ R U R′ F′ R U R′ U′ R′ F R

Start solved and execute one engine while looking. Inspect both intended pieces and the side effect. Execute that same engine again: the whole cube returns to solved. Practise until you can finish each full sequence without needing to inspect the cube halfway through.

## Bring another target to the exchange

We want the edge desk at UR to reach more than UL. A setup brings a chosen target sticker to UL without disturbing the buffer or the two corners that the edge engine uses. Execute the engine, then undo the setup. The whole package exchanges the buffer and the original target with the required facing.

For edge J, the FR target, the setup table gives d2 L. Do d2 L, then T, then L′ d2. The inverse is read backward; it is not d2 L′. The complete group restores the centers and has exactly the same two-corner side effect as T.

The lowercase d turns the bottom two layers together. Lowercase l in other rows turns the left two layers together. Both can move centers temporarily. Keep the same physical front position through setup, engine and undo. Do not turn the whole cube to chase a moving green center.

For corners, the table uses F, R and D setups. Those faces avoid the ULB buffer and the UL and UB side-effect edges. Corner C uses F: do F, the corner engine, then F′. Its target is the U-facing sticker at the upper front-right corner. Watch that particular sticker, not merely the corner’s address.

Every setup row has an explicit undo. Use the whole row once. Repeating a row twice cancels its complete effect. The table’s other sticker exchanges make the facing check visible and will also let you build a plan on paper.

## Complete setup, engine and undo tables

The table’s exchanges update only the selected family on a planning worksheet. The opposite-family side effect is described above and must be handled by the parity procedure. Do not omit it from physical execution. “None” means no setup turn.

### Edge targets

| Letter | Sticker target | Setup | Engine | Undo | Worksheet swaps |
| --- | --- | --- | --- | --- | --- |
| A | UB | l2 d' L2 | T | L2 d l2 | A ↔ B; Q ↔ M |
| C | UF | l2 d L2 | T | L2 d' l2 | B ↔ C; I ↔ M |
| D | UL | None | T | None | D ↔ B; M ↔ E |
| E | LU | L' d L' | T | L d' L | D ↔ M; B ↔ E |
| F | LF | d' L | T | L' d | B ↔ F; L ↔ M |
| G | LD | L d L' | T | L d' L' | B ↔ G; X ↔ M |
| H | LB | d L' | T | L d' | B ↔ H; R ↔ M |
| I | FU | l d' L2 | T | L2 d l' | B ↔ I; C ↔ M |
| J | FR | d2 L | T | L' d2 | B ↔ J; M ↔ P |
| K | FD | l d L2 | T | L2 d' l' | B ↔ K; U ↔ M |
| L | FL | L' | T | L | B ↔ L; M ↔ F |
| N | RB | d L | T | L' d' | B ↔ N; T ↔ M |
| O | RD | d2 L d L' | T | L d' L' d2 | B ↔ O; V ↔ M |
| P | RF | d' L' | T | L d | B ↔ P; J ↔ M |
| Q | BU | l' d L2 | T | L2 d' l | A ↔ M; B ↔ Q |
| R | BL | L | T | L' | B ↔ R; M ↔ H |
| S | BD | l' d' L2 | T | L2 d l | B ↔ S; W ↔ M |
| T | BR | d2 L' | T | L d2 | B ↔ T; M ↔ N |
| U | DF | d' L2 | T | L2 d | B ↔ U; K ↔ M |
| V | DR | d2 L2 | T | L2 d2 | B ↔ V; M ↔ O |
| W | DB | d L2 | T | L2 d' | B ↔ W; S ↔ M |
| X | DL | L2 | T | L2 | B ↔ X; M ↔ G |

### Corner targets

| Letter | Sticker target | Setup | Engine | Undo | Worksheet swaps |
| --- | --- | --- | --- | --- | --- |
| B | URB | R D' | Corner engine | D R' | A ↔ B; Q ↔ E; R ↔ N |
| C | URF | F | Corner engine | F' | A ↔ C; J ↔ R; M ↔ E |
| D | ULF | F R' | Corner engine | R F' | A ↔ D; I ↔ E; R ↔ F |
| F | LUF | F2 | Corner engine | F2 | A ↔ F; D ↔ E; I ↔ R |
| G | LDF | F2 R' | Corner engine | R F2 | A ↔ G; U ↔ R; L ↔ E |
| H | LDB | D2 | Corner engine | D2 | A ↔ H; X ↔ E; R ↔ S |
| I | FUL | F' D | Corner engine | D' F | A ↔ I; D ↔ R; E ↔ F |
| J | FUR | R2 D' | Corner engine | D R2 | A ↔ J; C ↔ E; R ↔ M |
| K | FDR | R F | Corner engine | F' R' | A ↔ K; V ↔ R; P ↔ E |
| L | FDL | D | Corner engine | D' | A ↔ L; U ↔ E; R ↔ G |
| M | RUF | R' | Corner engine | R | A ↔ M; C ↔ R; J ↔ E |
| N | RUB | R2 | Corner engine | R2 | A ↔ N; B ↔ E; Q ↔ R |
| O | RDB | R | Corner engine | R' | A ↔ O; W ↔ R; T ↔ E |
| P | RDF | None | Corner engine | None | A ↔ P; V ↔ E; K ↔ R |
| Q | BUR | R' F | Corner engine | F' R | A ↔ Q; B ↔ R; N ↔ E |
| S | BDL | D' R | Corner engine | R' D | A ↔ S; X ↔ R; E ↔ H |
| T | BDR | D' | Corner engine | D | A ↔ T; W ↔ E; R ↔ O |
| U | DLF | F' | Corner engine | F | A ↔ U; L ↔ R; E ↔ G |
| V | DRF | D' F' | Corner engine | F D | A ↔ V; K ↔ E; R ↔ P |
| W | DRB | D2 F' | Corner engine | F D2 | A ↔ W; R ↔ T; O ↔ E |
| X | DLB | D F' | Corner engine | F D' | A ↔ X; R ↔ H; S ↔ E |

## Plan with a working map first

For the first practice sessions, make a paper copy of the 24-letter edge map and a separate corner map. At each address, write the letter belonging to the sticker currently there. You identify that letter from the piece’s colors and the matching centers in the solved frame.

For example, a yellow-green edge’s yellow sticker belongs at UF, edge C. Its green sticker belongs at FU, edge I. If that edge is flipped at its own home, write I at address C and C at address I. Calling the whole edge “C” would miss the flip.

Do the same for corners using all three colors. Yellow green orange identifies the upper front-right home. Its yellow sticker belongs at corner C, its orange sticker at M, and its green sticker at J in this map. Read the printed map rather than guessing from a letter you remember from another scheme.

This paper exercise teaches planning. The real cube stays scrambled and unchanged while you update the paper map. Once you can make the same decisions mentally, remove the paper aid. Written aids during an official attempt are not part of the WCA procedure.

## Build the edge list

Read the letter at edge address B on your working map. That is the home of the buffer’s U-facing sticker. If it is a nonbuffer letter, append it to your edge list. Then update the working map by exchanging the entries at the pairs printed for that target. These pairs describe the virtual edge exchange only; ignore its corner side effect while making the edge list.

Read B again. The passenger brought back now names the next target. Keep choosing the home of the sticker currently at B and updating the two printed pairs. You are rehearsing the plan without moving the real cube.

Stop when every edge address contains its own letter. Check all 24 entries; a flipped edge still has two wrong entries even though the piece is at its home. Record the targets in the order you chose them. That order is your execution list.

## Open a new cycle when the desk has its own piece

Sometimes B contains B or M, a sticker of the buffer piece, while other edges remain unsolved. Your current chain has returned to the desk. Choose any wrong nonbuffer edge address, record that target, and update its exchange pairs. This deliberate choice is a cycle break.

Continue by reading B normally. The piece temporarily sent out from the buffer will come back later. A repeated destination is expected; do not delete it as a duplicate. Deleting a repeated letter can leave the broken cycle unfinished or leave a piece flipped.

A solved buffer does not prove the edges are solved. Inspect the entire working map after each chain. Equally, do not try to target M to “flip the buffer.” Choose a wrong nonbuffer address and let the complete exchanges take care of facing.

## Build the corner list from the original position

Use the original scrambled corner map, not the imagined corner side effects of your edge list. Read corner A. For a nonbuffer letter, record its home and update the three exchange pairs in that corner’s row. Continue until every corner entry matches its address.

If A contains A, E or R and other corners are wrong, choose a wrong nonbuffer corner address to break a cycle. Keep every target you record, including repeats. The three printed exchanges account for orientation as well as location. A twisted corner has three wrong entries and is not finished merely because it occupies its own home.

When a piece is already home and facing correctly, its entries agree with the map and it needs no target. When it is twisted or flipped in place, the disagreement remains visible. This is why we plan from sticker destinations rather than recording only piece names.

## Deal with an odd list before executing corners

Count targets, including cycle-break entries and repeated entries. Count individual letters, not remembered pairs. For a legal cube, the edge and corner counts in this system have the same even-or-odd status.

With an even edge count, the extra corner swap has already canceled. Execute the remembered edge list, then the remembered corner list. An even corner count cancels its extra edge swap too.

With an odd count, execute the edge list, then the parity bridge below, then the original corner list. The bridge cancels the edge engine’s remaining corner exchange and deliberately leaves the UL/UB edge exchange that the odd corner list will cancel. Do not add the bridge at the end instead.

T followed by U2 Ua U2

Written without abbreviations:

R U R′ U′ R′ F R2 U′ R′ U′ R U R′ F′ U2 R U′ R U R U R U′ R′ U′ R2 U2

This is a longer but explicit bridge built from actions already taught. Another parity algorithm is safe only if its entire sticker effect matches this bridge in this exact grip. A sequence called “R perm” elsewhere may use a different orientation and exchange different pieces.

If one target count is odd and the other even, stop and recheck the maps and lists. Do not add a random parity algorithm to compensate for a planning error.

## Turn destinations into memories

First learn to execute from a written target list with your eyes open. Next cover the cube while using that list. These isolate execution from memory. Then memorize the list, put the notes away, and execute without looking or consulting them.

Pair letters into images or short words you personally remember. An edge list C F U P C could become “CF, UP, C” in your own image system. The images are reminders for five targets; they are not additional moves. Keep an unpaired final letter when the list is odd.

Use a different imagined location for the corner list. Remember the parity decision as a separate clear cue between edges and corners. Recall both lists once before starting. At the cube, each target means setup, engine, undo; finish that package before moving to the next image.

Do not create a large letter-pair dictionary before learning whether you can execute two remembered targets reliably. Build memorable pairs gradually, use the same map consistently, and mix recognition practice with execution practice.

## Work through complete examples

The worked examples after the setup tables begin from solved in the stated grip. Apply the scramble, leave the real cube alone, and make the two working maps. The printed lists show one valid planning route. A different legal cycle-break choice can produce another valid list.

Try the single F scramble first. Its buffer pieces begin at home, so both families need an immediate cycle break. This deliberately teaches why a solved buffer can still leave plenty to do. The lists are odd, so execute the parity bridge between edges and corners.

Next use the longer even example. Check its cycle breaks rather than trying to remember the whole scramble. Finally attempt the independent scramble before reading its answers. The goal is to choose targets from a new state, not reproduce a familiar list blindly.

## Worked target lists and parity decisions

These answers are generated from the unchanged scrambled state. A target number in the cycle-break column counts from 1. Python’s raw record stores those positions from 0.

### Odd target count

Start solved, yellow up and green front. Scramble: `F`.

| Family | Targets in order | Cycle-break target numbers |
| --- | --- | --- |
| Edge | C F U P C | 1 |
| Corner | D G V M D | 1 |

Parity bridge: **yes, between edges and corners**. Execute all edges, the bridge if required, then the original corner list. The complete replay returns all 54 stickers to their starting reference frame.

### Even target count

Start solved, yellow up and green front. Scramble: `R U F2 L' D`.

| Family | Targets in order | Cycle-break target numbers |
| --- | --- | --- |
| Edge | A D V J L X W T C U R C | 9 |
| Corner | W K H B D M G D | 5 |

Parity bridge: **no**. Execute all edges, the bridge if required, then the original corner list. The complete replay returns all 54 stickers to their starting reference frame.

### Independent transfer

Start solved, yellow up and green front. Scramble: `R2 F U' L2 D B' R U2 F2 L'`.

| Family | Targets in order | Cycle-break target numbers |
| --- | --- | --- |
| Edge | X A D N L W P H C A V O | 2, 11 |
| Corner | I J B X V U W Q | 3 |

Parity bridge: **no**. Execute all edges, the bridge if required, then the original corner list. The complete replay returns all 54 stickers to their starting reference frame.

## Diagnose a failed blindfold attempt

If two corners remain exchanged after the edges, that can be the expected odd-count side effect. Judge it at the correct stage. After the full solve, an isolated two-edge exchange commonly points to an omitted bridge, a bridge in the wrong grip or a target-count error. Recheck the record instead of assuming that every two-piece-looking error has the same cause.

A target in its home but flipped suggests that the other sticker’s letter was used or an entry was skipped during a cycle break. Many disturbed pieces suggest a missed undo, a changed front, a wide turn mistaken for an outside turn, or an incomplete engine. Repeat the same scramble while looking and compare after each complete target package. The first disagreement is more useful than the final mess.

Do not promise yourself a time for the first blindfold solve. Aim for one accurately remembered exchange, then two, then a whole family, and finally both families with the parity decision. A successful slow attempt proves that the plan and execution can meet.

## Where to go after this system

M2-based edge methods use a middle-slice half turn as an efficient engine but need special treatment of its slice targets and alternating state. Three-style methods usually solve pairs of targets through three-cycles, often built from commutators. They require more recognition and a larger body of practiced actions.

These are worthwhile later choices, not interchangeable shortcuts to paste into the current tables. The [controlled-change lesson](controlled-changes.md) explains the logic behind three-cycles. Keep the first buffer system intact until you can diagnose your own misses.


## Sources and optional executable check

```sh
python3 examples/blindfold_practice.py --scramble "F"
```

[S10]: https://www.worldcubeassociation.org/regulations/#article-B-blindfolded-solving
[S11]: https://www.stefan-pochmann.info/spocc/blindsolving/3x3/

[WCA Article B](https://www.worldcubeassociation.org/regulations/#article-B-blindfolded-solving) governs official attempts; rules checked November 25, 2026. [Stefan Pochmann’s account](https://www.stefan-pochmann.info/spocc/blindsolving/3x3/) supplies method history. This project’s setup routes, worksheet swaps and exact replay tests are independently generated. The model does not establish fast or comfortable human execution.
