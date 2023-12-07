#!/usr/bin/python3
"""
A function that iterates over boxes to check for keys that
can unlock other boxes.
    Arg:
    boxes -> The number of boxes to be unlocked.
"""


def canUnlockAll(boxes):
    """
    A function that unlocks other bockes
    Returns true if it can open, otherwise false.
    """
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue

        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
