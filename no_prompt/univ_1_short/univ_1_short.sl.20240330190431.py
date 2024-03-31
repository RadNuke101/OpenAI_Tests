# Start time: 2024-03-30 19:07:02.193505

# Content: Given that given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is University of Pennsylvania, Phialdelphia, PA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Cornell University, Ithaca, New York, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is University of Maryland College Park, College Park, MD, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is University of Michigan, Ann Arbor, MI, USA, given input as ['Yale University', 'New Haven, CT, USA'] output is Yale University, New Haven, CT, USA, given input as ['Columbia University', 'New York, NY, USA'] output is Columbia University, New York, NY, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases
# Input: 'University of Pennsylvania', 'Phialdelphia, PA, USA'
# Output: 'University of Pennsylvania, Phialdelphia, PA, USA'
# Input: 'Cornell University', 'Ithaca, New York, USA'
# Output: 'Cornell University, Ithaca, New York, USA'
# Input: 'University of Maryland College Park', 'College Park, MD'
# Output: 'University of Maryland College Park, College Park, MD'
# Input: 'University of Michigan', 'Ann Arbor, MI, USA'
# Output: 'University of Michigan, Ann Arbor, MI, USA'
# Input: 'Yale University', 'New Haven, CT, USA'
# Output: 'Yale University, New Haven, CT, USA'
# Input: 'Columbia University', 'New York, NY, USA'
# Output: 'Columbia University, New York, NY, USA'

def format_university(input_str):
    try:
        university, location = input_str.split(', ')
        return university + ', ' + location
    except ValueError:
        return input_str

# Test cases
print(format_university('University of Pennsylvania, Phialdelphia, PA, USA'))
print(format_university('Cornell University, Ithaca, New York, USA'))
print(format_university('University of Maryland College Park, College Park, MD'))
print(format_university('University of Michigan, Ann Arbor, MI, USA'))
print(format_university('Yale University, New Haven, CT, USA'))
print(format_university('Columbia University, New York, NY, USA'))

# End time: 2024-03-30 19:07:07.323290
# Elapsed time in seconds: 5.129621728000075