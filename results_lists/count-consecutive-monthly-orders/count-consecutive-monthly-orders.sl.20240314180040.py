def check_repeats(input_list):
    def count_repeats(row):
        counts = {}
        for num in row:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for count in counts.values():
            if count > 1:
                return '3'
        return str(len(row))

    return [count_repeats(row[0].split()) for row in input_list]

input_list = [['7 0 0 5 4 4'], ['0 0 2 3 3 0'], ['5 6 4 6 0 7'], ['0 4 5 0 0 2'], ['3 0 3 0 1 2'], ['5 3 2 5 6 1']]
output = check_repeats(input_list)
print(output)
