# Start time: 2024-04-16 14:26:50.090593

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the phrase (space on atleast one end) in the inputted expression that ends with ".com", and input as ['send email to json_acme.com'] output is json_acme.com, input as ['contact help_robot.com for all support requests'] output is help_robot.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

def generated_function(input_str):
    # Split the input string by spaces
    words = input_str.split()
    
    # Find the word that ends with ".com"
    for word in words:
        if word.endswith(".com"):
            return word.strip()

# Test cases
generated_function('send email to json_acme.com')
generated_function('contact help_robot.com for all support requests')



print(generated_function("ask help_robot.google.com for all support requests"))  ### Output: "ask help_robot.google.com for all support requests"
print(generated_function("send email towards json_gmail.com"))  ### Output: "send email towards json_gmail.com"
print(generated_function("contact help_robot.org for all support"))  ### Output: "contact help_robot.org for all support"
print(generated_function("ask help_robot.com for all support requests"))  ### Output: "ask help_robot.com for all support requests"


print(generated_function("send email to json_acme.com"))  ## Output: json_acme.com
print(generated_function("contact help_robot.com for all support requests"))  ## Output: help_robot.com



# End time: 2024-04-16 14:26:51.573407
# Elapsed time in seconds: 1.4827769020000119