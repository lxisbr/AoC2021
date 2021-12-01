from pathlib import Path
from typing import List

_DAY_1_DIR = Path(__file__).resolve().parents[1]
_DATA_LOCATION = _DAY_1_DIR / "data/input"

def times_values_increase(depths: List[int], scale: int = 1) -> int:
    assert(len(depths) > scale, "given step size longer than array")
    times: int = 0
    window: int = sum(depths[:scale])
    for i in range(len(depths) - scale):
        window_new = window - depths[i] + depths[i+scale]
        if window_new > window:
            times += 1
        window = window_new
    return times

if __name__ == "__main__":
    with _DATA_LOCATION.open() as f:
        input = [int(line) for line in f.readlines()]
        print(times_values_increase(input))     # Part 1
        print(times_values_increase(input, 3))  # Part 2
