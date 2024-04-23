# Start time: 2024-04-09 17:34:13.494713

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of company names in various forms, including both their full legal names and more commonly used names. These names span across different industries, from technology giants like Microsoft and General Electric to entertainment powerhouses like Nintendo. The variations in the names include additions such as "Inc", "Corporation", and "Enterprises" to the base name of the company. This diversity in naming conventions reflects the formal registration of these companies versus their colloquial or brand recognition names. The input data showcases a mix of American and international corporations, highlighting the global nature of modern businesses.

### Output Column Summary:

The output data simplifies the company names provided in the input column to their most basic and widely recognized forms, removing any legal or formal suffixes such as "Inc", "Corporation", or "Enterprises". This distilled version of the company names focuses on how these entities are most commonly referred to in everyday language and media. The output reflects a standardization process, aiming to present the companies in a uniform manner that is easily identifiable and accessible to a broad audience.

### Relationship Between Input and Output:

The transformation from the input to the output column demonstrates a process of normalization and simplification of company names. This process strips away the formalities and legal designations that accompany a company's registered name to present a cleaner, more recognizable version of the name. This relationship underscores the difference between how companies are officially recognized in a legal or formal business context versus how they are known and referred to in the public domain or in informal settings. The summary operation effectively bridges the gap between the formal identity of a company and its public persona, making it easier for users to identify and relate to the company without the complexities of its full legal name., and input as ['General Electric'] output is General Electric, input as ['General Electric Inc'] output is General Electric, input as ['General Electric Company'] output is General Electric, input as ['Microsoft'] output is Microsoft, input as ['Microsoft Corporation'] output is Microsoft, input as ['Nintendo'] output is Nintendo, input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(company_name):
    # List of common legal and formal suffixes found in company names
    suffixes = [" Inc", " Corporation", " Company", " Enterprises"]
    
    # Remove any of the suffixes from the company name if present
    for suffix in suffixes:
        if company_name.endswith(suffix):
            # Remove the suffix and break the loop as only one suffix will be present
            company_name = company_name.replace(suffix, "")
            break
    
    # Return the simplified company name
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

# End time: 2024-04-09 17:34:22.608228
# Elapsed time in seconds: 9.119440724000015


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

