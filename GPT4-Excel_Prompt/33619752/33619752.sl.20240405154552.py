# Start time: 2024-04-05 16:11:05.333487

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the words "Inc", "Company", "Corporation", or "Enterprises", and input as ['General Electric'] output is General Electric, input as ['General Electric Inc'] output is General Electric, input as ['General Electric Company'] output is General Electric, input as ['Microsoft'] output is Microsoft, input as ['Microsoft Corporation'] output is Microsoft, input as ['Nintendo'] output is Nintendo, input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(company_name):
    # List of words to be removed from the input
    words_to_remove = ["Inc", "Company", "Corporation", "Enterprises"]
    
    # Split the input into a list of words
    name_parts = company_name.split()
    
    # Remove the specified words from the list of words
    cleaned_name_parts = [part for part in name_parts if part not in words_to_remove]
    
    # Join the cleaned list of words back into a string
    cleaned_name = " ".join(cleaned_name_parts)
    
    return cleaned_name

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

# End time: 2024-04-05 16:11:10.523963
# Elapsed time in seconds: 5.190329535000046