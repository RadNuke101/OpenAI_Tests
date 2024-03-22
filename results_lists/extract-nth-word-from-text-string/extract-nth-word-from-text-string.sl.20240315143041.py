def return_nth_word(input_data):
    output = []
    for data in input_data:
        sentence = data[0]
        n = int(data[1])
        words = sentence.split()
        output.append(words[n-1])
    return output

input_data = [['you can do anything but you cant do everything.', '4'], ['you can do anything but you cant do everything.', '1'], ['you can do anything but you cant do everything.', '2'], ['you can do anything but you cant do everything.', '3']]
print(return_nth_word(input_data))
