def reverse_names(input):
    names = input.split()
    return names[1] + " " + names[0]

# Prompt: return second input, followed by a space, and then the first input
# Given input as ['Launa', 'Withers'] output is Withers Launa
# Given input as ['Lakenya', 'Edison'] output is Edison Lakenya
# Given input as ['Brendan', 'Hage'] output is Hage Brendan

# Test the function with a sample input
input = "Brendan Hage"
output = reverse_names(input)
print(output)  # Output should be "Hage Brendan"
