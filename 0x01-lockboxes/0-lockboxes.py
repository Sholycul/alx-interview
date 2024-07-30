#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    opened = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if key < n:
                    stack.append(key)

    return len(opened) == n
