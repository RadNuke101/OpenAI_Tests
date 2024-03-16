def count_newlines(input_list):
    output = []
    for expression in input_list:
        count = expression[0].count('/n') + 1
        output.append(str(count))
    return output

input_list = [['one'], ['one/ntwo'], ['one/ntwo/nthree']]
output = count_newlines(input_list)
print(output)
