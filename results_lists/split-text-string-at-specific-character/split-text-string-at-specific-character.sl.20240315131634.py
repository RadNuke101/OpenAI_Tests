def extract_info(input_list):
    result = []
    for item in input_list:
        file_name = item[0]
        n = int(item[1])
        periods = [pos for pos, char in enumerate(file_name) if char == '.']
        if n <= len(periods):
            end_pos = periods[n]
            start_pos = periods[n-1] + 1
            result.extend([file_name[start_pos:end_pos], file_name[end_pos+1:]])
    return result

input_list = [['011016_assignment.xlsx', '1'], ['011016_assignment.xlsx', '2'], ['030116_cost.xlsx', '1'], ['030116_cost.xlsx', '2']]
output = extract_info(input_list)
print(output)