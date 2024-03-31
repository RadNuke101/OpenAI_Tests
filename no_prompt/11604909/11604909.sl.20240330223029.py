# Start time: 2024-03-30 22:31:34.262123

# Content: Given that given input as ['AIX 5.1'] output is 5.1, given input as ['VMware ESX Server 3.5.0 build-110268'] output is 3.5, given input as ['Linux Linux 2.6 Linux'] output is 2.6, given input as ['Red Hat Enterprise AS 4 <2.6-78.0.13.ELlargesmp>'] output is 2.6, given input as ['Microsoft <R> Windows <R> 2000 Advanced Server 1.0'] output is 1.0, given input as ['Microsoft Windows XP Win2008R2 6.1.7601'] output is 6.1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_version(input_string):
    # Test cases:
    # input_string = 'AIX 5.1' -> Output: 5.1
    # input_string = 'VMware ESX Server 3.5.0 build-110268' -> Output: 3.5
    # input_string = 'Linux Linux 2.6 Linux' -> Output: 2.6
    # input_string = 'Red Hat Enterprise AS 4 <2.6-78.0.13.ELlargesmp>' -> Output: 2.6
    # input_string = 'Microsoft <R> Windows <R> 2000 Advanced Server 1.0' -> Output: 1.0
    # input_string = 'Microsoft Windows XP Win2008R2 6.1.7601' -> Output: 6.1

    try:
        version = ''
        for char in input_string:
            if char.isdigit() or char == '.':
                version += char
            elif version and char.isalpha():
                break
        return version
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(extract_version('AIX 5.1'))
print(extract_version('VMware ESX Server 3.5.0 build-110268'))
print(extract_version('Linux Linux 2.6 Linux'))
print(extract_version('Red Hat Enterprise AS 4 <2.6-78.0.13.ELlargesmp>'))
print(extract_version('Microsoft <R> Windows <R> 2000 Advanced Server 1.0'))
print(extract_version('Microsoft Windows XP Win2008R2 6.1.7601'))

# End time: 2024-03-30 22:31:42.012078
# Elapsed time in seconds: 7.74976556799993