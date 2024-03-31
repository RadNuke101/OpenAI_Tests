# Start time: 2024-03-30 03:30:27.022797
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period, and given input as ['011016_assignment.xlsx', '1'] output is 011016, given input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, given input as ['030116_cost.xlsx', '1'] output is 030116, given input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def extract_text(input_str, n):
    try:
        # Split the input string by period
        parts = input_str.split('.')
        
        # Find the nth and (n-1)th occurrences of the period
        nth_period_index = -1
        prev_period_index = -1
        count = 0
        for i in range(len(input_str)):
            if input_str[i] == '.':
                count += 1
                if count == int(n):
                    nth_period_index = i
                elif count == int(n) - 1:
                    prev_period_index = i
        
        # Extract the text between the nth and (n-1)th periods
        if nth_period_index != -1 and prev_period_index != -1:
            return input_str[prev_period_index + 1:nth_period_index]
        else:
            return "Invalid input"
    except:
        return "Invalid input"

# Input: '011016_assignment.xlsx', '1'
# Output: '011016'
print(extract_text('011016_assignment.xlsx', '1'))

# Input: '011016_assignment.xlsx', '2'
# Output: 'assignment.xlsx'
print(extract_text('011016_assignment.xlsx', '2'))

# Input: '030116_cost.xlsx', '1'
# Output: '030116'
print(extract_text('030116_cost.xlsx', '1'))

# Input: '030116_cost.xlsx', '2'
# Output: 'cost.xlsx'
print(extract_text('030116_cost.xlsx', '2'))

# End time: 2024-03-30 03:30:33.542560
# Elapsed time in seconds: 6.519581598999139