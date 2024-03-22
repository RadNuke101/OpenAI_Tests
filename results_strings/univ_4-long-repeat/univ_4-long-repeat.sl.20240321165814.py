# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of California, Santa Barbara', 'Santa Barbara, CA, USA']
# Output: Santa Barbara, CA, USA

def return_second_input(input_str):
    inputs = input_str.split(', ')
    if 'USA' not in inputs[1]:
        return inputs[1] + ', USA'
    return inputs[1]

# Test cases
print(return_second_input('University of California, Santa Barbara, CA, USA'))  # Output: Santa Barbara, CA, USA
print(return_second_input('University of Connecticut, Storrs, CT, USA'))  # Output: Storrs, CT, USA
print(return_second_input('UC Berkeley, Berkeley, CA'))  # Output: Berkeley, CA, USA
print(return_second_input('MIT, Cambridge, MA'))  # Output: Cambridge, MA, USA
print(return_second_input('Rice University, Houston, TX'))  # Output: Houston, TX, USA
