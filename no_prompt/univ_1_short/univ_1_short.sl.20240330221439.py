# Start time: 2024-03-30 22:16:37.533750

# Content: Given that given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, given input as ['Yale University', 'New Haven, CT, USA'] output is Yale University, New Haven, CT, USA, given input as ['Columbia University', 'New York, NY, USA'] output is Columbia University, New York, NY, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_university(input_str):
    try:
        input_list = input_str.split(', ')
        university = input_list[0]
        location = ', '.join(input_list[1:])
        return f"{university}, {location}"
    except IndexError:
        return "Invalid input format"

# Test cases
print(format_university('University of Pennsylvania, Phialdelphia, PA, USA'))  # University of Pennsylvania, Phialdelphia, PA, USA
print(format_university('Cornell University, Ithaca, New York, USA'))  # Cornell University, Ithaca, New York, USA
print(format_university('University of Maryland College Park, College Park, MD'))  # University of Maryland College Park, College Park, MD
print(format_university('University of Michigan, Ann Arbor, MI, USA'))  # University of Michigan, Ann Arbor, MI, USA
print(format_university('Yale University, New Haven, CT, USA'))  # Yale University, New Haven, CT, USA
print(format_university('Columbia University, New York, NY, USA'))  # Columbia University, New York, NY, USA

# End time: 2024-03-30 22:16:39.267498
# Elapsed time in seconds: 1.7336983349996444