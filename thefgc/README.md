# Fox, Goose, and Corn — River Crossing Puzzle

A practice exercise from the book *Think Like a Programmer*, implemented in Python.

## About

This is **not a portfolio project** — it's a learning exercise focused on practicing
logic, list manipulation, and state tracking in Python.

The classic puzzle: a farmer must move a fox, a goose, and a bag of corn across a
river, one item at a time, without ever leaving the fox alone with the goose, or
the goose alone with the corn (both unsupervised pairings result in one eating
the other).

## Current status

This version uses a **manually scripted sequence of moves** to simulate both a
winning and a losing playthrough — it does not yet automatically solve the puzzle
on its own. State (what's on the starting shore, in the boat, and on the far
shore) is tracked with three lists, and `check_shore()` validates whether the
current state is safe after each move.

**Not yet implemented:** an automated solver that determines the correct move
sequence itself (e.g. via backtracking search). That's a planned next step, once
recursion/backtracking is covered more deeply.

## Functions

- `check_shore()` — returns whether the current state is safe (no illegal pairing left unsupervised)
- `add_to_boat(item)` — moves an item from the starting shore into the boat
- `add_to_end(item)` — moves an item from the boat to the far shore, if safe
- `bring_back(item)` — moves an item from the far shore back into the boat, then back to the start, if safe

## Run it

```bash
python thefgc.py
```

The script currently runs a hardcoded "lose" scenario by default; a commented-out
"win" sequence is included above it in the source.
