# Start time: 2024-03-30 18:26:39.944813

# Content: Given that given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is UCLA, Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Penn, Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_university(input_str):
    try:
        input_list = input_str.split(', ')
        university = input_list[0]
        location = input_list[1]
        if len(input_list) == 3:
            country = input_list[2]
            return f"{university}, {location}, {country}"
        else:
            return f"{university}, {location}, USA"
    except IndexError:
        return "Invalid input format"

# Test cases
# print(format_university('University of Pennsylvania, Phialdelphia, PA, USA'))  # University of Pennsylvania, Phialdelphia, PA, USA
# print(format_university('UCLA, Los Angeles, CA'))  # UCLA, Los Angeles, CA, USA
# print(format_university('Cornell University, Ithaca, New York, USA'))  # Cornell University, Ithaca, New York, USA
# print(format_university('Penn, Philadelphia, PA, USA'))  # Penn, Philadelphia, PA, USA
# print(format_university('University of Maryland College Park, College Park, MD'))  # University of Maryland College Park, College Park, MD, USA
# print(format_university('University of Michigan, Ann Arbor, MI, USA'))  # University of Michigan, Ann Arbor, MI, USA

# End time: 2024-03-30 18:26:44.989219
# Elapsed time in seconds: 5.044285389000038