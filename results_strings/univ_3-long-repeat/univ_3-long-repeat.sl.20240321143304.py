# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
# Output: Santa Barbara, CA, USA

def second_input(input):
    second_input = input.split(',')[1].strip()
    if "USA" not in second_input:
        return second_input + ', USA'
    return second_input

# Test the function with the provided input
input = 'University of California, Santa Barbara, Santa Barbara, CA, USA'
output = second_input(input)
print(output)  # Output: Santa Barbara, CA, USA
