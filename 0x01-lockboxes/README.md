# 0x01. Lockboxes

## Description
This project involves developing a method to determine if a series of locked boxes can all be opened. Each box may contain keys to other boxes, and the objective is to ensure that all boxes can be unlocked using the keys available.

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder of the project is mandatory
- Your code should be documented
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Concepts Needed
- Lists and List Manipulation
- Graph Theory Basics
- Algorithmic Complexity
- Recursion
- Queue and Stack
- Set Operations

### Resources
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) (Python Official Documentation)
- [Graph Theory](https://www.khanacademy.org/computing/computer-science/algorithms#graph-representation) (Khan Academy)
- [Big O Notation](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/) (GeeksforGeeks)
- [Recursion in Python](https://realpython.com/python-recursion/) (Real Python)
- [Python Queue and Stack](https://www.geeksforgeeks.org/stack-in-python/) (GeeksforGeeks)
- [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets) (Python Official Documentation)

## Tasks

### 0. Lockboxes
- **Prototype**: `def canUnlockAll(boxes)`
- **Input**: `boxes` is a list of lists
- **Output**: Return `True` if all boxes can be opened, else return `False`
- **Rules**:
  - A key with the same number as a box opens that box
  - You can assume all keys will be positive integers
  - There can be keys that do not have boxes
  - The first box `boxes[0]` is unlocked

### Example
```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```

### Submission
- GitHub repository: `alx-interview`
- Directory: `0x01-lockboxes`
- File: `0-lockboxes.py`

## Project Timeline
- **Project Start**: Jul 29, 2024, 6:00 AM
- **Project End**: Aug 2, 2024, 6:00 AM
- **Checker Release**: Jul 30, 2024, 6:00 AM
- **Auto Review**: At the deadline

## Additional Resources
- Mock Technical Interview

## Must Know
For this project, you will need a solid understanding of several key concepts to develop a solution that can efficiently determine if all boxes can be opened.

## Author
Sholycul
