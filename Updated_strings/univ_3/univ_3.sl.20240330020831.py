# Start time: 2024-03-30 02:19:51.056241
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA", and given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Ithaca, New York, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is Ann Arbor, MI, USA, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: Phialdelphia, PA, USA
# Input: ['UCLA', 'Los Angeles, CA']
# Output: Los Angeles, CA, USA
# Input: ['Cornell University', 'Ithaca, New York, USA']
# Output: Ithaca, New York, USA
# Input: ['Penn', 'Philadelphia, PA, USA']
# Output: Philadelphia, PA, USA
# Input: ['University of Maryland College Park', 'College Park, MD']
# Output: College Park, MD, USA
# Input: ['University of Michigan', 'Ann Arbor, MI, USA']
# Output: Ann Arbor, MI, USA

def return_second_input(input_list):
    try:
        second_input = input_list[1]
        if "USA" not in second_input:
            return second_input + ", USA"
        else:
            return second_input
    except IndexError:
        return "Invalid input format"

# Test cases
print(return_second_input(['University of Pennsylvania', 'Phialdelphia, PA, USA']))
print(return_second_input(['UCLA', 'Los Angeles, CA']))
print(return_second_input(['Cornell University', 'Ithaca, New York, USA']))
print(return_second_input(['Penn', 'Philadelphia, PA, USA']))
print(return_second_input(['University of Maryland College Park', 'College Park, MD']))
print(return_second_input(['University of Michigan', 'Ann Arbor, MI, USA']))

# End time: 2024-03-30 02:19:58.825323
# Elapsed time in seconds: 7.770304886998929