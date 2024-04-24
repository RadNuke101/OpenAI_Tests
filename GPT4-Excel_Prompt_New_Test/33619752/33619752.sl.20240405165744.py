# Start time: 2024-04-05 17:21:32.080126

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the words "Inc", "Company", "Corporation", or "Enterprises", and input as ['General Electric'] output is General Electric, input as ['General Electric Inc'] output is General Electric, input as ['General Electric Company'] output is General Electric, input as ['Microsoft'] output is Microsoft, input as ['Microsoft Corporation'] output is Microsoft, input as ['Nintendo'] output is Nintendo, input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # List of words to be removed from the input string
    words_to_remove = ["Inc", "Company", "Corporation", "Enterprises"]
    
    # Split the input string into a list of words
    input_words = input_string.split()
    
    # Remove the specified words from the input list
    filtered_words = [word for word in input_words if word not in words_to_remove]
    
    # Join the filtered words back into a string
    output_string = " ".join(filtered_words)
    
    return output_string

# Test cases
print(generated_function('General Electric'))
print(generated_function('General Electric Inc'))
print(generated_function('General Electric Company'))
print(generated_function('Microsoft'))
print(generated_function('Microsoft Corporation'))
print(generated_function('Nintendo'))
print(generated_function('Nintendo Enterprises'))
print(generated_function("General Electric"))  ## Output: General Electric
print(generated_function("General Electric Inc"))  ## Output: General Electric
print(generated_function("General Electric Company"))  ## Output: General Electric
print(generated_function("Microsoft"))  ## Output: Microsoft
print(generated_function("Microsoft Corporation"))  ## Output: Microsoft
print(generated_function("Nintendo"))  ## Output: Nintendo
print(generated_function("Nintendo Enterprises"))  ## Output: Nintendo

# End time: 2024-04-05 17:21:37.331022
# Elapsed time in seconds: 5.25074573800066


# APPEND TEST SCRIPTS...
print(generated_function("General Electric"))  ## Output: General Electric
print(generated_function("General Electric Inc"))  ## Output: General Electric
print(generated_function("General Electric Company"))  ## Output: General Electric
print(generated_function("Microsoft"))  ## Output: Microsoft
print(generated_function("Microsoft Corporation"))  ## Output: Microsoft
print(generated_function("Nintendo"))  ## Output: Nintendo
print(generated_function("Nintendo Enterprises"))  ## Output: Nintendo


print(generated_function("Nintendo Company"))  ### Output: Nintendo
print(generated_function("General Electric Corporation"))  ### Output: General Electric
print(generated_function("Microsoft Corporation"))  ### Output: Microsoft
print(generated_function("Microsoft Inc"))  ### Output: Microsoft
print(generated_function("Microsoft Enterprises"))  ### Output: Microsoft
print(generated_function("Microsoft"))  ### Output: Microsoft
print(generated_function("Walmart Inc"))  ### Output: Walmart
print(generated_function("General Electric Enterprises"))  ### Output: General Electric
print(generated_function("Microsoft Company"))  ### Output: Microsoft
print(generated_function("Walmart"))  ### Output: Walmart
print(generated_function("Walmart Corporation"))  ### Output: Walmart
print(generated_function("Walmart Enterprises"))  ### Output: Walmart
print(generated_function("Nintendo Corporation"))  ### Output: Nintendo
print(generated_function("Walmart Company"))  ### Output: Walmart

# TEST SCRIPTS APPENDED!

