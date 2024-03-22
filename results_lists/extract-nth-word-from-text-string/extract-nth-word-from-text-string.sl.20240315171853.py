def return_nth_word(input_list):
    output = []
    for item in input_list:
        words = item[0].split()
        n = int(item[1])
        output.append(words[n-1])
    return output

input_list = [['you can do anything but you cant do everything.', '4'], ['you can do anything but you cant do everything.', '1'], ['you can do anything but you cant do everything.', '2'], ['you can do anything but you cant do everything.', '3']]
print(return_nth_word(input_list))
