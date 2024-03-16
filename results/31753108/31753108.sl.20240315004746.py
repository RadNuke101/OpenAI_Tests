def extract_capitalized_letters(input_list):
    output = []
    for item in input_list:
        phrase = item[0]
        capitalized_letters = ''
        for i in range(len(phrase)):
            if phrase[i].isupper():
                capitalized_letters += phrase[i]
            elif len(capitalized_letters) == 3:
                break
        output.append(capitalized_letters)
    return output

input_list = [['Tire Pressure ABC123873 Monitor'], [' Oil Life ABC849999999021 gauge'], [' Air conditioner GHF211 maintenance']]
print(extract_capitalized_letters(input_list))
