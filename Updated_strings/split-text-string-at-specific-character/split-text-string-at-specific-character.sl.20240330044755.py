# Start time: 2024-03-30 04:56:21.737756
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period, and given input as ['011016_assignment.xlsx', '1'] output is 011016, given input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, given input as ['030116_cost.xlsx', '1'] output is 030116, given input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def extract_string(input_str, n):
    try:
        periods = [i for i, char in enumerate(input_str) if char == '.']
        if n > len(periods) or n < 1:
            return "Invalid input for n"
        
        end_index = periods[n-1]
        start_index = periods[n-2] if n > 1 else 0
        
        while start_index > 0 and input_str[start_index] != '.':
            start_index -= 1
        
        return input_str[start_index+1:end_index]
    
    except Exception as e:
        return str(e)

# Input: '011016_assignment.xlsx', '1'
# Output: '011016'
# Prompt: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period
print(extract_string('011016_assignment.xlsx', 1))

# Input: '011016_assignment.xlsx', '2'
# Output: 'assignment.xlsx'
print(extract_string('011016_assignment.xlsx', 2))

# Input: '030116_cost.xlsx', '1'
# Output: '030116'
print(extract_string('030116_cost.xlsx', 1))

# Input: '030116_cost.xlsx', '2'
# Output: 'cost.xlsx'
print(extract_string('030116_cost.xlsx', 2))

# End time: 2024-03-30 04:56:24.230744
# Elapsed time in seconds: 2.4930741810021573