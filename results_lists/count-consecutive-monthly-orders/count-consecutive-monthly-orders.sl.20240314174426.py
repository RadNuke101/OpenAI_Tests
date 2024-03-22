def find_repeating_numbers(input_list):
    output_list = []
    for sublist in input_list:
        numbers = sublist[0].split()
        count_dict = {}
        for num in numbers:
            if num in count_dict:
                count_dict[num] += 1
                if count_dict[num] > 1:
                    output_list.append('3')
                    break
            else:
                count_dict[num] = 1
        else:
            output_list.append(str(len(set(numbers))))
    
    return output_list

input_list = [['7 0 0 5 4 4'], ['0 0 2 3 3 0'], ['5 6 4 6 0 7'], ['0 4 5 0 0 2'], ['3 0 3 0 1 2'], ['5 3 2 5 6 1']]
output_list = find_repeating_numbers(input_list)
print(output_list)
