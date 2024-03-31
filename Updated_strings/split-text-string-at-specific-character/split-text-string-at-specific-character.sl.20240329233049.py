# Start time: 2024-03-29 23:39:12.987613
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period, and given input as ['011016_assignment.xlsx', '1'] output is 011016, given input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, given input as ['030116_cost.xlsx', '1'] output is 030116, given input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def extract_text(input_str, n):
    try:
        n = int(n)
        if n <= 0:
            raise ValueError("n must be a positive integer")
        
        periods = [pos for pos, char in enumerate(input_str) if char == '.']
        
        if n > len(periods):
            return "n is greater than the number of periods in the input string"
        
        end_pos = periods[n-1]
        start_pos = periods[n-2] if n > 1 else 0
        
        return input_str[start_pos+1:end_pos]
    
    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)

# Input: '011016_assignment.xlsx', '1'
# Output: 011016
# Prompt: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period
# Example: extract_text('011016_assignment.xlsx', '1') -> '011016'

# End time: 2024-03-29 23:39:16.376598
# Elapsed time in seconds: 3.38888495599997