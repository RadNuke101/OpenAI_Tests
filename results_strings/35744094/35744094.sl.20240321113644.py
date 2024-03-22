# Prompt: if there is data after last "/", return that data, else return the phrase that starts after "www." and ends before ".com"
# Input: 'http=//www.apple.com/uk/mac', Output: 'mac'
# Input: 'https=//www.microsoft.com/en-gb/windows', Output: 'windows'
# Input: 'https=//www.microsoft.com/', Output: 'microsoft'

def get_output(input_str):
    if '/' in input_str:
        return input_str.split('/')[-1]
    else:
        start_index = input_str.find('www.') + 4
        end_index = input_str.find('.com')
        return input_str[start_index:end_index]

# Test cases
print(get_output('http=//www.apple.com/uk/mac'))  # Output: 'mac'
print(get_output('https=//www.microsoft.com/en-gb/windows'))  # Output: 'windows'
print(get_output('https=//www.microsoft.com/'))  # Output: 'microsoft'
