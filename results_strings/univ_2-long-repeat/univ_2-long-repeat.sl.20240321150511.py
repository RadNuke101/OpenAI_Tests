def add_country(input_str):
    inputs = input_str.split(', ')
    if "USA" not in inputs[1]:
        return inputs[0] + ', ' + inputs[1] + ', USA'
    return input_str

# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Given input as ['UC Berkeley', 'Berkeley, CA'] output is UC Berkeley, Berkeley, CA, USA
# Given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA
# Given input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA

# Test cases
print(add_country('UC Berkeley, Berkeley, CA'))  # UC Berkeley, Berkeley, CA, USA
print(add_country('University of Pennsylvania, Phialdelphia, PA, USA'))  # University of Pennsylvania, Phialdelphia, PA, USA
print(add_country('UCLA, Los Angeles, CA'))  # UCLA, Los Angeles, CA, USA
