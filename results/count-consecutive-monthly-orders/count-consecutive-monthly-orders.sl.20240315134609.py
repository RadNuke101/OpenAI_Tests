def find_repeating_numbers(input_list):
    output_list = []
    for lst in input_list:
        repeated_numbers = set()
        prev_num = None
        count = 1
        for num in lst[0].split():
            if num == prev_num:
                count += 1
            else:
                if count > 1:
                    repeated_numbers.add(prev_num)
                count = 1
            prev_num = num
        if count > 1:
            repeated_numbers.add(prev_num)
        if len(repeated_numbers) > 1:
            output_list.append('3')
        else:
            output_list.append(str(len(repeated_numbers)))
    return output_list

input_list = [['7 0 0 5 4 4'], ['0 0 2 3 3 0'], ['5 6 4 6 0 7'], ['0 4 5 0 0 2'], ['3 0 3 0 1 2'], ['5 3 2 5 6 1']]
print(find_repeating_numbers(input_list))
