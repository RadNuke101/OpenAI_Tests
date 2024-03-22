def process_data(input_data):
    output = []
    for item in input_data:
        if item.count("2015") > 1:
            output.append(item.split("/n")[-1])
        else:
            output.append(item)
    return output

input_data = [['11/1/2015 - First call/n12/3/2015-order placed/n11/15/2015-follow-up,interested'], ['11/1/2015 - First call/n12/3/2015-order placed'], ['11/1/2015 - First call']]
print(process_data(input_data))
