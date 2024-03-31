# Start time: 2024-03-30 19:29:20.433186

# Content: Given that given input as ['one, 1'] output is one apple, given input as ['two, 2'] output is two bananas, given input as ['three, 3'] output is three strawberries, given input as ['four, 4'] output is four oranges, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def fruit_mapping(input_str):
    try:
        input_list = input_str.split(', ')
        num = int(input_list[1])
        
        if num == 1:
            return f"{input_list[0]} apple"
        elif num == 2:
            return f"{input_list[0]} bananas"
        elif num == 3:
            return f"{input_list[0]} strawberries"
        elif num == 4:
            return f"{input_list[0]} oranges"
        else:
            return "Invalid input"
    
    except (IndexError, ValueError):
        return "Invalid input"

# Test cases
print(fruit_mapping('one, 1'))  # Output: one apple
print(fruit_mapping('two, 2'))  # Output: two bananas
print(fruit_mapping('three, 3'))  # Output: three strawberries
print(fruit_mapping('four, 4'))  # Output: four oranges
print(fruit_mapping('five, 5'))  # Output: Invalid input
print(fruit_mapping('six'))  # Output: Invalid input

# End time: 2024-03-30 19:29:24.294361
# Elapsed time in seconds: 3.8610594000001583