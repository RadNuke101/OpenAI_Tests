# Start time: 2024-04-09 15:43:55.685777

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data:

The input column data consists of names of well-known companies, including both their full legal names and their commonly used names. These names vary in formality and length, with some entries including designations such as "Inc", "Corporation", and "Enterprises" that denote the company's legal status or structure. The companies represented span various industries, including technology, electronics, and entertainment. The diversity in naming conventions reflects the different ways companies are referred to in formal, legal, and casual contexts. The input data showcases how a single entity can be known by multiple appellations, highlighting the nuances in corporate branding and identity.

### Summary of Output Column Data:

The output column data simplifies the names of the companies provided in the input column, stripping away any formal designations or suffixes that indicate the company's legal structure, such as "Inc", "Corporation", or "Enterprises". The output focuses on the most recognizable and essential part of each company's name, which is how they are most commonly referred to by the general public. This simplification process results in a more uniform and concise representation of each company, emphasizing the core identity of each entity without the additional legal or structural descriptors.

### Summary of the Relationship Between Input and Output:

The relationship between the input and output data illustrates a process of normalization and simplification of company names. It demonstrates an understanding that, despite the various formal and legal ways a company might be referred to, there exists a more universally recognized and streamlined version of each company's name that is widely used and understood. This process of reducing a company's name to its most essential components allows for easier recognition and recall, facilitating communication and reference in less formal contexts. The transformation from input to output underscores the importance of accessibility and efficiency in language, especially in the context of corporate identity, where clarity and brevity are valuable. This relationship also reflects a common practice in business and media of using shortened or simplified names for ease of discussion and branding purposes., and input as ['General Electric'] output is General Electric, input as ['General Electric Inc'] output is General Electric, input as ['General Electric Company'] output is General Electric, input as ['Microsoft'] output is Microsoft, input as ['Microsoft Corporation'] output is Microsoft, input as ['Nintendo'] output is Nintendo, input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(company_name):
    """
    Simplifies the company name by removing any formal designations or suffixes.
    
    Args:
    - company_name (str): The full name of the company.
    
    Returns:
    - str: The simplified company name.
    """
    # List of common formal designations or suffixes in company names
    suffixes = [" Inc", " Corporation", " Enterprises", " Company"]
    
    # Remove any of the suffixes from the company name, if present
    for suffix in suffixes:
        if company_name.endswith(suffix):
            # Remove the suffix and break the loop
            company_name = company_name.replace(suffix, "")
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

# End time: 2024-04-09 15:44:05.841204
# Elapsed time in seconds: 10.155149993001032