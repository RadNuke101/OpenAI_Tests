# Start time: 2024-04-10 17:42:48.978446

'''
Prompt:
Given that input as ['Launa', 'Withers'] output is Withers, L., input as ['Lakenya', 'Edison'] output is Edison, L., input as ['Brendan', 'Hage'] output is Hage, B., input as ['Bradford', 'Lango'] output is Lango, B., input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Split the input string into first name and last name
        first_name, last_name = input_str.split(', ')
        
        # Get the first letter of the last name
        last_name_initial = last_name[0]
        
        # Get the first letter of the first name
        first_name_initial = first_name[0]
        
        # Format the output string
        output_str = f"{last_name}, {first_name_initial}."
        
        return output_str
        
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('Launa, Withers'))
print(generated_function('Lakenya, Edison'))
print(generated_function('Brendan, Hage'))
print(generated_function('Bradford, Lango'))
print(generated_function('Rudolf, Akiyama'))
print(generated_function("Launa", "Withers"))  ## Output: Withers, L.
print(generated_function("Lakenya", "Edison"))  ## Output: Edison, L.
print(generated_function("Brendan", "Hage"))  ## Output: Hage, B.
print(generated_function("Bradford", "Lango"))  ## Output: Lango, B.
print(generated_function("Rudolf", "Akiyama"))  ## Output: Akiyama, R.

# End time: 2024-04-10 17:42:52.416304
# Elapsed time in seconds: 3.4378208289999748