# Start time: 2024-04-10 13:14:06.461754

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase, and input as ['Polygonum amphibium'] output is Polygonum, input as ['Hippuris vulgaris'] output is Hippuris, input as ['Lysimachia vulgaris'] output is Lysimachia, input as ['Juncus bulbosus ssp. bulbosus'] output is Juncus bulbosus, input as ['Lycopus europaeus ssp. europaeus'] output is Lycopus europaeus, input as ['Nymphaea alba'] output is Nymphaea, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    if 'ssp' in input_str:
        return ' '.join(input_str.split()[:2])
    else:
        return input_str.split()[0]
    
# Test cases
print(generated_function('Polygonum amphibium'))
print(generated_function('Hippuris vulgaris'))
print(generated_function('Lysimachia vulgaris'))
print(generated_function('Juncus bulbosus ssp. bulbosus'))
print(generated_function('Lycopus europaeus ssp. europaeus'))
print(generated_function('Nymphaea alba'))
print(generated_function("Polygonum amphibium"))  ## Output: Polygonum
print(generated_function("Hippuris vulgaris"))  ## Output: Hippuris
print(generated_function("Lysimachia vulgaris"))  ## Output: Lysimachia
print(generated_function("Juncus bulbosus ssp. bulbosus"))  ## Output: Juncus bulbosus
print(generated_function("Lycopus europaeus ssp. europaeus"))  ## Output: Lycopus europaeus
print(generated_function("Nymphaea alba"))  ## Output: Nymphaea

# End time: 2024-04-10 13:14:09.240660
# Elapsed time in seconds: 2.778891655000052