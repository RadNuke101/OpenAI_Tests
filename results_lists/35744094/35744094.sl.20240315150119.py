def extract_data(input_data):
    output = []
    for data in input_data:
        if data[0].rfind("/") != -1:
            output.append(data[0][data[0].rfind("/") + 1:])
        else:
            start_index = data[0].find("www.") + 4
            end_index = data[0].find(".com")
            output.append(data[0][start_index:end_index])
    return output

input_data = [['http=//www.apple.com/uk/mac'], ['https=//www.microsoft.com/en-gb/windows'], ['https=//www.microsoft.com/']]
print(extract_data(input_data))
