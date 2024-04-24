# Start time: 2024-04-10 13:46:30.765741

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return phrase containing three capitalized letters in the beginning, and input as ['Tire Pressure ABC123873 Monitor'] output is ABC123873, input as [' Oil Life ABC849999999021 gauge'] output is ABC849999999021, input as [' Air conditioner GHF211 maintenance'] output is GHF211, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function to extract the desired phrase containing three capitalized letters in the beginning
def generated_function(input_str):
    # Split the input string into words
    words = input_str.split()
    
    # Iterate through the words to find the phrase with three capitalized letters in the beginning
    for word in words:
        if word.isupper() and len(word) >= 3:
            return word
    
# Test cases
print(generated_function('Tire Pressure ABC123873 Monitor'))
print(generated_function('Oil Life ABC849999999021 gauge'))
print(generated_function('Air conditioner GHF211 maintenance'))
print(generated_function("Tire Pressure ABC123873 Monitor"))  ## Output: ABC123873
print(generated_function(" Oil Life ABC849999999021 gauge"))  ## Output: ABC849999999021
print(generated_function(" Air conditioner GHF211 maintenance"))  ## Output: GHF211

# End time: 2024-04-10 13:46:32.704692
# Elapsed time in seconds: 1.9389060399998925


# APPEND TEST SCRIPTS...
print(generated_function("Tire Pressure ABC123873 Monitor"))  ## Output: ABC123873
print(generated_function(" Oil Life ABC849999999021 gauge"))  ## Output: ABC849999999021
print(generated_function(" Air conditioner GHF211 maintenance"))  ## Output: GHF211


print(generated_function(" Life ABC8499999021 gauge"))  ### Output: ABC8499999021
print(generated_function("Tire ABC123873 Monitor"))  ### Output: ABC123873
print(generated_function(" Air conditioner GDF211 maintenance company"))  ### Output: GDF211

# TEST SCRIPTS APPENDED!
