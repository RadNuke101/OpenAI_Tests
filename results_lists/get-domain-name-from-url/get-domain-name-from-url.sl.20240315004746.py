def process_input(input_list):
    output = []
    for item in input_list:
        expression = item[0]
        if expression[-3:] == "cef":
            index = expression.find("/def")
            output.append(expression[:index] + "/")
        else:
            index = expression.rfind("/")
            output.append(expression[:index])
    return output

input_list = [['https=//abc.com/def'], ['http=//www.abc.com/def/cef'], ['http=//chandoo.org/wp/def-def']]
output = process_input(input_list)
print(output)
