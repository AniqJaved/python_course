"""
Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters.
Input : 'Q-301 is at 4th floor of quaid block.'
Output : Sum = 8
         Average = 2.0 
"""


def findSum(str1):
    temp = "0"
    Sum = 0
    count = 0
    for ch in str1:
        if ch.isdigit():
            Sum += int(ch)
            count += 1
    return Sum + int(temp), Sum / count


s, a = findSum('Q-301 is at 4th floor of quaid block.')

print('Sum = ', s)
print('Average = ', a)
