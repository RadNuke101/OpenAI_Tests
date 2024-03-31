# Start time: 2024-03-30 00:32:17.548186
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period, and given input as ['011016_assignment.xlsx', '1'] output is 011016, given input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, given input as ['030116_cost.xlsx', '1'] output is 030116, given input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def extract_text(input_str, n):
    try:
        # Input: ['011016_assignment.xlsx', '1']
        # Output: 011016
        # Prompt: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period
        parts = input_str.split('.')
        if n == 1:
            return parts[0]
        else:
            return parts[n - 1]

    except Exception as e:
        return "Error: Invalid input"

# Test cases
print(extract_text('011016_assignment.xlsx', 1))  # Output: 011016
print(extract_text('011016_assignment.xlsx', 2))  # Output: assignment.xlsx
print(extract_text('030116_cost.xlsx', 1))  # Output: 030116
print(extract_text('030116_cost.xlsx', 2))  # Output: cost.xlsx

# End time: 2024-03-30 00:32:20.783524
# Elapsed time in seconds: 3.2353062040001532