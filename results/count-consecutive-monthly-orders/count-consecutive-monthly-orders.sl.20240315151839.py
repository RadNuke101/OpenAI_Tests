def find_repeating_numbers(input_list):
    def count_repeats(lst):
        count = 1
        max_count = 1
        for i in range(1, len(lst)):
            if lst[i] == lst[i-1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count

    output = []
    for lst in input_list:
        numbers = [int(num) for num in lst[0].split()]
        max_repeats = count_repeats(numbers)
        if max_repeats > 1:
            output.append(str(max_repeats))
        else:
            output.append(str(numbers[-1]))

    return output

input_list = [['7 0 0 5 4 4'], ['0 0 2 3 3 0'], ['5 6 4 6 0 7'], ['0 4 5 0 0 2'], ['3 0 3 0 1 2'], ['5 3 2 5 6 1']]
output = find_repeating_numbers(input_list)
print(output)
