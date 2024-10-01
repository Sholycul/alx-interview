# Prime Game

## Description

The Prime Game is a two-player game between Maria and Ben. Players take turns selecting prime numbers from a set of consecutive integers (1 to \( n \)). Choosing a prime removes that number and its multiples, and the player unable to make a move loses. This repository provides a solution to determine the winner after a specified number of rounds.

## Function Prototype

```python
def isWinner(x, nums):
```

### Parameters

- `x`: Number of rounds (1 ≤ x ≤ 10000).
- `nums`: List of integers representing the maximum number for each round (1 ≤ n ≤ 10000).

### Returns

- Name of the player who won the most rounds or `None` if there's a tie.

## Example

Input:
```python
x = 3
nums = [4, 5, 1]
```

Output:
```
Winner: Ben
```

## Usage

Run the function as follows:
```bash
$ python3 main_0.py
```

## Repository Structure

- **GitHub Repository:** [alx-interview](https://github.com/Sholycul/alx-interview)
- **Directory:** `0x0A-primegame`
- **File:** `0-prime_game.py`
