def extract_data(input_str):
    if '/' in input_str:
        return input_str.split('/')[-1]
    else:
        return input_str.split('www.')[1].split('.com')[0]

# Prompt: if there is data after last "/", return that data, else return the phrase that starts after "www." and ends before ".com"
# Input: 'http=//www.apple.com/uk/mac'
# Output: 'mac'

# Input: 'https=//www.microsoft.com/en-gb/windows'
# Output: 'windows'

# Input: 'https=//www.microsoft.com/'
# Output: 'microsoft'
