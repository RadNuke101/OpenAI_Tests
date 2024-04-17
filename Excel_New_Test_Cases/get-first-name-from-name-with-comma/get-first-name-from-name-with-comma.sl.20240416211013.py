# Start time: 2024-04-16 21:10:48.317362

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if second input is 1, return everything after the ",". else if the second input is 2, return everything before the ",", and input as: "Chang,Amy", "1" output is: Amy, input as: "Chang,Amy", "2" output is: Chang, input as: "smith,bobby", "2" output is: smith, input as: "smith,bobby", "1" output is: bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

# Define the generated function
def generated_function(input_str, num):
    # Split the input string by ","
    parts = input_str.split(",")
    
    # Check if the second input is 1
    if num == "1":
        return parts[1]
    # Check if the second input is 2
    elif num == "2":
        return parts[0]

# Test cases
print(generated_function("Chang,Amy", "1"))
print(generated_function("Chang,Amy", "2"))
print(generated_function("smith,bobby", "2"))
print(generated_function("smith,bobby", "1"))



print(generated_function("parker,olivia", "1"))  ### Output: "parker,olivia", "1"
print(generated_function("parker,olivia", "2"))  ### Output: "parker,olivia", "2"
print(generated_function("Turner,Jackson", "2"))  ### Output: "Turner,Jackson", "2"
print(generated_function("Turner,Jackson", "1"))  ### Output: "Turner,Jackson", "1"


print(generated_function("Chang,Amy", "1"))  ## Output: Amy
print(generated_function("Chang,Amy", "2"))  ## Output: Chang
print(generated_function("smith,bobby", "2"))  ## Output: smith
print(generated_function("smith,bobby", "1"))  ## Output: bobby



# End time: 2024-04-16 21:10:50.442406
# Elapsed time in seconds: 2.125002604999999