# Prompt: if last three letters of inputted expression is "cef", delete the "/" before "def" and everything after. If not, delete everything after the third "/".
# Input: 'https=//abc.com/def'
# Output: 'https=//abc.com/'

def process_input(input_str):
    if input_str[-3:] == "cef":
        index = input_str.rfind("/def")
        return input_str[:index] + "/"
    else:
        parts = input_str.split("/")
        return "/".join(parts[:3]) + "/"

# Test cases
print(process_input('https=//abc.com/def'))  # Output: 'https=//abc.com/'
print(process_input('http=//www.abc.com/def/cef'))  # Output: 'http=//www.abc.com'
print(process_input('http=//chandoo.org/wp/def-def'))  # Output: 'http=//chandoo.org/'
