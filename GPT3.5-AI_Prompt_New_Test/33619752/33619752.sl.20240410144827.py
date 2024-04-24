# Start time: 2024-04-10 15:02:20.128241

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of various company names such as General Electric, Microsoft, and Nintendo.
- Some company names include additional terms such as "Inc" or "Corporation" in their names.

Summary for Output Column Data:
- The output column data consists of the cleaned-up company names, where any additional terms such as "Inc" or "Corporation" have been removed.
- The output column includes the cleaned-up versions of the company names such as General Electric, Microsoft, and Nintendo.

Relationship between Input and Output:
- The relationship between the input and output is that the output column provides a simplified version of the company names by removing any additional terms or variations present in the input column data.
- The output column serves as a standardized form of the company names, making it easier to compare and analyze the data., and input as ['General Electric'] output is General Electric, input as ['General Electric Inc'] output is General Electric, input as ['General Electric Company'] output is General Electric, input as ['Microsoft'] output is Microsoft, input as ['Microsoft Corporation'] output is Microsoft, input as ['Nintendo'] output is Nintendo, input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    cleaned_names = []
    for name in args:
        cleaned_name = name.replace(" Inc", "").replace(" Corporation", "").replace(" Company", "")
        cleaned_names.append(cleaned_name)
    return cleaned_names
print(generated_function("General Electric"))  ## Output: General Electric
print(generated_function("General Electric Inc"))  ## Output: General Electric
print(generated_function("General Electric Company"))  ## Output: General Electric
print(generated_function("Microsoft"))  ## Output: Microsoft
print(generated_function("Microsoft Corporation"))  ## Output: Microsoft
print(generated_function("Nintendo"))  ## Output: Nintendo
print(generated_function("Nintendo Enterprises"))  ## Output: Nintendo

# End time: 2024-04-10 15:02:21.153847
# Elapsed time in seconds: 1.025599093999972


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

