def process_input(input_list):
    output_list = []
    for item in input_list:
        if item[0][-3:] == "cef":
            output_list.append(item[0].split("/def")[0])
        else:
            output_list.append(item[0].split("/", 3)[0] + "/")
    return output_list

input_list = [['https=//abc.com/def'], ['http=//www.abc.com/def/cef'], ['http=//chandoo.org/wp/def-def']]
output = process_input(input_list)
print(output)
