def extract_info(input_list):
    result = []
    for item in input_list:
        file_name = item[0]
        n = int(item[1])
        periods = [i for i, char in enumerate(file_name) if char == '.']
        if n <= len(periods):
            start = periods[n-1] + 1
            end = periods[n] - 1
            result.extend([file_name[start:end], file_name[end+1:]])
    return result

input_list = [['011016_assignment.xlsx', '1'], ['011016_assignment.xlsx', '2'], ['030116_cost.xlsx', '1'], ['030116_cost.xlsx', '2']]
output = extract_info(input_list)
print(output)
