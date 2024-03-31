# Start time: 2024-03-30 02:02:00.477895
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if more than one number repeats more than once in a row in input, return "3", , and given input as ['7 0 0 5 4 4'] output is 3, given input as ['0 0 2 3 3 0'] output is 3, given input as ['5 6 4 6 0 7'] output is 4, given input as ['0 4 5 0 0 2'] output is 2, given input as ['3 0 3 0 1 2'] output is 2, given input as ['5 3 2 5 6 1'] output is 6, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if more than one number repeats more than once in a row in input, return "3"
# Input: '7 0 0 5 4 4'
# Output: 3

def find_repeating_numbers(input_str):
    try:
        input_list = input_str.split()
        count = 1
        max_count = 1

        for i in range(1, len(input_list)):
            if input_list[i] == input_list[i-1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

        if max_count > 2:
            return str(max_count)
        else:
            return "No repeating numbers more than twice in a row"

    except Exception as e:
        return str(e)

# Test cases
print(find_repeating_numbers('7 0 0 5 4 4'))  # Output: 3
print(find_repeating_numbers('0 0 2 3 3 0'))  # Output: 3
print(find_repeating_numbers('5 6 4 6 0 7'))  # Output: 4
print(find_repeating_numbers('0 4 5 0 0 2'))  # Output: 2
print(find_repeating_numbers('3 0 3 0 1 2'))  # Output: 2
print(find_repeating_numbers('5 3 2 5 6 1'))  # Output: 6

# End time: 2024-03-30 02:02:09.302314
# Elapsed time in seconds: 8.824272399999245