# Start time: 2024-04-10 15:12:21.229769

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column 1:
- The input column 1 contains a list of names in the format "Lastname,Firstname".
- The names in the input column 1 are in a Lastname, Firstname format.

Summary for Input Column 2:
- The input column 2 contains numerical values representing a choice or option.

Summary for Output Column:
- The output column contains the extracted part of the name based on the choice made in input column 2.
- The output column displays either the Firstname or Lastname based on the choice made in input column 2.

Relationship between Input and Output:
- The output column displays the part of the name (Firstname or Lastname) based on the choice made in input column 2.
- If input column 2 is '1', the output displays the Firstname.
- If input column 2 is '2', the output displays the Lastname.
- The relationship between input and output is that the output is determined by the choice made in the input column 2., and input as ['Chang,Amy', '1'] output is Amy, input as ['Chang,Amy', '2'] output is Chang, input as ['smith,bobby', '2'] output is smith, input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(name, choice):
    # Split the name into Lastname and Firstname
    lastname, firstname = name.split(',')
    
    # Check the choice and return the corresponding part of the name
    if choice == '1':
        return firstname.strip()
    elif choice == '2':
        return lastname.strip()

# Test cases
print(generated_function('Chang,Amy', '1'))  # Output: Amy
print(generated_function('Chang,Amy', '2'))  # Output: Chang
print(generated_function('smith,bobby', '2'))  # Output: smith
print(generated_function('smith,bobby', '1'))  # Output: bobby
print(generated_function("Chang,Amy", "1"))  ## Output: Amy
print(generated_function("Chang,Amy", "2"))  ## Output: Chang
print(generated_function("smith,bobby", "2"))  ## Output: smith
print(generated_function("smith,bobby", "1"))  ## Output: bobby

# End time: 2024-04-10 15:12:23.990831
# Elapsed time in seconds: 2.7609937889997127