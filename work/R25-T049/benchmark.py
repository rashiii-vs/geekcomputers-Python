
from pathlib import Path
import statistics
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from totaldigits import totaldigits

SIZES = [10, 100, 1000]
REPETITIONS = 5
CALLS_PER_REPETITION = 1000


def run_benchmark():
    print("totaldigits performance benchmark")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Repetitions: {REPETITIONS}")
    print(f"Calls per repetition: {CALLS_PER_REPETITION}")
    print()

    for digits in SIZES:
        base = 10 ** (digits - 1)
        timings = []

        for repetition in range(REPETITIONS):
            offset = repetition * CALLS_PER_REPETITION

            # Prepare fresh inputs outside the timed section.
            inputs = [
                base + ((offset + i) % (9 * base))
                for i in range(CALLS_PER_REPETITION)
            ]

            # Verify correctness before timing.
            for number in inputs:
                assert totaldigits(number) == digits

            start = time.perf_counter_ns()

            for number in inputs:
                totaldigits(number)

            end = time.perf_counter_ns()

            timings.append(
                (end - start) / CALLS_PER_REPETITION
            )

        print(f"Input size: {digits} decimal digits")
        print(f"Median: {statistics.median(timings):.2f} ns/call")
        print(
            f"Range: {min(timings):.2f} - "
            f"{max(timings):.2f} ns/call"
        )
        print()


if __name__ == "__main__":
    run_benchmark()

