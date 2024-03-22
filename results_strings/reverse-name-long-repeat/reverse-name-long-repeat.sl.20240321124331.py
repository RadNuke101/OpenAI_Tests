def reverse_names(name1, name2):
    return name2 + ' ' + name1

# Prompt: return second input, followed by a space, and then the first input
# Input: ['Launa', 'Withers'] Output: Withers Launa
# Input: ['Lakenya', 'Edison'] Output: Edison Lakenya
# Input: ['Brendan', 'Hage'] Output: Hage Brendan

# Test the function with the provided inputs
print(reverse_names('Launa', 'Withers'))  # Output: Withers Launa
print(reverse_names('Lakenya', 'Edison'))  # Output: Edison Lakenya
print(reverse_names('Brendan', 'Hage'))  # Output: Hage Brendan
