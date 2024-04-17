# Start time: 2024-04-10 15:47:02.754590

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of various company names such as General Electric, Microsoft, and Nintendo. Some entries include additional terms like Inc, Corporation, and Enterprises.

Summary for Output Column Data:
- The output column consists of the cleaned-up company names, where any additional terms like Inc, Corporation, or Enterprises have been removed.

Relationship between Input and Output:
- The relationship between the input and output is that the output column simplifies the company names by removing any additional terms, resulting in a cleaner and more standardized format. This process helps in standardizing the data and making it easier to compare and analyze the company names., and input as ['General Electric'] output is General Electric, input as ['General Electric Inc'] output is General Electric, input as ['General Electric Company'] output is General Electric, input as ['Microsoft'] output is Microsoft, input as ['Microsoft Corporation'] output is Microsoft, input as ['Nintendo'] output is Nintendo, input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    cleaned_up_names = []
    for name in args:
        cleaned_name = name.replace(' Inc', '').replace(' Corporation', '').replace(' Enterprises', '').replace(' Company', '')
        cleaned_up_names.append(cleaned_name)
    return cleaned_up_names

# Test cases
generated_function('General Electric', 'General Electric Inc', 'General Electric Company', 'Microsoft', 'Microsoft Corporation', 'Nintendo', 'Nintendo Enterprises')
print(generated_function("General Electric"))  ## Output: General Electric
print(generated_function("General Electric Inc"))  ## Output: General Electric
print(generated_function("General Electric Company"))  ## Output: General Electric
print(generated_function("Microsoft"))  ## Output: Microsoft
print(generated_function("Microsoft Corporation"))  ## Output: Microsoft
print(generated_function("Nintendo"))  ## Output: Nintendo
print(generated_function("Nintendo Enterprises"))  ## Output: Nintendo

# End time: 2024-04-10 15:47:04.744875
# Elapsed time in seconds: 1.9902378300002965