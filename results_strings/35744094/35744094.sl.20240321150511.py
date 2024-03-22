def get_data(input_str):
    # Prompt: if there is data after last "/", return that data, else return the phrase that starts after "www." and ends before ".com"
    
    # Input: 'http=//www.apple.com/uk/mac'
    # Output: 'mac'
    
    # Input: 'https=//www.microsoft.com/en-gb/windows'
    # Output: 'windows'
    
    # Input: 'https=//www.microsoft.com/'
    # Output: 'microsoft'
    
    if '/' in input_str:
        return input_str.rsplit('/', 1)[-1]
    else:
        return input_str.split('www.', 1)[-1].split('.com', 1)[0]

# Test cases
print(get_data('http=//www.apple.com/uk/mac'))  # Output: mac
print(get_data('https=//www.microsoft.com/en-gb/windows'))  # Output: windows
print(get_data('https=//www.microsoft.com/'))  # Output: microsoft
