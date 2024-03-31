# Start time: 2024-03-30 03:05:42.951089
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first input, followed by a comma and space, and then the second input, and given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, given input as ['Yale University', 'New Haven, CT, USA'] output is Yale University, New Haven, CT, USA, given input as ['Columbia University', 'New York, NY, USA'] output is Columbia University, New York, NY, USA, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def combine_inputs(input_list):
    try:
        if len(input_list) != 2:
            raise ValueError("Input list must contain exactly 2 elements")
        
        output = input_list[0] + ', ' + input_list[1]
        return output
    except Exception as e:
        return str(e)

# Test cases
print(combine_inputs(['University of Pennsylvania', 'Phialdelphia, PA, USA']))
print(combine_inputs(['Cornell University', 'Ithaca, New York, USA']))
print(combine_inputs(['University of Maryland College Park', 'College Park, MD']))
print(combine_inputs(['University of Michigan', 'Ann Arbor, MI, USA']))
print(combine_inputs(['Yale University', 'New Haven, CT, USA']))
print(combine_inputs(['Columbia University', 'New York, NY, USA']))

# End time: 2024-03-30 03:05:45.884039
# Elapsed time in seconds: 2.9328693070001464