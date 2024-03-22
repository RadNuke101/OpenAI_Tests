def find_repeating_numbers(input_list):
    def has_repeating_numbers(row):
        numbers = row.split()
        for i in range(len(numbers) - 1):
            if numbers[i] == numbers[i+1]:
                return True
        return False

    output = []
    for row in input_list:
        if has_repeating_numbers(row[0]):
            output.append('3')
        else:
            unique_numbers = set(row[0].split())
            output.append(str(len(unique_numbers)))

    return output

input_list = [['7 0 0 5 4 4'], ['0 0 2 3 3 0'], ['5 6 4 6 0 7'], ['0 4 5 0 0 2'], ['3 0 3 0 1 2'], ['5 3 2 5 6 1']]
output = find_repeating_numbers(input_list)
print(output)
