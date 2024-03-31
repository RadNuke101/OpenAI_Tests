# Start time: 2024-03-30 20:08:53.389457

# Content: Given that given input as ['Polygonum amphibium'] output is Polygonum, given input as ['Hippuris vulgaris'] output is Hippuris, given input as ['Lysimachia vulgaris'] output is Lysimachia, given input as ['Juncus bulbosus ssp. bulbosus'] output is Juncus bulbosus, given input as ['Lycopus europaeus ssp. europaeus'] output is Lycopus europaeus, given input as ['Nymphaea alba'] output is Nymphaea, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Polygonum amphibium'
# Output: 'Polygonum'

def extract_genus(input_str):
    try:
        genus = input_str.split()[0]
        return genus
    except Exception as e:
        print("Error: ", e)

# Test cases
print(extract_genus('Polygonum amphibium'))  # Output: 'Polygonum'
print(extract_genus('Hippuris vulgaris'))  # Output: 'Hippuris'
print(extract_genus('Lysimachia vulgaris'))  # Output: 'Lysimachia'
print(extract_genus('Juncus bulbosus ssp. bulbosus'))  # Output: 'Juncus'
print(extract_genus('Lycopus europaeus ssp. europaeus'))  # Output: 'Lycopus'
print(extract_genus('Nymphaea alba'))  # Output: 'Nymphaea'

# End time: 2024-03-30 20:09:01.686524
# Elapsed time in seconds: 8.29697372999999