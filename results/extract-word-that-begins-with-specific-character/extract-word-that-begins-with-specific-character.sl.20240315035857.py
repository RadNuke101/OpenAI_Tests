def find_phrases_with_underscore(input_expression):
    result = []
    for sublist in input_expression:
        for phrase in sublist:
            words = phrase.split()
            for word in words:
                if word.startswith('_'):
                    result.append(word)
                    break
    return result

input_expression = [['this is a _username in the middle'], ['twitter names look like= _name'], ['with two _name1 and _name2']]
output = find_phrases_with_underscore(input_expression)
print(output)
