def remove_that(input_phrases):
    output_phrases = []
    for phrase in input_phrases:
        if len(phrase[0].split()) == 1:
            output_phrases.append(phrase[0])
        else:
            updated_phrase = phrase[0].replace('that', '')
            output_phrases.append(updated_phrase)
    return output_phrases

input_phrases = [['thatensures'], ['thatwill'], ['thathave'], ['knowthat'], ['that'], ['mouse'], ['knowthat']]
output = ['ensures', 'will', 'have', 'know', 'that', 'mouse', 'know']

print(remove_that(input_phrases))
