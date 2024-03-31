# Start time: 2024-03-30 19:05:49.102763

# Content: Given that given input as ['AIX 5.1'] output is 5.1, given input as ['VMware ESX Server 3.5.0 build-110268'] output is 3.5, given input as ['Linux Linux 2.6 Linux'] output is 2.6, given input as ['Red Hat Enterprise AS 4 <2.6-78.0.13.ELlargesmp>'] output is 2.6, given input as ['Microsoft <R> Windows <R> 2000 Advanced Server 1.0'] output is 1.0, given input as ['Microsoft Windows XP Win2008R2 6.1.7601'] output is 6.1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_version(input_string):
    try:
        version = None
        words = input_string.split()
        for word in words:
            if '.' in word:
                version = word
                break
        if version is None:
            raise ValueError("Version not found in input string")
        return version
    except Exception as e:
        print(f"Error extracting version: {e}")

# Test cases
input1 = 'AIX 5.1'  # Output: 5.1
input2 = 'VMware ESX Server 3.5.0 build-110268'  # Output: 3.5
input3 = 'Linux Linux 2.6 Linux'  # Output: 2.6
input4 = 'Red Hat Enterprise AS 4 <2.6-78.0.13.ELlargesmp>'  # Output: 2.6
input5 = 'Microsoft <R> Windows <R> 2000 Advanced Server 1.0'  # Output: 1.0
input6 = 'Microsoft Windows XP Win2008R2 6.1.7601'  # Output: 6.1

print(extract_version(input1))
print(extract_version(input2))
print(extract_version(input3))
print(extract_version(input4))
print(extract_version(input5))
print(extract_version(input6))

# End time: 2024-03-30 19:05:51.882547
# Elapsed time in seconds: 2.779699230999995