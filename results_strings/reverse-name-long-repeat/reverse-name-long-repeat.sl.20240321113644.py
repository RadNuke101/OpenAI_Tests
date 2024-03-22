def reverse_names(input):
    names = input.split()
    return names[1] + " " + names[0]

# Input: "Launa Withers"
# Output: "Withers Launa"
# Prompt: return second input, followed by a space, and then the first input

# Test cases
print(reverse_names("Launa Withers"))  # Output: "Withers Launa"
print(reverse_names("Lakenya Edison"))  # Output: "Edison Lakenya"
print(reverse_names("Brendan Hage"))  # Output: "Hage Brendan"
