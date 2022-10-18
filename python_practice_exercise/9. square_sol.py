"""Task
The provided code stub reads and integer, , from STEIN. For all non-negative integers i < n, print i^2 .
1. The list of non-negative integers that are equal to n.
2. Print the square of each number on a separate line.

Example
Input: n = 3
Output: 1
        4
        9
"""

if __name__ == "__main__":
    n = int(input())
    for i in range(1,n+1):
        print(i*i)



