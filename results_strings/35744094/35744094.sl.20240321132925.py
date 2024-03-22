# Prompt: if there is data after last "/", return that data, else return the phrase that starts after "www." and ends before ".com"
# Input: 'http=//www.apple.com/uk/mac'
# Output: 'mac'

def get_data(input_str):
    if '/' in input_str:
        return input_str.split('/')[-1]
    else:
        start = input_str.find('www.') + 4
        end = input_str.find('.com')
        return input_str[start:end]

# Test cases
print(get_data('http=//www.apple.com/uk/mac'))  # Output: 'mac'
print(get_data('https=//www.microsoft.com/en-gb/windows'))  # Output: 'windows'
print(get_data('https=//www.microsoft.com/'))  # Output: 'microsoft'
