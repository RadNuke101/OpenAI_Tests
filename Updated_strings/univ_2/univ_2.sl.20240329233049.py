# Start time: 2024-03-29 23:42:36.286714
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

def format_input_output(input_str):
    try:
        input_list = input_str.strip('[]').split(', ')
        first_input = input_list[0].strip("'")
        second_input = input_list[1].strip("'")
        
        if "USA" not in second_input:
            return f"{first_input}, {second_input}, USA"
        else:
            return f"{first_input}, {second_input}"
    except:
        return "Invalid input format"

# Test cases
print(format_input_output("['University of Pennsylvania', 'Phialdelphia, PA, USA']"))  # University of Pennsylvania, Phialdelphia, PA, USA
print(format_input_output("['UCLA', 'Los Angeles, CA']"))  # UCLA, Los Angeles, CA, USA
print(format_input_output("['Cornell University', 'Ithaca, New York, USA']"))  # Cornell University, Ithaca, New York, USA
print(format_input_output("['Penn', 'Philadelphia, PA, USA']"))  # Penn, Philadelphia, PA, USA
print(format_input_output("['University of Maryland College Park', 'College Park, MD']"))  # University of Maryland College Park, College Park, MD, USA
print(format_input_output("['University of Michigan', 'Ann Arbor, MI, USA']"))  # University of Michigan, Ann Arbor, MI, USA
print(format_input_output("['Invalid input format']"))  # Invalid input format

# End time: 2024-03-29 23:42:46.264623
# Elapsed time in seconds: 9.977606560000027