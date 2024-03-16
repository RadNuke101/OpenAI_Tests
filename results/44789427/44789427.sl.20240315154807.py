def extract_dates(data):
    result = []
    for entry in data:
        if entry[1] == '1':
            result.append(entry[0].split('-')[0])
        elif entry[1] == '2':
            result.append(entry[0].split('-')[1])
    return result

data = [['1/17/16-1/18/17', '1'], ['1/17/16-1/18/17', '2'], ['01/17/2016-01/18/2017', '1'], ['01/17/2016-01/18/2017', '2']]
output = extract_dates(data)
print(output)
