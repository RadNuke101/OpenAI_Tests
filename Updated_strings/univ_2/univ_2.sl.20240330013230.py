# Start time: 2024-03-30 01:45:51.776999
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA", and given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Penn, Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the first input, followed by a comma and space, and then the second input. If the second input does not have "USA" in it, again return a comma followed by a space, and then "USA"
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def format_location(input_list):
    try:
        first_input = input_list[0]
        second_input = input_list[1]
        
        if "USA" not in second_input:
            return f"{first_input}, {second_input}, USA"
        else:
            return f"{first_input}, {second_input}"
    except IndexError:
        return "Invalid input format"

# Test cases
print(format_location(['University of Pennsylvania', 'Phialdelphia, PA, USA']))
print(format_location(['UCLA', 'Los Angeles, CA']))
print(format_location(['Cornell University', 'Ithaca, New York, USA']))
print(format_location(['Penn', 'Philadelphia, PA, USA']))
print(format_location(['University of Maryland College Park', 'College Park, MD']))
print(format_location(['University of Michigan', 'Ann Arbor, MI, USA']))

# End time: 2024-03-30 01:46:00.108477
# Elapsed time in seconds: 8.331320326000423