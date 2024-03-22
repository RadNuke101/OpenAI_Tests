def extract_text(input_str, n):
    periods = [i for i, char in enumerate(input_str) if char == '.']
    start = periods[n-1] + 1
    end = periods[n] - 1
    return input_str[start:end]

# Prompt: in the first input, return everything between the nth (n = second input) occurance of the period and the prior occurance of the period
# Input: '011016_assignment.xlsx', '1'
# Output: '011016'
# Input: '011016_assignment.xlsx', '2'
# Output: 'assignment.xlsx'
# Input: '030116_cost.xlsx', '1'
# Output: '030116'
# Input: '030116_cost.xlsx', '2'
# Output: 'cost.xlsx'
