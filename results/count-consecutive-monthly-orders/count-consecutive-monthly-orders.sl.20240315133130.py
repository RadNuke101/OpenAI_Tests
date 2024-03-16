def find_repeating_numbers(input_list):
    output_list = []
    for sublist in input_list:
        numbers = sublist[0].split()
        repeating_numbers = set()
        prev_num = None
        count = 1
        for num in numbers:
            if num == prev_num:
                count += 1
            else:
                count = 1
            if count > 1:
                repeating_numbers.add(num)
            prev_num = num
        if len(repeating_numbers) > 1:
            output_list.append('3')
        else:
            output_list.append(str(len(repeating_numbers)))
    return output_list

input_list = [['7 0 0 5 4 4'], ['0 0 2 3 3 0'], ['5 6 4 6 0 7'], ['0 4 5 0 0 2'], ['3 0 3 0 1 2'], ['5 3 2 5 6 1']]
output_list = find_repeating_numbers(input_list)
print(output_list)
