# Start time: 2024-03-30 21:20:17.793700

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
input_str1 = 'Tire Pressure ABC123873 Monitor'
input_str2 = 'Oil Life ABC849999999021 gauge'
input_str3 = 'Air conditioner GHF211 maintenance'

print(extract_code(input_str1))
print(extract_code(input_str2))
print(extract_code(input_str3))

# End time: 2024-03-30 21:20:23.046188
# Elapsed time in seconds: 5.252368207999098