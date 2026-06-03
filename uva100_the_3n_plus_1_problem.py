"""
UVA 100 - The 3n + 1 Problem

Author: Daniel Alejandro Acero Varela
Date: 3 de junio de 2026

Problem:
Given two integers i and j, determine the maximum cycle length
for all numbers between them (inclusive) using the Collatz sequence.

Approach:
- Generate the Collatz sequence for each number in the interval.
- Use memoization to store previously computed cycle lengths.
- When a known value is reached, reuse its stored result instead
  of recomputing the remaining sequence.
- Propagate the computed cycle lengths back through the current path.
- Keep track of the maximum cycle length in the interval.

Why Memoization?
Many Collatz sequences share common subsequences. Instead of
recomputing those subsequences multiple times, their cycle lengths
are cached and reused, significantly reducing execution time.

Time Complexity:
Approximately O(N * average_cycle_length), with substantial
improvements due to memoization.

Space Complexity:
O(M), where M is the number of cached values stored in memory.
"""

def GOTO(n):
    # Apply the Collatz transformation
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


# Cache previously computed cycle lengths
memo = {}

while True:
    try:
        # Read input pair
        i, j = map(int, input().split())

        # Handle intervals where i > j
        start = min(i, j)
        end = max(i, j)

        # Maximum cycle length found in the interval
        maximum = 0

        # Evaluate every number in the interval
        for ele in range(start, end + 1):

            num = ele

            # Store the current path until reaching
            # a known cycle length
            path = []

            while num != 1 and num not in memo:
                path.append(num)
                num = GOTO(num)

            # Base case or cached result
            if num == 1:
                length = 1
            else:
                length = memo[num]

            # Back-propagate cycle lengths
            while path:
                value = path.pop()
                length += 1
                memo[value] = length

            # Update interval maximum
            maximum = max(maximum, memo.get(ele, 1))

        # Print original values and maximum cycle length
        print(i, j, maximum)

    except EOFError:
        break
