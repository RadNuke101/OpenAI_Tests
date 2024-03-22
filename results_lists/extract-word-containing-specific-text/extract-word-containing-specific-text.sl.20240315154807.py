def find_phrases_with_com(input_list):
    result = []
    for sublist in input_list:
        for phrase in sublist:
            words = phrase.split()
            for word in words:
                if word.endswith(".com"):
                    result.append(word.strip())
    return result

input_list = [['send email to json_acme.com'], ['contact help_robot.com for all support requests']]
output = find_phrases_with_com(input_list)
print(output)
