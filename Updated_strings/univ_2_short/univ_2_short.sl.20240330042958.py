# Start time: 2024-03-30 04:42:58.172719
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA", and given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Penn, Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA
# Input: ['UCLA', 'Los Angeles, CA']
# Output: UCLA, Los Angeles, CA, USA
# Input: ['Cornell University', 'Ithaca, New York, USA']
# Output: Cornell University, Ithaca, New York, USA
# Input: ['Penn', 'Philadelphia, PA, USA']
# Output: Penn, Philadelphia, PA, USA
# Input: ['University of Maryland College Park', 'College Park, MD']
# Output: University of Maryland College Park, College Park, MD, USA
# Input: ['University of Michigan', 'Ann Arbor, MI, USA']
# Output: University of Michigan, Ann Arbor, MI, USA

def format_location(input_data):
    try:
        if "USA" not in input_data[1]:
            return f"{input_data[0]}, {input_data[1]}, USA"
        else:
            return f"{input_data[0]}, {input_data[1]}"
    except (IndexError, TypeError):
        return "Invalid input format"

# Test cases
print(format_location(['University of Pennsylvania', 'Phialdelphia, PA, USA']))
print(format_location(['UCLA', 'Los Angeles, CA']))
print(format_location(['Cornell University', 'Ithaca, New York, USA']))
print(format_location(['Penn', 'Philadelphia, PA, USA']))
print(format_location(['University of Maryland College Park', 'College Park, MD']))
print(format_location(['University of Michigan', 'Ann Arbor, MI, USA']))
print(format_location(['Invalid input']))  # Testing invalid input

# End time: 2024-03-30 04:43:01.717626
# Elapsed time in seconds: 3.5448990129989397