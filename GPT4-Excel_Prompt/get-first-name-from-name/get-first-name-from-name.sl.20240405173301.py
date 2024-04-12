# Start time: 2024-04-05 17:44:42.397997

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, and input as ['Susan Ann Chang'] output is Susan, input as ['Ayako Tanaka'] output is Ayako, input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phrase):
    # Split the input phrase by spaces and return the first word
    return phrase.split()[0]

# Test cases
result1 = generated_function('Susan Ann Chang')
result2 = generated_function('Ayako Tanaka')
result3 = generated_function('Bobby T. smth')

# You can print the results to verify the correct outputs
print(result1)  # Expected output: Susan
print(result2)  # Expected output: Ayako
print(result3)  # Expected output: Bobby
print(generated_function("Susan Ann Chang"))  ## Output: Susan
print(generated_function("Ayako Tanaka"))  ## Output: Ayako
print(generated_function("Bobby T. smth"))  ## Output: Bobby

# End time: 2024-04-05 17:44:48.746444
# Elapsed time in seconds: 6.348275778999778