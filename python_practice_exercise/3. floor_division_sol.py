"""Task
Usage of floor function:

1. Take two integers.
2. Firstly take normal division, secondly take floor divison.

Example
a = 3
b = 5
The result of the integer division 3/5 = 0.
The result of the float division is 3/5 = 0.6."""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"Floor division :" + str(a // b))  # floor division
    print(f"Division :" + str(a / b))  # division
