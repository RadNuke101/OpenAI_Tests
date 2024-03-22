def extract_data(input_data):
    output = []
    for item in input_data:
        if item[0].endswith('/'):
            output.append(item[0].split('/')[-2])
        else:
            output.append(item[0].split('www.')[1].split('.com')[0])
    return output

input_data = [['http=//www.apple.com/uk/mac'], ['https=//www.microsoft.com/en-gb/windows'], ['https=//www.microsoft.com/']]
output = extract_data(input_data)
print(output)
