def extract_info(input_list):
    result = []
    for item in input_list:
        filename = item[0]
        n = int(item[1])
        periods = [pos for pos, char in enumerate(filename) if char == '.']
        if n <= len(periods):
            end_pos = periods[n - 1]
            start_pos = periods[n - 2] + 1 if n > 1 else 0
            result.append(filename[start_pos:end_pos])
            result.append(filename[end_pos+1:])
    return result

input_list = [['011016_assignment.xlsx', '1'], ['011016_assignment.xlsx', '2'], ['030116_cost.xlsx', '1'], ['030116_cost.xlsx', '2']]
output = extract_info(input_list)
print(output)
