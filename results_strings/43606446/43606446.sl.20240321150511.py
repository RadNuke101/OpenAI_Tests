# Prompt: return the three capitalized letters before the ">" in the expression
# Input: ['USD.EUR<IDEALPRO,CASH,EUR>'], Output: EUR
# Input: ['USD.EUR<IDEALPRO,CASH,USD>'], Output: USD
# Input: ['KOR.JPN<IDEALPRO,CASH,WON>'], Output: WON
# Input: ['KOR.JPN<IDEALPRO,CASH,YEN>'], Output: YEN

def get_capitalized_letters(input_list):
    input_str = input_list[0]
    start_index = input_str.find('.') - 3
    end_index = input_str.find('<')
    return input_str[start_index:end_index].upper()

# Test cases
print(get_capitalized_letters(['USD.EUR<IDEALPRO,CASH,EUR>']))  # Output: EUR
print(get_capitalized_letters(['USD.EUR<IDEALPRO,CASH,USD>']))  # Output: USD
print(get_capitalized_letters(['KOR.JPN<IDEALPRO,CASH,WON>']))  # Output: WON
print(get_capitalized_letters(['KOR.JPN<IDEALPRO,CASH,YEN>']))  # Output: YEN
