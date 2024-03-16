def extract_data(input_data):
    output = []
    for item in input_data:
        url = item[0]
        if '/' in url:
            output.append(url.split('/')[-1])
        else:
            output.append(url.split('www.')[1].split('.com')[0])
    return output

input_data = [['http=//www.apple.com/uk/mac'], ['https=//www.microsoft.com/en-gb/windows'], ['https=//www.microsoft.com/']]
output = extract_data(input_data)
print(output)
