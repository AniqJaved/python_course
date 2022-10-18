"""
Given a string input Count all lower case, upper case, digits, and special symbols.

Input:
Original Substrings: ABC123@gmail.com

Output:

Upper case characters:  3
Lower case characters:  8
Number case:  3
Special case characters:  2
"""


def count_chars(str):
    upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
    for i in range(len(str)):
        if 'A' <= str[i] <= 'Z':
            upper_ctr += 1
        elif 'a' <= str[i] <= 'z':
            lower_ctr += 1
        elif '0' <= str[i] <= '9':
            number_ctr += 1
        else:
            special_ctr += 1
    return upper_ctr, lower_ctr, number_ctr, special_ctr


str = "ABC123@gmail.com"
print("Original Substrings:", str)
u, l, n, s = count_chars(str)
print('\nUpper case characters: ', u)
print('Lower case characters: ', l)
print('Number case: ', n)
print('Special case characters: ', s)