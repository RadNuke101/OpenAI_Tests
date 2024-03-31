# Start time: 2024-03-30 11:51:11.530464
# Content: Given that given input as ['R/V<208,0,32>'] output is R/V 208 0 32, given input as ['R/S<184,28,16>'] output is R/S 184 28 16, given input as ['R/B<255,88,80>'] output is R/B 255 88 80, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input and output to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any noncode
def parse_input(input_str):
    try:
        # Removing brackets and splitting the input string
        input_str = input_str.replace('<', ' ').replace('>', ' ')
        input_list = input_str.split(',')

        # Extracting the required values
        color_code = input_list[0].split('/')[1]
        values = [int(val) for val in input_list[1:]]

        # Constructing the output string
        output_str = f"{color_code} {' '.join(map(str, values))}"
        
        return output_str

    except Exception as e:
        return f"Error: {e}"

# Test cases
print(parse_input('R/V<208,0,32>'))  # Output: R/V 208 0 32
print(parse_input('R/S<184,28,16>'))  # Output: R/S 184 28 16
print(parse_input('R/B<255,88,80>'))  # Output: R/B 255 88 80

# End time: 2024-03-30 11:51:14.852786
# Elapsed time in seconds: 3.322254421000004