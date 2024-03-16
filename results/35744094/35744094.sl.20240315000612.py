def extract_data(input_data):
    output = []
    for item in input_data:
        if len(item[0].split('/')[-1]) > 0:
            output.append(item[0].split('/')[-1])
        else:
            output.append(item[0].split('www.')[1].split('.com')[0])
    return output

input_data = [['http=//www.apple.com/uk/mac'], ['https=//www.microsoft.com/en-gb/windows'], ['https=//www.microsoft.com/']]
print(extract_data(input_data))
