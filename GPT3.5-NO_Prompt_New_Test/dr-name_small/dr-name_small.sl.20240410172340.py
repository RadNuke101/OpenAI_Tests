# Start time: 2024-04-10 17:30:53.332292

'''
Prompt:
Given that input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        name = input_str.split()[0]
        return "Dr. " + name
    except:
        return "Invalid input"

# Test cases
print(generated_function('Nancy FreeHafer'))
print(generated_function('Andrew Cencici'))
print(generated_function('Jan Kotas'))
print(generated_function('Mariya Sergienko'))
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-10 17:30:54.673379
# Elapsed time in seconds: 1.3412828929999705


# APPEND TEST SCRIPTS...
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya


print(generated_function("Smith Logan"))  ### Output: Dr. Smith
print(generated_function("Anderson Lily"))  ### Output: Dr. Anderson
print(generated_function("Carter Liam"))  ### Output: Dr. Carter
print(generated_function("Parker Olivia"))  ### Output: Dr. Parker
print(generated_function("Hayes Gabriel"))  ### Output: Dr. Hayes
print(generated_function("Foster Madison"))  ### Output: Dr. Foster
print(generated_function("Martin Hannah"))  ### Output: Dr. Martin
print(generated_function("Reynolds Emma"))  ### Output: Dr. Reynolds
print(generated_function("Foster Elijah"))  ### Output: Dr. Foster
print(generated_function("Clark Aiden"))  ### Output: Dr. Clark
print(generated_function("Coleman Sophia"))  ### Output: Dr. Coleman
print(generated_function("Adams Chloe"))  ### Output: Dr. Adams
print(generated_function("Cooper Abigail"))  ### Output: Dr. Cooper
print(generated_function("Turner Jackson"))  ### Output: Dr. Turner
print(generated_function("Turner Zoey"))  ### Output: Dr. Turner
print(generated_function("Bennett Ava"))  ### Output: Dr. Bennett
print(generated_function("Brooks Isabella"))  ### Output: Dr. Brooks
print(generated_function("Thompson Mason"))  ### Output: Dr. Thompson
print(generated_function("Johnson Caleb"))  ### Output: Dr. Johnson
print(generated_function("Taylor Harper"))  ### Output: Dr. Taylor
print(generated_function("Nelson Amelia"))  ### Output: Dr. Nelson
print(generated_function("Edwards Carter"))  ### Output: Dr. Edwards
print(generated_function("Mitchell Caleb"))  ### Output: Dr. Mitchell
print(generated_function("Harrison Grace"))  ### Output: Dr. Harrison
print(generated_function("Davis Wyatt"))  ### Output: Dr. Davis
print(generated_function("Walker Scarlett"))  ### Output: Dr. Walker
print(generated_function("Morgan Owen"))  ### Output: Dr. Morgan
print(generated_function("Hayes Benjamin"))  ### Output: Dr. Hayes
print(generated_function("Cooper Nolan"))  ### Output: Dr. Cooper
print(generated_function("Wright Samuel"))  ### Output: Dr. Wright

# TEST SCRIPTS APPENDED!

