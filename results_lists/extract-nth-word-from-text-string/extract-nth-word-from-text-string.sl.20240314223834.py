def return_nth_word(input_list):
    output_list = []
    for item in input_list:
        words = item[0].split()
        n = int(item[1]) - 1
        output_list.append(words[n])
    return output_list

input_list = [['you can do anything but you cant do everything.', '4'], ['you can do anything but you cant do everything.', '1'], ['you can do anything but you cant do everything.', '2'], ['you can do anything but you cant do everything.', '3']]
output = return_nth_word(input_list)
print(output)
