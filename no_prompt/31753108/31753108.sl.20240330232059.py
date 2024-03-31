# Start time: 2024-03-30 23:29:17.652759

# Content: Given that given input as ['Tire Pressure ABC123873 Monitor'] output is ABC123873, given input as [' Oil Life ABC849999999021 gauge'] output is ABC849999999021, given input as [' Air conditioner GHF211 maintenance'] output is GHF211, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# Input: 'Tire Pressure ABC123873 Monitor'
# Output: 'ABC123873'
# Input: ' Oil Life ABC849999999021 gauge'
# Output: 'ABC849999999021'
# Input: ' Air conditioner GHF211 maintenance'
# Output: 'GHF211'

def extract_code(input_str):
    try:
        # Split the input string by spaces
        words = input_str.split()
        
        # Find the word that contains only uppercase letters and numbers
        for word in words:
            if word.isalnum() and word.isupper():
                return word
    except Exception as e:
        print("Error:", e)
    
    return None

# Test the function with the provided test cases
print(extract_code('Tire Pressure ABC123873 Monitor'))
print(extract_code(' Oil Life ABC849999999021 gauge'))
print(extract_code(' Air conditioner GHF211 maintenance'))

# End time: 2024-03-30 23:29:19.729374
# Elapsed time in seconds: 2.0765497510001296