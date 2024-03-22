def extract_capitalized_letters(input_list):
    output = []
    for item in input_list:
        phrase = item[0]
        capitalized_letters = ''
        for char in phrase:
            if char.isupper():
                capitalized_letters += char
            elif capitalized_letters:
                break
        output.append(capitalized_letters)
    return output

input_list = [['Tire Pressure ABC123873 Monitor'], [' Oil Life ABC849999999021 gauge'], [' Air conditioner GHF211 maintenance']]
output = extract_capitalized_letters(input_list)
print(output)
