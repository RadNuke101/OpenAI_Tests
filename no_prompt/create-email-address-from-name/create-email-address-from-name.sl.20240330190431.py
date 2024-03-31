# Start time: 2024-03-30 19:09:31.100373

# Content: Given that given input as ['brown', 'traci'] output is tbrown_acme.com, given input as ['thomas', 'linda'] output is lthomas_acme.com, given input as ['ward', 'jack'] output is jward_acme.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'brown', 'traci' => output: 'tbrown_acme.com'
# input: 'thomas', 'linda' => output: 'lthomas_acme.com'
# input: 'ward', 'jack' => output: 'jward_acme.com'

def generate_email(first_name, last_name):
    try:
        # Extract the first letter of the last name
        last_initial = last_name[0].lower()
        
        # Construct the email format
        email = last_initial + first_name.lower() + '_acme.com'
        
        return email
    except Exception as e:
        print("Error:", e)

# Test cases
print(generate_email('brown', 'traci'))
print(generate_email('thomas', 'linda'))
print(generate_email('ward', 'jack'))

# End time: 2024-03-30 19:09:32.577486
# Elapsed time in seconds: 1.4770665999999437