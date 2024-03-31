# Start time: 2024-03-30 20:35:24.819932

# Content: Given that given input as ['University of Pennsylvania', 'Phialdelphia, PA, USA'] output is Phialdelphia, PA, USA, given input as ['UCLA', 'Los Angeles, CA'] output is Los Angeles, CA, USA, given input as ['Cornell University', 'Ithaca, New York, USA'] output is Ithaca, New York, USA, given input as ['Penn', 'Philadelphia, PA, USA'] output is Philadelphia, PA, USA, given input as ['University of Maryland College Park', 'College Park, MD'] output is College Park, MD, USA, given input as ['University of Michigan', 'Ann Arbor, MI, USA'] output is Ann Arbor, MI, USA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'University of Pennsylvania', 'Phialdelphia, PA, USA'
# output: 'Phialdelphia, PA, USA'
# input: 'UCLA', 'Los Angeles, CA'
# output: 'Los Angeles, CA, USA'
# input: 'Cornell University', 'Ithaca, New York, USA'
# output: 'Ithaca, New York, USA'
# input: 'Penn', 'Philadelphia, PA, USA'
# output: 'Philadelphia, PA, USA'
# input: 'University of Maryland College Park', 'College Park, MD'
# output: 'College Park, MD, USA'
# input: 'University of Michigan', 'Ann Arbor, MI, USA'
# output: 'Ann Arbor, MI, USA'

def get_location(university, location):
    try:
        parts = location.split(',')
        if len(parts) == 3:
            return location
        elif len(parts) == 2:
            return parts[0].strip() + ', ' + parts[1].strip() + ', USA'
        else:
            raise ValueError("Invalid location format")
    except Exception as e:
        print("Error:", e)

# Test cases
print(get_location('University of Pennsylvania', 'Phialdelphia, PA, USA'))
print(get_location('UCLA', 'Los Angeles, CA'))
print(get_location('Cornell University', 'Ithaca, New York, USA'))
print(get_location('Penn', 'Philadelphia, PA, USA'))
print(get_location('University of Maryland College Park', 'College Park, MD'))
print(get_location('University of Michigan', 'Ann Arbor, MI, USA'))

# End time: 2024-03-30 20:35:27.909431
# Elapsed time in seconds: 3.089868308000405