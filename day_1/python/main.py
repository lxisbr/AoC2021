#!/usr/bin/env python

from pathlib import Path
from typing import List

from aocd import get_data 

def times_values_increase(depths: List[int], scale: int = 1) -> int:
    return sum([ int(depths[i] < depths[i+scale]) for i in range(len(depths)-scale)])

if __name__ == "__main__":
    input = [int(n) for n in get_data(year=2021, day=1).splitlines()]
    print(times_values_increase(input))     # Part 1
    print(times_values_increase(input, 3))  # Part 2
