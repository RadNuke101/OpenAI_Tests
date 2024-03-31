# Start time: 2024-03-30 19:23:38.010797

# Content: Given that given input as ['brown', 'traci'] output is tbrown_acme.com, given input as ['thomas', 'linda'] output is lthomas_acme.com, given input as ['ward', 'jack'] output is jward_acme.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'brown', 'traci'
# Output: tbrown_acme.com

def generate_email(first_name, last_name):
    try:
        email = last_name[0] + first_name + '_acme.com'
        return email
    except Exception as e:
        print("Error:", e)

# Test cases
print(generate_email('brown', 'traci'))
print(generate_email('thomas', 'linda'))
print(generate_email('ward', 'jack'))

# End time: 2024-03-30 19:23:39.488734
# Elapsed time in seconds: 1.4778886590002003