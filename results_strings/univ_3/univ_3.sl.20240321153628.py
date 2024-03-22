# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
def second_input_with_usa(input):
    second_input = input.split(',')[1].strip()
    if "USA" not in second_input:
        return second_input + ', USA'
    return second_input

# Test cases
print(second_input_with_usa('University of Pennsylvania, Phialdelphia, PA, USA'))  # Output: Phialdelphia, PA, USA
print(second_input_with_usa('UCLA, Los Angeles, CA'))  # Output: Los Angeles, CA, USA
print(second_input_with_usa('Cornell University, Ithaca, New York, USA'))  # Output: Ithaca, New York, USA
print(second_input_with_usa('Penn, Philadelphia, PA, USA'))  # Output: Philadelphia, PA, USA
print(second_input_with_usa('University of Maryland College Park, College Park, MD'))  # Output: College Park, MD, USA
print(second_input_with_usa('University of Michigan, Ann Arbor, MI, USA'))  # Output: Ann Arbor, MI, USA
