def return_nth_word(input_list):
    output_list = []
    for item in input_list:
        sentence = item[0]
        n = int(item[1])
        words = sentence.split()
        output_list.append(words[n-1])
    return output_list

input_list = [['you can do anything but you cant do everything.', '4'], ['you can do anything but you cant do everything.', '1'], ['you can do anything but you cant do everything.', '2'], ['you can do anything but you cant do everything.', '3']]
print(return_nth_word(input_list))
