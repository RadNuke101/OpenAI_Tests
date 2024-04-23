# Start time: 2024-04-09 14:45:05.797465

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data column consists of company names that are primarily in the trucking industry. These names are presented in a formal structure, often including legal identifiers such as "Inc." or "LLC" at the end of the company name. The names vary in length and complexity, ranging from simple, straightforward names to more complex ones that may include acronyms or multiple words before the legal identifiers. The commonality across all entries is the presence of an industry descriptor (e.g., "Trucking") and a legal business structure designation (e.g., "Inc.", "LLC").

### Output Column Summary:

The output data column simplifies the company names from the input column by removing the legal identifiers such as "Inc." or "LLC" and retaining the core name of the company. This process results in a cleaner, more concise version of each company name, focusing on the part of the name that most directly represents the company's identity. The output names maintain the industry descriptor (e.g., "Trucking") and any other descriptive or identifying words from the original name, excluding the legal business structure designation.

### Relationship Summary:

The transformation from the input to the output column represents a process of simplification and clarification of company names within the trucking industry. By removing the legal identifiers, the output focuses on the essential elements of each company's name, making it easier to identify and remember. This process does not alter the fundamental identity or industry descriptor of the company; instead, it streamlines the name to its most recognizable and relevant components. The relationship between the input and output columns demonstrates a methodical approach to distilling company names down to their core identities, facilitating clearer communication and recognition of the company names within the context of the trucking industry., and input as ['Trucking Inc.'] output is Trucking, input as ['New Truck Inc'] output is New Truck, input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(company_name):
    # Split the company name by spaces to work with each part
    parts = company_name.split()
    
    # Remove legal identifiers such as "Inc." or "LLC"
    cleaned_parts = [part for part in parts if part not in ["Inc.", "LLC", "Inc", "LLC,"]]
    
    # Join the cleaned parts back together to form the simplified company name
    simplified_name = " ".join(cleaned_parts)
    
    return simplified_name

# Test cases based on the provided examples
print(generated_function('Trucking Inc.'))  # Expected output: Trucking
print(generated_function('New Truck Inc'))  # Expected output: New Truck
print(generated_function('ABV Trucking Inc, LLC'))  # Expected output: ABV Trucking
print(generated_function("Trucking Inc."))  ## Output: Trucking
print(generated_function("New Truck Inc"))  ## Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  ## Output: ABV Trucking

# End time: 2024-04-09 14:45:12.351893
# Elapsed time in seconds: 6.554403390000516


# APPEND TEST SCRIPTS...
print(generated_function("Trucking Inc."))  ## Output: Trucking
print(generated_function("New Truck Inc"))  ## Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  ## Output: ABV Trucking


print(generated_function("New House Inc"))  ### Output: New House
print(generated_function("Brand New House Inc"))  ### Output: Brand New House
print(generated_function("Housing Inc."))  ### Output: Housing
print(generated_function("ABV Housing Inc, LLC"))  ### Output: ABV Housing

# TEST SCRIPTS APPENDED!

