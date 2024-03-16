def process_phrases(phrases):
    result = []
    for phrase in phrases:
        if len(phrase[0].split()) > 1:
            result.append(phrase[0].split()[0])
        else:
            result.append('')
    return result

input_phrases = [['The quick brown fox.'], ['quick brown fox.'], ['fox']]
output_result = process_phrases(input_phrases)
print(output_result)
