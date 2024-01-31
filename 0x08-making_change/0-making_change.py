#!/usr/bin/python3
""" A function used to determine the fewest number of coins
needed to attain a given total amount of cash."""


def makeChange(coins, total):
    """
    Takes and list of coins and total amount as args
    and returns the minium number of coints to makeup the amount.
    """
    if total <= 0:
        return 0
    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while (total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
