# Start time: 2024-04-10 15:56:26.330786

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1 ('ayako', 'ogawa', 'acme.com'):
- The names in this column are 'ayako' and 'ogawa'.
- Both names have a different number of characters.
- The names do not follow a specific pattern or theme.

Summary for Input Column 2 ('amy', 'johnson', 'google.com'):
- The names in this column are 'amy' and 'johnson'.
- Both names have a different number of characters.
- The second name is longer than the first name.
- The second name is a common surname.

Summary for Input Column 3 ('acme.com', 'google.com', 'upenn.edu'):
- The domains in this column are 'acme.com', 'google.com', and 'upenn.edu'.
- Each domain has a different length and structure.
- The domains represent different types of organizations (company, search engine, university).

Summary for Output Column ('aogawa_acme.com', 'ajohnson_google.com', 'tchang_upenn.edu'):
- The output combines the first initial of the first name with the last name, followed by an underscore, and then the domain.
- The output creates a unique identifier for each input by combining elements from different columns.
- The output maintains the original structure and order of the input data., and input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(first_name, last_name, domain):
    # Combine the first initial of the first name with the last name, followed by an underscore, and then the domain
    output = first_name[0] + last_name + '_' + domain
    return output

# Test cases
print(generated_function('ayako', 'ogawa', 'acme.com'))  # Output: aogawa_acme.com
print(generated_function('amy', 'johnson', 'google.com'))  # Output: ajohnson_google.com
print(generated_function('tom', 'chang', 'upenn.edu'))  # Output: tchang_upenn.edu
print(generated_function("ayako", "ogawa", "acme.com"))  ## Output: aogawa_acme.com
print(generated_function("amy", "johnson", "google.com"))  ## Output: ajohnson_google.com
print(generated_function("tom", "chang", "upenn.edu"))  ## Output: tchang_upenn.edu

# End time: 2024-04-10 15:56:28.176106
# Elapsed time in seconds: 1.8452754519994414


# APPEND TEST SCRIPTS...
print(generated_function("ayako", "ogawa", "acme.com"))  ## Output: aogawa_acme.com
print(generated_function("amy", "johnson", "google.com"))  ## Output: ajohnson_google.com
print(generated_function("tom", "chang", "upenn.edu"))  ## Output: tchang_upenn.edu


print(generated_function("ayako", "ogawa", "apple.com"))  ### Output: aogawa_apple.com
print(generated_function("tom", "chang", "banana.org"))  ### Output: tchang_banana.org
print(generated_function("ayako", "ogawa", "usa.gov"))  ### Output: aogawa_usa.gov
print(generated_function("amy", "johnson", "gmail.com"))  ### Output: ajohnson_gmail.com
print(generated_function("tom", "chang", "harvard.edu"))  ### Output: tchang_harvard.edu

# TEST SCRIPTS APPENDED!

