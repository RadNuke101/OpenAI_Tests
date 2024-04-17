# Start time: 2024-04-10 17:30:20.592533

'''
Prompt:
Given that input as ['Launa', 'Withers'] output is Withers, L., input as ['Lakenya', 'Edison'] output is Edison, L., input as ['Brendan', 'Hage'] output is Hage, B., input as ['Bradford', 'Lango'] output is Lango, B., input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Split the input string into first and last name
        names = input_str.split(', ')
        last_name = names[1]
        first_name = names[0][0] + '.'

        return last_name + ', ' + first_name
    except:
        return "Invalid input"

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

# End time: 2024-04-10 17:30:21.945881
# Elapsed time in seconds: 1.355068053000025