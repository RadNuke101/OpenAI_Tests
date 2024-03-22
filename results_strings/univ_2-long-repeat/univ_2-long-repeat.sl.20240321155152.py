# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"

def format_input_output(input_str1, input_str2):
    if "USA" not in input_str2:
        return f"{input_str1}, {input_str2}, USA"
    else:
        return f"{input_str1}, {input_str2}"

# Test cases
print(format_input_output('UC Berkeley', 'Berkeley, CA'))  # Output: UC Berkeley, Berkeley, CA, USA
print(format_input_output('University of Pennsylvania', 'Phialdelphia, PA, USA'))  # Output: University of Pennsylvania, Phialdelphia, PA, USA
print(format_input_output('UCLA', 'Los Angeles, CA'))  # Output: UCLA, Los Angeles, CA, USA
print(format_input_output('Cornell University', 'Ithaca, New York, USA'))  # Output: Cornell University, Ithaca, New York, USA
print(format_input_output('Penn', 'Philadelphia, PA, USA'))  # Output: Penn, Philadelphia, PA, USA
print(format_input_output('University of Michigan', 'Ann Arbor, MI, USA'))  # Output: University of Michigan, Ann Arbor, MI, USA
