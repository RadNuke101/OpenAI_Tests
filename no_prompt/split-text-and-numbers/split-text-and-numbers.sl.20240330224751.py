# Start time: 2024-03-30 22:54:48.962498

# Content: Given that given input as ['apples30', '7'] output is apples, given input as ['peaches24', '8'] output is peaches, given input as ['peaches0', '8'] output is peaches, given input as ['pears', '6'] output is pears, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_fruit(input_str):
    try:
        # Split the input string into fruit name and quantity
        fruit, quantity = input_str.split(',')

        # Remove any digits from the fruit name
        fruit_name = ''.join([i for i in fruit if not i.isdigit()])

        return fruit_name.strip()

    except Exception as e:
        return "Invalid input"

# Test cases
print(extract_fruit('apples30,7'))  # Output: apples
print(extract_fruit('peaches24,8'))  # Output: peaches
print(extract_fruit('peaches0,8'))  # Output: peaches
print(extract_fruit('pears,6'))  # Output: pears

# End time: 2024-03-30 22:54:50.612137
# Elapsed time in seconds: 1.649600475000625