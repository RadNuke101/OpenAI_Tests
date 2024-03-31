# Start time: 2024-03-30 22:25:46.985253

# Content: Given that given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Penn, Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_location(input_str):
    try:
        input_list = input_str.split(', ')
        if len(input_list) == 2:
            return input_list[0] + ', ' + input_list[1] + ', USA'
        elif len(input_list) == 3:
            return input_list[0] + ', ' + input_list[1] + ', ' + input_list[2]
        else:
            return "Invalid input format"
    except:
        return "Invalid input format"

# Test cases
# input: 'University of Pennsylvania, Phialdelphia, PA, USA'
# expected output: 'University of Pennsylvania, Phialdelphia, PA, USA'
print(format_location('University of Pennsylvania, Phialdelphia, PA, USA'))

# input: 'UCLA, Los Angeles, CA'
# expected output: 'UCLA, Los Angeles, CA, USA'
print(format_location('UCLA, Los Angeles, CA'))

# input: 'Cornell University, Ithaca, New York, USA'
# expected output: 'Cornell University, Ithaca, New York, USA'
print(format_location('Cornell University, Ithaca, New York, USA'))

# input: 'Penn, Philadelphia, PA, USA'
# expected output: 'Penn, Philadelphia, PA, USA'
print(format_location('Penn, Philadelphia, PA, USA'))

# input: 'University of Maryland College Park, College Park, MD'
# expected output: 'University of Maryland College Park, College Park, MD, USA'
print(format_location('University of Maryland College Park, College Park, MD'))

# input: 'University of Michigan, Ann Arbor, MI, USA'
# expected output: 'University of Michigan, Ann Arbor, MI, USA'
print(format_location('University of Michigan, Ann Arbor, MI, USA'))

# End time: 2024-03-30 22:25:50.416262
# Elapsed time in seconds: 3.430911716999617