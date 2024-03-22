def extract_info(input_list):
    output = []
    for item in input_list:
        filename = item[0]
        n = int(item[1])
        periods = [pos for pos, char in enumerate(filename) if char == '.']
        if n <= len(periods) and n > 1:
            end_pos = periods[n-1]
            start_pos = periods[n-2] + 1
            output.append(filename[start_pos:end_pos])
            output.append(filename[end_pos+1:])
    return output

input_list = [['011016_assignment.xlsx', '1'], ['011016_assignment.xlsx', '2'], ['030116_cost.xlsx', '1'], ['030116_cost.xlsx', '2']]
print(extract_info(input_list))
