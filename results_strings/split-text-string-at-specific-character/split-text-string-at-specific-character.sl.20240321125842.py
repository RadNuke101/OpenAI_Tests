def extract_text(input_str, n):
    periods = [i for i, char in enumerate(input_str) if char == '.']
    if n > len(periods) or n < 1:
        return "Invalid input"
    end_index = periods[n-1]
    start_index = periods[n-2] if n > 1 else 0
    return input_str[start_index+1:end_index]

# Prompt: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period
# Input: '011016_assignment.xlsx', '1'
# Output: '011016'
# Input: '011016_assignment.xlsx', '2'
# Output: 'assignment.xlsx'
# Input: '030116_cost.xlsx', '1'
# Output: '030116'
# Input: '030116_cost.xlsx', '2'
# Output: 'cost.xlsx'
