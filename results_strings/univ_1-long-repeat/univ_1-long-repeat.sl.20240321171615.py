def format_input_output(input_str):
    input_list = input_str.split("', '")
    output_str = input_list[0][2:] + ", " + input_list[1][:-2]
    return output_str

# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: "['University of California, Santa Barbara', 'Santa Barbara, CA, USA']"
# Output: "University of California, Santa Barbara, Santa Barbara, CA, USA"

# Test cases
print(format_input_output("['UC Berkeley', 'Berkeley, CA']"))  # Output: UC Berkeley, Berkeley, CA
print(format_input_output("['University of Pennsylvania', 'Phialdelphia, PA, USA']"))  # Output: University of Pennsylvania, Phialdelphia, PA, USA
print(format_input_output("['UCLA', 'Los Angeles, CA']"))  # Output: UCLA, Los Angeles, CA
print(format_input_output("['Cornell University', 'Ithaca, New York, USA']"))  # Output: Cornell University, Ithaca, New York, USA
