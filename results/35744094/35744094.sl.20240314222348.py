def extract_data(input_data):
    output = []
    for data in input_data:
        url = data[0]
        if '/' in url:
            output.append(url.split('/')[-1])
        else:
            output.append(url.split('www.')[1].split('.com')[0])
    return output

input_data = [['http=//www.apple.com/uk/mac'], ['https=//www.microsoft.com/en-gb/windows'], ['https=//www.microsoft.com/']]
print(extract_data(input_data))
