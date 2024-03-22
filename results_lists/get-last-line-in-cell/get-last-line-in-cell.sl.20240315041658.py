def process_input(input_list):
    output_list = []
    for item in input_list:
        if item.count("2015") > 1:
            output_list.append(item.split("/n")[-1])
        else:
            output_list.append(item)
    return output_list

input_list = [['11/1/2015 - First call/n12/3/2015-order placed/n11/15/2015-follow-up,interested'], ['11/1/2015 - First call/n12/3/2015-order placed'], ['11/1/2015 - First call']]
output = process_input(input_list)
print(output)
