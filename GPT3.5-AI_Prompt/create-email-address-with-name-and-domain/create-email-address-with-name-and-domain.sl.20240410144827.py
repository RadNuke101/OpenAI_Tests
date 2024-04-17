# Start time: 2024-04-10 14:49:50.065886

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1 (First Names):
- The first names in the input data are 'ayako', 'amy', and 'tom'.
- The names are of different lengths and have varying origins or cultural backgrounds.

Summary for Input Column 2 (Last Names):
- The last names in the input data are 'ogawa', 'johnson', and 'chang'.
- The last names are also of different lengths and likely have different cultural origins.

Summary for Input Column 3 (Domains):
- The domains in the input data are 'acme.com', 'google.com', and 'upenn.edu'.
- The domains are from different organizations or institutions and have different extensions.

Summary for Output Column (Concatenated Names):
- The output column combines the first and last names with an underscore in between, followed by the domain.
- The output column shows a pattern of combining the first initial of the first name with the last name, followed by the domain name.
- The output column creates a unique identifier that combines elements from the input columns in a structured format.

Relationship between Input and Output:
- The output column combines elements from the input columns in a specific format to create a unique identifier.
- The output column shows a pattern of using the first initial of the first name and the full last name, followed by the domain.
- The relationship between the input and output is a transformation process that combines qualitative data elements to generate a new structured output., and input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name, domain):
    # Combine the first initial of the first name, full last name, and domain with an underscore
    output = first_name[0] + last_name + "_" + domain
    return output

# Test cases
print(generated_function('ayako', 'ogawa', 'acme.com'))  # Expected output: aogawa_acme.com
print(generated_function('amy', 'johnson', 'google.com'))  # Expected output: ajohnson_google.com
print(generated_function('tom', 'chang', 'upenn.edu'))  # Expected output: tchang_upenn.edu
print(generated_function("ayako", "ogawa", "acme.com"))  ## Output: aogawa_acme.com
print(generated_function("amy", "johnson", "google.com"))  ## Output: ajohnson_google.com
print(generated_function("tom", "chang", "upenn.edu"))  ## Output: tchang_upenn.edu

# End time: 2024-04-10 14:49:52.527950
# Elapsed time in seconds: 2.4620127979999324