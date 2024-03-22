def find_repeating_numbers(input_list):
    def check_repeating_numbers(lst):
        for i in range(len(lst) - 1):
            if lst[i] == lst[i + 1]:
                return True
        return False

    output = []
    for lst in input_list:
        numbers = [int(num) for num in lst[0].split()]
        if check_repeating_numbers(numbers):
            output.append('3')
        else:
            output.append(str(len(set(numbers))))

    return output

input_list = [['7 0 0 5 4 4'], ['0 0 2 3 3 0'], ['5 6 4 6 0 7'], ['0 4 5 0 0 2'], ['3 0 3 0 1 2'], ['5 3 2 5 6 1']]
output = find_repeating_numbers(input_list)
print(output)
