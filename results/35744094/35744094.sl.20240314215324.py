def extract_data(input_data):
    output = []
    for item in input_data:
        data = item[0]
        if data.rfind("/") != -1:
            output.append(data[data.rfind("/") + 1:])
        else:
            start_index = data.find("www.") + 4
            end_index = data.find(".com")
            output.append(data[start_index:end_index])
    return output

input_data = [['http=//www.apple.com/uk/mac'], ['https=//www.microsoft.com/en-gb/windows'], ['https=//www.microsoft.com/']]
output = extract_data(input_data)
print(output)
