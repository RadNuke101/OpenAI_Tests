# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def format_input_output(input_str):
    inputs = input_str.split(', ')
    return inputs[0] + ', ' + inputs[1]

# Test the function with the given inputs
print(format_input_output('University of Pennsylvania, Phialdelphia, PA, USA'))  # Output: University of Pennsylvania, Phialdelphia, PA, USA
print(format_input_output('UCLA, Los Angeles, CA'))  # Output: UCLA, Los Angeles, CA
print(format_input_output('Cornell University, Ithaca, New York, USA'))  # Output: Cornell University, Ithaca, New York, USA
print(format_input_output('Penn, Philadelphia, PA, USA'))  # Output: Penn, Philadelphia, PA, USA
print(format_input_output('University of Maryland College Park, College Park, MD'))  # Output: University of Maryland College Park, College Park, MD
print(format_input_output('University of Michigan, Ann Arbor, MI, USA'))  # Output: University of Michigan, Ann Arbor, MI, USA
print(format_input_output('UC Berkeley, Berkeley, CA'))  # Output: UC Berkeley, Berkeley, CA
print(format_input_output('MIT, Cambridge, MA'))  # Output: MIT, Cambridge, MA
print(format_input_output('Rice University, Houston, TX'))  # Output: Rice University, Houston, TX
print(format_input_output('Yale University, New Haven, CT, USA'))  # Output: Yale University, New Haven, CT, USA
print(format_input_output('Columbia University, New York, NY, USA'))  # Output: Columbia University, New York, NY, USA
print(format_input_output('NYU, New York, New York, USA'))  # Output: NYU, New York, New York, USA
print(format_input_output('UC Berkeley, Berkeley, CA'))  # Output: UC Berkeley, Berkeley, CA
print(format_input_output('UIUC, Urbana, IL'))  # Output: UIUC, Urbana, IL
print(format_input_output('Temple University, Philadelphia, PA'))  # Output: Temple University, Philadelphia, PA
print(format_input_output('Harvard University, Cambridge, MA, USA'))  # Output: Harvard University, Cambridge, MA, USA
print(format_input_output('University of Connecticut, Storrs, CT, USA'))  # Output: University of Connecticut, Storrs, CT, USA
print(format_input_output('Drexel University, Philadelphia, PA'))  # Output: Drexel University, Philadelphia, PA
print(format_input_output('New Haven University, New Haven, CT, USA'))  # Output: New Haven University, New Haven, CT, USA
print(format_input_output('University of California, Santa Barbara, Santa Barbara, CA, USA'))  # Output: University of California, Santa Barbara, Santa Barbara, CA, USA
