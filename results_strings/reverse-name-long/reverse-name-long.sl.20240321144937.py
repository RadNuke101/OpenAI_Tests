def reverse_names(input):
    names = input.split()
    return names[1] + " " + names[0]

# Prompt: return second input, followed by a space, and then the first input
# Input: ['Launa', 'Withers'] Output: Withers Launa
# Input: ['Lakenya', 'Edison'] Output: Edison Lakenya
# Input: ['Brendan', 'Hage'] Output: Hage Brendan

# Test the function with the provided inputs
print(reverse_names('Launa Withers'))  # Output: Withers Launa
print(reverse_names('Lakenya Edison'))  # Output: Edison Lakenya
print(reverse_names('Brendan Hage'))  # Output: Hage Brendan
