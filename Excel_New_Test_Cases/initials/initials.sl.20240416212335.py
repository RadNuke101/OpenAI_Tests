# Start time: 2024-04-16 21:26:26.268901

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first letter of the first word in the inputted phrase, followed by a period, and then the first letter of the second word, followed by a period, and input as: "Nancy FreeHafer" output is: N.F., input as: "Andrew Cencici" output is: A.C., input as: "Jan Kotas" output is: J.K., input as: "Mariya Sergienko" output is: M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

def generated_function(input_str):
    # Split the input string into words
    words = input_str.split()
    
    # Extract the first letter of each word and join them with a period
    output = '.'.join([word[0] for word in words]) + '.'
    
    return output



print(generated_function("Mason Thompson"))  ### Output: "Mason Thompson"
print(generated_function("Scarlett Walker"))  ### Output: "Scarlett Walker"
print(generated_function("Logan Smith"))  ### Output: "Logan Smith"
print(generated_function("Samuel Wright"))  ### Output: "Samuel Wright"
print(generated_function("Gabriel Hayes"))  ### Output: "Gabriel Hayes"
print(generated_function("Abigail Cooper"))  ### Output: "Abigail Cooper"
print(generated_function("Zoey Turner"))  ### Output: "Zoey Turner"
print(generated_function("Carter Edwards"))  ### Output: "Carter Edwards"
print(generated_function("Lily Anderson"))  ### Output: "Lily Anderson"
print(generated_function("Benjamin Hayes"))  ### Output: "Benjamin Hayes"
print(generated_function("Olivia Parker"))  ### Output: "Olivia Parker"
print(generated_function("Grace Harrison"))  ### Output: "Grace Harrison"
print(generated_function("Sophia Coleman"))  ### Output: "Sophia Coleman"
print(generated_function("Aiden Clark"))  ### Output: "Aiden Clark"
print(generated_function("Liam Carter"))  ### Output: "Liam Carter"
print(generated_function("Wyatt Davis"))  ### Output: "Wyatt Davis"
print(generated_function("Elijah Foster"))  ### Output: "Elijah Foster"
print(generated_function("Hannah Martin"))  ### Output: "Hannah Martin"
print(generated_function("Jackson Turner"))  ### Output: "Jackson Turner"
print(generated_function("Caleb Johnson"))  ### Output: "Caleb Johnson"
print(generated_function("Isabella Brooks"))  ### Output: "Isabella Brooks"
print(generated_function("Amelia Nelson"))  ### Output: "Amelia Nelson"
print(generated_function("Caleb Mitchell"))  ### Output: "Caleb Mitchell"
print(generated_function("Chloe Adams"))  ### Output: "Chloe Adams"
print(generated_function("Madison Foster"))  ### Output: "Madison Foster"
print(generated_function("Nolan Cooper"))  ### Output: "Nolan Cooper"
print(generated_function("Ava Bennett"))  ### Output: "Ava Bennett"
print(generated_function("Owen Morgan"))  ### Output: "Owen Morgan"
print(generated_function("Harper Taylor"))  ### Output: "Harper Taylor"
print(generated_function("Emma Reynolds"))  ### Output: "Emma Reynolds"


print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.



# End time: 2024-04-16 21:26:27.321444
# Elapsed time in seconds: 1.0525126919999934