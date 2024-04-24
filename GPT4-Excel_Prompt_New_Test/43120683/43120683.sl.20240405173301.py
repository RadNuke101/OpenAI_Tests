# Start time: 2024-04-05 17:56:23.275782

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the input followed by a space, and if there is a 1 in the input return "apple", if there is a 2 in the input return "bananas", if there is a 3 in the input return "strawberries", if there is a 4 in the input return "oranges", and input as ['one, 1'] output is one apple, input as ['two, 2'] output is two bananas, input as ['three, 3'] output is three strawberries, input as ['four, 4'] output is four oranges, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Splitting the input string to analyze its parts
    parts = input_string.split(", ")
    first_word = parts[0]
    number_part = parts[1] if len(parts) > 1 else ""

    # Mapping numbers to fruits
    fruit_map = {
        "1": "apple",
        "2": "bananas",
        "3": "strawberries",
        "4": "oranges"
    }

    # Determining the fruit based on the number in the input
    fruit = fruit_map.get(number_part, "")

    # Constructing the output string
    output = f"{first_word} {fruit}"
    return output

# Test cases
print(generated_function('one, 1'))
print(generated_function('two, 2'))
print(generated_function('three, 3'))
print(generated_function('four, 4'))
print(generated_function("one, 1"))  ## Output: one apple
print(generated_function("two, 2"))  ## Output: two bananas
print(generated_function("three, 3"))  ## Output: three strawberries
print(generated_function("four, 4"))  ## Output: four oranges

# End time: 2024-04-05 17:56:29.244101
# Elapsed time in seconds: 5.967996529000629


# APPEND TEST SCRIPTS...
print(generated_function("one, 1"))  ## Output: one apple
print(generated_function("two, 2"))  ## Output: two bananas
print(generated_function("three, 3"))  ## Output: three strawberries
print(generated_function("four, 4"))  ## Output: four oranges


print(generated_function("one, 3"))  ### Output: one strawberries
print(generated_function("three, 4"))  ### Output: three oranges
print(generated_function("two, 1"))  ### Output: two apple
print(generated_function("four, 2"))  ### Output: four bananas

# TEST SCRIPTS APPENDED!

