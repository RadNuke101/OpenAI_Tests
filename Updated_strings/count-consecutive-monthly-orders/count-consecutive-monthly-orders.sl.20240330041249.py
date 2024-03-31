# Start time: 2024-03-30 04:23:29.760964
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if more than one number repeats more than once in a row in input, return "3", , and given input as ['7 0 0 5 4 4'] output is 3, given input as ['0 0 2 3 3 0'] output is 3, given input as ['5 6 4 6 0 7'] output is 4, given input as ['0 4 5 0 0 2'] output is 2, given input as ['3 0 3 0 1 2'] output is 2, given input as ['5 3 2 5 6 1'] output is 6, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if more than one number repeats more than once in a row in input, return "3"
# Input: ['7 0 0 5 4 4'], Output: 3
# Input: ['0 0 2 3 3 0'], Output: 3
# Input: ['5 6 4 6 0 7'], Output: 4
# Input: ['0 4 5 0 0 2'], Output: 2
# Input: ['3 0 3 0 1 2'], Output: 2
# Input: ['5 3 2 5 6 1'], Output: 6

def find_repeating_number(input_str):
    try:
        input_list = input_str.split()
        count = 1
        max_count = 1
        prev_num = input_list[0]

        for num in input_list[1:]:
            if num == prev_num:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
            prev_num = num

        if max_count > 1:
            return str(max_count)
        else:
            return "No repeating numbers in a row"

    except Exception as e:
        return str(e)

# Test the function with the given inputs
print(find_repeating_number('7 0 0 5 4 4'))  # Output: 3
print(find_repeating_number('0 0 2 3 3 0'))  # Output: 3
print(find_repeating_number('5 6 4 6 0 7'))  # Output: 4
print(find_repeating_number('0 4 5 0 0 2'))  # Output: 2
print(find_repeating_number('3 0 3 0 1 2'))  # Output: 2
print(find_repeating_number('5 3 2 5 6 1'))  # Output: 6

# End time: 2024-03-30 04:23:33.389054
# Elapsed time in seconds: 3.6279791409979225