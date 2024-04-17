# Start time: 2024-04-16 20:56:57.641154

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: first return everything after the "," in the inputted expression, followed by a comma, and then everything before the "," in the inputted expression, and input as: ['chang,amy'] output is: amy,chang, input as: ['smith,bobby'] output is: bobby,smith, input as: ['lennox,aaron'] output is: aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

def generated_function(input_str):
    # Split the input string by ","
    parts = input_str.split(',')
    # Rearrange the parts and join them with a comma
    return parts[1] + ',' + parts[0]

# Test cases
print(generated_function('chang,amy'))
print(generated_function('smith,bobby'))
print(generated_function('lennox,aaron'))



print(generated_function("hayes,benjamin"))  ### Output: "hayes,benjamin"
print(generated_function("parker,olivia"))  ### Output: "parker,olivia"
print(generated_function("turner,jackson"))  ### Output: "turner,jackson"


print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox



# End time: 2024-04-16 20:56:58.935838
# Elapsed time in seconds: 1.2946909439999956