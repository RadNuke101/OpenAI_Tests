def extract_numbers(data):
    result = []
    for item in data:
        numbers = item[0].split('-')
        result.append(numbers[1])
    return result
