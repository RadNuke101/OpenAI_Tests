# Start time: 2024-03-30 21:21:44.996790

# Content: Given that given input as ['7 0 0 5 4 4'] output is 3, given input as ['0 0 2 3 3 0'] output is 3, given input as ['5 6 4 6 0 7'] output is 4, given input as ['0 4 5 0 0 2'] output is 2, given input as ['3 0 3 0 1 2'] output is 2, given input as ['5 3 2 5 6 1'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test Cases:
# Input: '7 0 0 5 4 4', Output: 3
# Input: '0 0 2 3 3 0', Output: 3
# Input: '5 6 4 6 0 7', Output: 4
# Input: '0 4 5 0 0 2', Output: 2
# Input: '3 0 3 0 1 2', Output: 2
# Input: '5 3 2 5 6 1', Output: 6

def find_unique_number(input_str):
    try:
        # Convert input string to a list of integers
        nums = list(map(int, input_str.split()))

        # Count occurrences of each number
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        # Find the unique number
        for num, count in count_dict.items():
            if count == 1:
                return num

    except ValueError:
        print("Invalid input. Please provide a string of space-separated integers.")
    except Exception as e:
        print("An error occurred:", e)

# Test the function with the provided test cases
input_str = '7 0 0 5 4 4'
print(find_unique_number(input_str))

input_str = '0 0 2 3 3 0'
print(find_unique_number(input_str))

input_str = '5 6 4 6 0 7'
print(find_unique_number(input_str))

input_str = '0 4 5 0 0 2'
print(find_unique_number(input_str))

input_str = '3 0 3 0 1 2'
print(find_unique_number(input_str))

input_str = '5 3 2 5 6 1'
print(find_unique_number(input_str))

# End time: 2024-03-30 21:21:54.857116
# Elapsed time in seconds: 9.86008295800093