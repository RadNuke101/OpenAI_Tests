def count_newlines(lst):
    return [str(1 + x[0].count("/n")) for x in lst]

input_lst = [['one'], ['one/ntwo'], ['one/ntwo/nthree']]
output_lst = count_newlines(input_lst)
print(output_lst)
