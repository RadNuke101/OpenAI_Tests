def return_nth_word(input_list):
    output = []
    for item in input_list:
        sentence = item[0]
        n = int(item[1])
        words = sentence.split()
        if n <= len(words):
            output.append(words[n-1])
    return output

input_list = [['you can do anything but you cant do everything.', '4'], ['you can do anything but you cant do everything.', '1'], ['you can do anything but you cant do everything.', '2'], ['you can do anything but you cant do everything.', '3']]
output = return_nth_word(input_list)
print(output)
