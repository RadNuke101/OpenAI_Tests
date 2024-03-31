# Start time: 2024-03-30 19:13:16.199961

# Content: Given that given input as ['Tire Pressure ABC123873 Monitor'] output is ABC123873, given input as [' Oil Life ABC849999999021 gauge'] output is ABC849999999021, given input as [' Air conditioner GHF211 maintenance'] output is GHF211, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Tire Pressure ABC123873 Monitor'
# Output: 'ABC123873'

# Input: 'Oil Life ABC849999999021 gauge'
# Output: 'ABC849999999021'

# Input: 'Air conditioner GHF211 maintenance'
# Output: 'GHF211'

def extract_code(input_str):
    try:
        words = input_str.split()
        for word in words:
            if word.isalnum() and len(word) == 9:
                return word
    except Exception as e:
        print("Error:", e)
    
    return None

# Test cases
print(extract_code('Tire Pressure ABC123873 Monitor'))
print(extract_code('Oil Life ABC849999999021 gauge'))
print(extract_code('Air conditioner GHF211 maintenance'))

# End time: 2024-03-30 19:13:18.334572
# Elapsed time in seconds: 2.1345544820001123