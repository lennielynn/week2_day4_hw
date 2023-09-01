# Write a function that returns the number (i.e., count) of vowels in a given string.

# For this exercise, consider the following as vowels: a, e, i, o, u. The letter 'y' is not considered a vowel.

# Constraints:

# The input string will only consist of lowercase letters and/or spaces.

vowels = []
input = ("this is an example sentece")


def vowel_ct():
    for v in input:
        if v in ('aeiou'):
              vowels.append(v)
              print(vowels)
        else:
            continue
vowel_ct()
print(vowels.count())