def find_repeating_numbers(input_list):
    output_list = []
    for sublist in input_list:
        numbers = sublist[0].split()
        repeated_numbers = set([num for num in numbers if numbers.count(num) > 1])
        if len(repeated_numbers) > 1:
            output_list.append('3')
        else:
            output_list.append(str(len(repeated_numbers)))
    return output_list

input_list = [['7 0 0 5 4 4'], ['0 0 2 3 3 0'], ['5 6 4 6 0 7'], ['0 4 5 0 0 2'], ['3 0 3 0 1 2'], ['5 3 2 5 6 1']]
output_list = find_repeating_numbers(input_list)
print(output_list)
