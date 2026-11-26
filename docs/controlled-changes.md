# How can a short action change only a few pieces?

John Briggs · Updated November 25, 2026

A setup carries a useful action to another location. A commutator combines two actions so that much of their movement cancels. Learn to predict the complete sticker effect before using either idea inside a solve. Begin solved and use [the notation guide](notation.md).

## Move an action, then put its surroundings back

Write a setup as S and an action as A. A conjugate is `S A S'`, where the last part is the inverse of the complete setup. The prime on a named group means reverse the group's order and each turn's direction.

For an exact example, do `U' R U`. The yellow-green edge starts at UF. U' carries it to UR; R carries it to BR; the last U leaves BR alone. This follows one piece; the complete sequence has other effects too. Undo with `U' R' U` and inspect every face. Moving one selected piece is not evidence that all other work was preserved.

## Combine actions and undo them in order

A commutator has the form `A B A' B'`. If A and B act on entirely disjoint pieces, their effects cancel. From solved, test `R L R' L'`: the whole cube returns.

Overlap can leave a controlled cycle. From solved in the original yellow-up, green-front grip:

| Complete sequence | Piece addresses that move | Check |
| --- | --- | --- |
| `M U2 M' U2` | UF, UB and DB edges | Every other piece and every center returns |
| `R U R' D R U' R' D'` | UFR, DFR and DFL corners | Every other piece and every center returns |

Follow one of the named pieces, then inspect the others. Address sets alone do not fully specify sticker facing. Execute the inverse to undo the experiment. Repeating either entire sequence three times also returns every sticker; this is checked by the model tests. Do not insert either sequence into a partly solved cube merely because its moved-piece count is small.

## Transfer the reasoning

Cover the table. Predict whether a proposed setup preserves the pieces you need. Verify the entire action, including sticker facing and collateral movement. If you cannot explain the effect, return to a solved practice cube rather than experimenting inside an unfinished solve.

The [blindfold course](blindfold-course.md) uses exact buffer exchanges with deliberately managed side effects. M2 and three-style blindfold methods are later systems with their own special cases; the two examples here are not complete courses in those methods. See the [mathematics lesson](mathematics-and-shorter-solutions.md) for inverse, permutation and invariant experiments.

The sequences and stated affected-piece sets are covered by `tests/test_mechanisms.py`. These checks do not establish comfortable grips or human execution speed.
