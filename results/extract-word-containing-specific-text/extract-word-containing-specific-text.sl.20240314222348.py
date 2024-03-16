def find_phrase_with_com(input_list):
    output = []
    for sublist in input_list:
        for phrase in sublist:
            words = phrase.split()
            for word in words:
                if word.endswith(".com"):
                    output.append(word)
    return output

input_list = [['send email to json_acme.com'], ['contact help_robot.com for all support requests']]
print(find_phrase_with_com(input_list))
