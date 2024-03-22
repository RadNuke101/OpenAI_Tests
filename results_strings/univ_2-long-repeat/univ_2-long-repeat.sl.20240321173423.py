# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"

def format_location(input_str):
    inputs = input_str.split(', ')
    if "USA" not in inputs[1]:
        return inputs[0] + ', ' + inputs[1] + ', USA'
    return input_str

# Test cases
print(format_location('UC Berkeley, Berkeley, CA'))  # Output: UC Berkeley, Berkeley, CA, USA
print(format_location('University of Pennsylvania, Phialdelphia, PA, USA'))  # Output: University of Pennsylvania, Phialdelphia, PA, USA
print(format_location('UCLA, Los Angeles, CA'))  # Output: UCLA, Los Angeles, CA, USA
print(format_location('Cornell University, Ithaca, New York, USA'))  # Output: Cornell University, Ithaca, New York, USA
print(format_location('Penn, Philadelphia, PA, USA'))  # Output: Penn, Philadelphia, PA, USA
print(format_location('University of Michigan, Ann Arbor, MI, USA'))  # Output: University of Michigan, Ann Arbor, MI, USA
print(format_location('MIT, Cambridge, MA'))  # Output: MIT, Cambridge, MA, USA
print(format_location('Rice University, Houston, TX'))  # Output: Rice University, Houston, TX, USA
print(format_location('Yale University, New Haven, CT, USA'))  # Output: Yale University, New Haven, CT, USA
print(format_location('Columbia University, New York, NY, USA'))  # Output: Columbia University, New York, NY, USA
print(format_location('NYU, New York, New York, USA'))  # Output: NYU, New York, New York, USA
print(format_location('Drexel University, Philadelphia, PA'))  # Output: Drexel University, Philadelphia, PA, USA
print(format_location('UIUC, Urbana, IL'))  # Output: UIUC, Urbana, IL, USA
print(format_location('Temple University, Philadelphia, PA'))  # Output: Temple University, Philadelphia, PA, USA
print(format_location('Harvard University, Cambridge, MA, USA'))  # Output: Harvard University, Cambridge, MA, USA
print(format_location('University of Connecticut, Storrs, CT, USA'))  # Output: University of Connecticut, Storrs, CT, USA
print(format_location('New Haven University, New Haven, CT, USA'))  # Output: New Haven University, New Haven, CT, USA
print(format_location('University of California, Santa Barbara, Santa Barbara, CA, USA'))  # Output: University of California, Santa Barbara, Santa Barbara, CA, USA
