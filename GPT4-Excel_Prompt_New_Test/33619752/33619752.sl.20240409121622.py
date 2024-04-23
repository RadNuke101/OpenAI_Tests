# Start time: 2024-04-09 13:37:01.836353

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of company names in various forms, including their full legal names and more commonly used names. These names sometimes include suffixes that denote their incorporation status, such as "Inc" for incorporated, "Corporation," or specific designations like "Enterprises." The companies represented in the input data span a range of industries, from technology giants like Microsoft to major conglomerates like General Electric, and include iconic entertainment and gaming companies like Nintendo. The variation in the input data highlights the common practice of companies operating under different names or variations of their names for legal, branding, or operational reasons.

### Output Column Summary:

The output data simplifies the company names provided in the input column by removing any suffixes or descriptors that indicate the company's legal status or structure, such as "Inc," "Corporation," or "Enterprises." The output focuses on the most recognizable and commonly used name of each company, stripping away additional legal or formal designations. This simplification process results in a more uniform and concise representation of each company's name, making it easier for general recognition and use in less formal contexts.

### Relationship Summary:

The transformation from the input to the output column data demonstrates a process of normalization and simplification of company names. This process involves identifying and removing specific suffixes or terms that are not essential for the general identification or recognition of a company. The relationship between the input and output data underscores a common need or preference for using simplified names in contexts where legal formalities are not required or when ease of recognition is prioritized. This simplification can be particularly useful in communication, marketing, and branding efforts where clarity and brevity are valued. The method applied here could be part of a larger data cleaning or preparation task, aimed at standardizing company names for analysis, reporting, or database management purposes., and input as ['General Electric'] output is General Electric, input as ['General Electric Inc'] output is General Electric, input as ['General Electric Company'] output is General Electric, input as ['Microsoft'] output is Microsoft, input as ['Microsoft Corporation'] output is Microsoft, input as ['Nintendo'] output is Nintendo, input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(company_name):
    # List of suffixes to remove from the company name
    suffixes = [' Inc', ' Corporation', ' Company', ' Enterprises']
    
    # Remove any of the suffixes if present in the company name
    for suffix in suffixes:
        if company_name.endswith(suffix):
            # Remove the suffix and break the loop as only one suffix will be present
            company_name = company_name.replace(suffix, '')
            break
    
    return company_name

# Test cases
print(generated_function('General Electric'))  # Expected output: General Electric
print(generated_function('General Electric Inc'))  # Expected output: General Electric
print(generated_function('General Electric Company'))  # Expected output: General Electric
print(generated_function('Microsoft'))  # Expected output: Microsoft
print(generated_function('Microsoft Corporation'))  # Expected output: Microsoft
print(generated_function('Nintendo'))  # Expected output: Nintendo
print(generated_function('Nintendo Enterprises'))  # Expected output: Nintendo
print(generated_function("General Electric"))  ## Output: General Electric
print(generated_function("General Electric Inc"))  ## Output: General Electric
print(generated_function("General Electric Company"))  ## Output: General Electric
print(generated_function("Microsoft"))  ## Output: Microsoft
print(generated_function("Microsoft Corporation"))  ## Output: Microsoft
print(generated_function("Nintendo"))  ## Output: Nintendo
print(generated_function("Nintendo Enterprises"))  ## Output: Nintendo

# End time: 2024-04-09 13:37:13.140212
# Elapsed time in seconds: 11.303524885000115


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

