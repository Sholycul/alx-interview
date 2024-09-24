# 0x09 - Island Perimeter

## Project Overview

The "Island Perimeter" project aims to develop an algorithm that calculates the perimeter of an island represented on a grid. In the grid, land is represented by `1`s and water by `0`s. The goal is to determine the total perimeter of the island formed by the land cells.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm](#algorithm)
- [Example](#example)

## Requirements

- Python 3
- Basic knowledge of 2D arrays and algorithms

## Installation

To clone the repository, run the following command:

```bash
git clone https://github.com/Sholycul/alx-interview/0x09-island_perimeter.git
cd 0x09-island_perimeter
```

## Usage

To calculate the island perimeter, import the function `island_perimeter` from the module and provide a grid as input:

```python
from island_perimeter import island_perimeter

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

perimeter = island_perimeter(grid)
print("Island Perimeter:", perimeter)
```

## Algorithm

The algorithm works by iterating through each cell in the grid. For every land cell (`1`), it checks its four possible neighbors (up, down, left, right). For each neighboring cell that is either water (`0`) or out of bounds, the perimeter count is incremented.

Here’s a high-level outline:
1. Initialize a `perimeter` variable to 0.
2. Loop through each cell in the grid.
3. For each land cell, check its neighbors.
4. Count the edges that are either water or out of bounds.
5. Return the total perimeter.

## Example

Given the following grid:

```
0 1 0 0
1 1 1 0
0 1 0 0
0 0 0 0
```

The expected output for the perimeter calculation is `16`.
