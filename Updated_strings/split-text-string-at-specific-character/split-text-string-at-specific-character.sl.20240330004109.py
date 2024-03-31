# Start time: 2024-03-30 00:49:08.804758
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period, and given input as ['011016_assignment.xlsx', '1'] output is 011016, given input as ['011016_assignment.xlsx', '2'] output is assignment.xlsx, given input as ['030116_cost.xlsx', '1'] output is 030116, given input as ['030116_cost.xlsx', '2'] output is cost.xlsx, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
def extract_text(input_str, n):
    try:
        # Split the input string by periods
        parts = input_str.split('.')
        
        # Find the nth and (n-1)th occurrences of the period
        start_index = 0
        end_index = 0
        count = 0
        for i in range(len(parts)):
            if parts[i]:
                count += 1
                if count == int(n):
                    start_index = i
                if count == int(n) + 1:
                    end_index = i
                    break
        
        # Extract the desired text between the nth and (n-1)th occurrences of the period
        output = '.'.join(parts[start_index:end_index])
        
        return output
    except Exception as e:
        return str(e)

# Test cases
print(extract_text('011016_assignment.xlsx', '1'))  # Output: 011016
print(extract_text('011016_assignment.xlsx', '2'))  # Output: assignment.xlsx
print(extract_text('030116_cost.xlsx', '1'))  # Output: 030116
print(extract_text('030116_cost.xlsx', '2'))  # Output: cost.xlsx

# End time: 2024-03-30 00:49:14.297325
# Elapsed time in seconds: 5.492438901999776