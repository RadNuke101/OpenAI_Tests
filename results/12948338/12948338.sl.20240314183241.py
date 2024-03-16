def count_phrase_in_expression(input_list):
    output = []
    for expression, phrase in input_list:
        count = expression.count(phrase)
        output.append(str(count))
    return output

input_list = [['An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'], ['An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser'], ['An _example string with _example in it is awesome _example', 'example']]
print(count_phrase_in_expression(input_list))
