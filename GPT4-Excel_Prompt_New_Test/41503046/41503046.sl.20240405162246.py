# Start time: 2024-04-05 16:29:04.358843

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, but if "ssp" in expression, return first two words of inputted phrase, and input as ['Polygonum amphibium'] output is Polygonum, input as ['Hippuris vulgaris'] output is Hippuris, input as ['Lysimachia vulgaris'] output is Lysimachia, input as ['Juncus bulbosus ssp. bulbosus'] output is Juncus bulbosus, input as ['Lycopus europaeus ssp. europaeus'] output is Lycopus europaeus, input as ['Nymphaea alba'] output is Nymphaea, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase):
    # Check if "ssp" is in the phrase
    if "ssp" in phrase:
        # Split the phrase into words and return the first two words joined with a space
        words = phrase.split()
        return ' '.join(words[:2])
    else:
        # Split the phrase into words and return the first word
        return phrase.split()[0]

# Test cases
print(generated_function('Polygonum amphibium'))  # Expected output: Polygonum
print(generated_function('Hippuris vulgaris'))  # Expected output: Hippuris
print(generated_function('Lysimachia vulgaris'))  # Expected output: Lysimachia
print(generated_function('Juncus bulbosus ssp. bulbosus'))  # Expected output: Juncus bulbosus
print(generated_function('Lycopus europaeus ssp. europaeus'))  # Expected output: Lycopus europaeus
print(generated_function('Nymphaea alba'))  # Expected output: Nymphaea
print(generated_function("Polygonum amphibium"))  ## Output: Polygonum
print(generated_function("Hippuris vulgaris"))  ## Output: Hippuris
print(generated_function("Lysimachia vulgaris"))  ## Output: Lysimachia
print(generated_function("Juncus bulbosus ssp. bulbosus"))  ## Output: Juncus bulbosus
print(generated_function("Lycopus europaeus ssp. europaeus"))  ## Output: Lycopus europaeus
print(generated_function("Nymphaea alba"))  ## Output: Nymphaea

# End time: 2024-04-05 16:29:11.454605
# Elapsed time in seconds: 7.095660045000386


# APPEND TEST SCRIPTS...
print(generated_function("Polygonum amphibium"))  ## Output: Polygonum
print(generated_function("Hippuris vulgaris"))  ## Output: Hippuris
print(generated_function("Lysimachia vulgaris"))  ## Output: Lysimachia
print(generated_function("Juncus bulbosus ssp. bulbosus"))  ## Output: Juncus bulbosus
print(generated_function("Lycopus europaeus ssp. europaeus"))  ## Output: Lycopus europaeus
print(generated_function("Nymphaea alba"))  ## Output: Nymphaea


print(generated_function("Polygonum pengioius ssp. pengioius"))  ### Output: Polygonum pengioius
print(generated_function("Lycopus europaeus"))  ### Output: Lycopus
print(generated_function("Polygonum pengioius"))  ### Output: Polygonum
print(generated_function("Lysimachia amphibium ssp. amphibium"))  ### Output: Lysimachia amphibium

# TEST SCRIPTS APPENDED!

