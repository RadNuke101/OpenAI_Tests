# Start time: 2024-03-30 01:42:14.584931
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period, and given input as ['011016_assignment.xlsx', '1'] output is 011016, given input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, given input as ['030116_cost.xlsx', '1'] output is 030116, given input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def extract_text(input_str, n):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError("n must be a positive integer")
        
        periods = [i for i, char in enumerate(input_str) if char == '.']
        
        if n > len(periods):
            raise ValueError("n is greater than the number of periods in the input string")
        
        end_index = periods[n-1]
        start_index = periods[n-2] if n > 1 else 0
        
        while start_index > 0 and input_str[start_index] != '.':
            start_index -= 1
        
        return input_str[start_index+1:end_index]
    
    except ValueError as e:
        return str(e)

# Input: '011016_assignment.xlsx', '1'
# Output: '011016'
# Prompt: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period
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

# End time: 2024-03-30 01:42:18.602340
# Elapsed time in seconds: 4.017332418000478