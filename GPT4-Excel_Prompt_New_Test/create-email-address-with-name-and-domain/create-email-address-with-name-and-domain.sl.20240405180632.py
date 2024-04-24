# Start time: 2024-04-05 18:09:32.068621

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: take the first letter of the first input and add it to the front of the second input, then add "_" to the end, and then add the third input to the end, and input as ['ayako', 'ogawa', 'acme.com'] output is aogawa_acme.com, input as ['amy', 'johnson', 'google.com'] output is ajohnson_google.com, input as ['tom', 'chang', 'upenn.edu'] output is tchang_upenn.edu, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(first_input, second_input, third_input):
    # Take the first letter of the first input
    first_letter = first_input[0]
    # Add it to the front of the second input
    modified_second_input = first_letter + second_input
    # Add "_" to the end, and then add the third input
    result = modified_second_input + "_" + third_input
    return result

# Test cases
generated_function('ayako', 'ogawa', 'acme.com')  # Expected output: aogawa_acme.com
generated_function('amy', 'johnson', 'google.com')  # Expected output: ajohnson_google.com
generated_function('tom', 'chang', 'upenn.edu')  # Expected output: tchang_upenn.edu
print(generated_function("ayako", "ogawa", "acme.com"))  ## Output: aogawa_acme.com
print(generated_function("amy", "johnson", "google.com"))  ## Output: ajohnson_google.com
print(generated_function("tom", "chang", "upenn.edu"))  ## Output: tchang_upenn.edu

# End time: 2024-04-05 18:09:39.220189
# Elapsed time in seconds: 7.151354253999671


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

