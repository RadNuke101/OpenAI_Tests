# Start time: 2024-04-05 18:29:46.074745

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if "—" present, delete that and everything after "|", and input as ['TL-18273982| 10MM'] output is TL-18273982, input as ['TL-288762| 76DK'] output is TL-288762, input as ['CT-576'] output is CT-576, input as ['N/A'] output is N/A, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Check if "-" is present in the input string
    if "-" in input_string:
        # Split the input string at "|", if "|" is present, and take the first part
        output_string = input_string.split("|")[0].strip()
    else:
        # If "-" is not present, return the input string as is
        output_string = input_string
    return output_string

# Test cases
print(generated_function('TL-18273982| 10MM'))  # Expected output: TL-18273982
print(generated_function('TL-288762| 76DK'))    # Expected output: TL-288762
print(generated_function('CT-576'))             # Expected output: CT-576
print(generated_function('N/A'))                # Expected output: N/A
print(generated_function("TL-18273982| 10MM"))  ## Output: TL-18273982
print(generated_function("TL-288762| 76DK"))  ## Output: TL-288762
print(generated_function("CT-576"))  ## Output: CT-576
print(generated_function("N/A"))  ## Output: N/A

# End time: 2024-04-05 18:29:51.247651
# Elapsed time in seconds: 5.172813355000471