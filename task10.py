'''
You are given a string.
In the first line, print the third character of this string.
In the second line, print the second to last character of this string.
In the third line, print the first five characters of this string.
In the fourth line, print all but the last two characters of this string.
In the fifth line, print all the characters of this string with even indices
( remember indexing starts at 0, so the characters are displayed starting with
the first).
In the sixth line, print all the characters of this string with odd indices ( i.e.
starting with the second character in the string).
In the seventh line, print all the characters of the string in reverse order.
In the eighth line, print every second character of the string in reverse order,
starting from the last one.
In the ninth line, print the length of the given string.

'''

string_1  = "In the first line, print the third character of this string."
print (string_1 [2])

string_2 = "In the second line, print the second to last character of this string."
print (string_2 [1], string_2[-1])

string_3 = "In the third line, print the first five characters of this string."
print(string_3[0:5])

string_4 = "In the fourth line, print all but the last two characters of this string."
print(string_4[0:61])

string_5 = "In the fifth line, print all the characters of this string with even indices"
print(string_5[0::2])

string_6 = "In the sixth line, print all the characters of this string with odd indices"
print(string_6[1::2])

string_7 = "In the seventh line, print all the characters of the string in reverse order."
print(string_7[::-1])

string_8 = "In the eighth line, print every second character of the string in reverse order, starting from the last one."
print(string_8[:2:-1])

string_9 = "In the ninth line, print the length of the given string."
print(len(string_9))