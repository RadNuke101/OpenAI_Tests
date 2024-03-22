def reverse_names(input):
    names = input.split()
    return names[1] + " " + names[0]

# Prompt: return second input, followed by a space, and then the first input
# Given input as ['Launa', 'Withers'] output is Withers Launa
# Given input as ['Lakenya', 'Edison'] output is Edison Lakenya
# Given input as ['Brendan', 'Hage'] output is Hage Brendan

# Test cases
print(reverse_names('Launa Withers'))  # Output: Withers Launa
print(reverse_names('Lakenya Edison'))  # Output: Edison Lakenya
print(reverse_names('Brendan Hage'))  # Output: Hage Brendan
