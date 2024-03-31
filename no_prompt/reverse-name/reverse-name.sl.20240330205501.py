# Start time: 2024-03-30 21:10:54.640501

# Content: Given that given input as ['Launa', 'Withers'] output is Withers Launa, given input as ['Lakenya', 'Edison'] output is Edison Lakenya, given input as ['Brendan', 'Hage'] output is Hage Brendan, given input as ['Bradford', 'Lango'] output is Lango Bradford, given input as ['Rudolf', 'Akiyama'] output is Akiyama Rudolf, given input as ['Lara', 'Constable'] output is Constable Lara, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def rearrange_names(input_str):
    try:
        first_name, last_name = input_str.split()
        return f"{last_name} {first_name}"
    except ValueError:
        print("Input format should be 'First Last'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(rearrange_names('Launa Withers'))  # Output: Withers Launa
print(rearrange_names('Lakenya Edison'))  # Output: Edison Lakenya
print(rearrange_names('Brendan Hage'))  # Output: Hage Brendan
print(rearrange_names('Bradford Lango'))  # Output: Lango Bradford
print(rearrange_names('Rudolf Akiyama'))  # Output: Akiyama Rudolf
print(rearrange_names('Lara Constable'))  # Output: Constable Lara

# End time: 2024-03-30 21:11:00.746017
# Elapsed time in seconds: 6.105380734999926