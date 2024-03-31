# Start time: 2024-03-30 21:22:51.099466

# Content: Given that given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Ithaca, New York, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is Ann Arbor, MI, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_location(input_str):
    try:
        input_list = input_str.split(', ')
        return input_list[-1]
    except:
        return "Invalid input format"

# Test cases
print(get_location('University of Pennsylvania, Phialdelphia, PA, USA'))  # Output: Phialdelphia, PA, USA
print(get_location('UCLA, Los Angeles, CA'))  # Output: Los Angeles, CA, USA
print(get_location('Cornell University, Ithaca, New York, USA'))  # Output: Ithaca, New York, USA
print(get_location('Penn, Philadelphia, PA, USA'))  # Output: Philadelphia, PA, USA
print(get_location('University of Maryland College Park, College Park, MD'))  # Output: College Park, MD, USA
print(get_location('University of Michigan, Ann Arbor, MI, USA'))  # Output: Ann Arbor, MI, USA

# End time: 2024-03-30 21:22:53.044600
# Elapsed time in seconds: 1.9446810190001997