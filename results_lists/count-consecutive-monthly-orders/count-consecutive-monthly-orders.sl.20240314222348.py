def find_repeating_numbers(input_list):
    def count_repeats(row):
        counts = {}
        for num in row:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        max_repeat = max(counts.values())
        return max_repeat if max_repeat > 1 else 1

    output = []
    for row in input_list:
        row = list(map(int, row[0].split()))
        max_repeat = count_repeats(row)
        output.append(str(max_repeat))

    return output

input_list = [['7 0 0 5 4 4'], ['0 0 2 3 3 0'], ['5 6 4 6 0 7'], ['0 4 5 0 0 2'], ['3 0 3 0 1 2'], ['5 3 2 5 6 1']]
output_list = find_repeating_numbers(input_list)
print(output_list)
