def get_first_word(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split()[0])
    return output_list

input_list = [['Susan Ann Chang'], ['Ayako Tanaka'], ['Bobby T. smth']]
print(get_first_word(input_list))
