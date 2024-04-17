# Start time: 2024-04-10 14:25:26.018770

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1 (First Names):
- The first names in the input column are 'ayako', 'amy', and 'tom'.
- The names are of Japanese, English, and Western origin, respectively.
- The names are relatively short and have different cultural backgrounds.

Summary for Input Column 2 (Last Names):
- The last names in the input column are 'ogawa', 'johnson', and 'chang'.
- The last names have different origins and cultural backgrounds.
- The last names are relatively common and easy to spell.

Summary for Input Column 3 (Domains):
- The domains in the input column are 'acme.com', 'google.com', and 'upenn.edu'.
- The domains belong to different types of organizations (corporate, search engine, educational institution).
- The domains have different extensions (.com, .edu).

Summary for Output Column (Concatenated Names with Domain):
- The output column combines the first and last names with the domain.
- The output reflects a personalized email address format.
- The output shows a mix of different cultural backgrounds and organizations.

Relationship between Input and Output:
- The output combines the first and last names with the domain to create a personalized email address.
- The input names and domains are diverse, reflecting a mix of cultural backgrounds and organizations.
- The output column showcases a blend of personal identity (names) and professional affiliation (domains)., and input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_name, last_name, domain):
    # Concatenate the first name, last name, and domain with underscores
    output = f"{first_name[0]}{last_name}_{domain}"
    
    return output

# Test cases
print(generated_function('ayako', 'ogawa', 'acme.com'))
print(generated_function('amy', 'johnson', 'google.com'))
print(generated_function('tom', 'chang', 'upenn.edu'))
print(generated_function("ayako", "ogawa", "acme.com"))  ## Output: aogawa_acme.com
print(generated_function("amy", "johnson", "google.com"))  ## Output: ajohnson_google.com
print(generated_function("tom", "chang", "upenn.edu"))  ## Output: tchang_upenn.edu

# End time: 2024-04-10 14:25:27.758137
# Elapsed time in seconds: 1.739332736999998