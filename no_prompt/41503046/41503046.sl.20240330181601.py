# Start time: 2024-03-30 18:18:24.374168

# Content: Given that given input as ['Polygonum amphibium'] output is Polygonum, given input as ['Hippuris vulgaris'] output is Hippuris, given input as ['Lysimachia vulgaris'] output is Lysimachia, given input as ['Juncus bulbosus ssp. bulbosus'] output is Juncus bulbosus, given input as ['Lycopus europaeus ssp. europaeus'] output is Lycopus europaeus, given input as ['Nymphaea alba'] output is Nymphaea, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_genus(input_str):
    try:
        # Input: 'Polygonum amphibium' => Output: 'Polygonum'
        genus = input_str.split()[0]
        return genus
    except (IndexError, AttributeError):
        return "Invalid input format"

# Test cases
print(extract_genus('Polygonum amphibium'))  # Output: Polygonum
print(extract_genus('Hippuris vulgaris'))    # Output: Hippuris
print(extract_genus('Lysimachia vulgaris'))  # Output: Lysimachia
print(extract_genus('Juncus bulbosus ssp. bulbosus'))  # Output: Juncus
print(extract_genus('Lycopus europaeus ssp. europaeus'))  # Output: Lycopus
print(extract_genus('Nymphaea alba'))  # Output: Nymphaea

# End time: 2024-03-30 18:18:29.821581
# Elapsed time in seconds: 5.447288575000016