def find_phrases_starting_with_underscore(input_expression):
    output = []
    for sublist in input_expression:
        for phrase in sublist:
            words = phrase.split()
            for word in words:
                if word.startswith('_'):
                    output.append(word)
                    break
    return output

input_expression = [['this is a _username in the middle'], ['twitter names look like= _name'], ['with two _name1 and _name2']]
print(find_phrases_starting_with_underscore(input_expression))
