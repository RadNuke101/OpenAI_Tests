# Start time: 2024-04-09 19:16:39.309130

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of a list of company names, both in their full legal forms and in more commonly used shorter versions. These names include a mix of technology and industrial companies, illustrating a variety of naming conventions. Some entries include suffixes that denote their incorporation status or company type, such as "Inc", "Corporation", and "Enterprises". The diversity in naming reflects the formal registration names of these entities as well as the colloquial names by which they are more widely recognized. The companies represented span different sectors, indicating a broad scope of industries.

### Output Column Summary:

The output column simplifies the company names provided in the input column by removing any suffixes or descriptors that indicate the company's legal status or structure, such as "Inc", "Corporation", and "Enterprises". The output retains the core name of each company, which is how they are most commonly known to the public. This simplification process results in a more uniform and concise representation of each company's name, focusing on the essential and most recognizable part of their identity.

### Relationship Summary:

The relationship between the input and output columns demonstrates a process of standardization and simplification of company names. The transformation from input to output strips away the formal legal descriptors attached to the company names, leaving behind the most essential and universally recognized part of the name. This process acknowledges the common practice of referring to companies by their core names in everyday language, rather than their full legal titles. It reflects an understanding of how company identities are commonly communicated in the public sphere, focusing on simplicity and recognizability. This relationship highlights the distinction between formal, legal naming conventions and the more streamlined versions of names used in casual or non-legal contexts., and input as ['General Electric'] output is General Electric, input as ['General Electric Inc'] output is General Electric, input as ['General Electric Company'] output is General Electric, input as ['Microsoft'] output is Microsoft, input as ['Microsoft Corporation'] output is Microsoft, input as ['Nintendo'] output is Nintendo, input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(company_name):
    # List of common legal suffixes to remove
    suffixes = [" Inc", " Corporation", " Company", " Enterprises"]
    
    # Remove any of the suffixes if present in the company name
    for suffix in suffixes:
        if company_name.endswith(suffix):
            # Remove the suffix and break, assuming only one suffix is present
            company_name = company_name.replace(suffix, "")
            break
    
    return company_name

# Test cases
print(generated_function('General Electric'))  # Expected: General Electric
print(generated_function('General Electric Inc'))  # Expected: General Electric
print(generated_function('General Electric Company'))  # Expected: General Electric
print(generated_function('Microsoft'))  # Expected: Microsoft
print(generated_function('Microsoft Corporation'))  # Expected: Microsoft
print(generated_function('Nintendo'))  # Expected: Nintendo
print(generated_function('Nintendo Enterprises'))  # Expected: Nintendo
print(generated_function("General Electric"))  ## Output: General Electric
print(generated_function("General Electric Inc"))  ## Output: General Electric
print(generated_function("General Electric Company"))  ## Output: General Electric
print(generated_function("Microsoft"))  ## Output: Microsoft
print(generated_function("Microsoft Corporation"))  ## Output: Microsoft
print(generated_function("Nintendo"))  ## Output: Nintendo
print(generated_function("Nintendo Enterprises"))  ## Output: Nintendo

# End time: 2024-04-09 19:16:46.228827
# Elapsed time in seconds: 6.9195296420002705


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

