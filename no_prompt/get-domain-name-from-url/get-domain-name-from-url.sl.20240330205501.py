# Start time: 2024-03-30 21:02:30.393923

# Content: Given that given input as ['https=//abc.com/def'] output is https=//abc.com/, given input as ['http=//www.abc.com/def/cef'] output is http=//www.abc.com, given input as ['http=//chandoo.org/wp/def-def'] output is http=//chandoo.org/, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_domain(input_str):
    try:
        # Input: 'https=//abc.com/def'
        # Output: 'https=//abc.com/'
        parts = input_str.split('=')
        protocol = parts[0]
        domain = parts[1].split('/')[0]
        return f"{protocol}={domain}/"
    except Exception as e:
        print(f"Error: {e}")

# Test cases
print(extract_domain('https=//abc.com/def'))  # Output: https=//abc.com/
print(extract_domain('http=//www.abc.com/def/cef'))  # Output: http=//www.abc.com
print(extract_domain('http=//chandoo.org/wp/def-def'))  # Output: http=//chandoo.org/

# End time: 2024-03-30 21:02:32.630063
# Elapsed time in seconds: 2.2360802399998647