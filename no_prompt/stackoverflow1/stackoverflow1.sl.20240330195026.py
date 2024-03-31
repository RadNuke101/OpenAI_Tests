# Start time: 2024-03-30 19:53:02.366341

# Content: Given that given input as ['Trucking Inc.'] output is Trucking, given input as ['New Truck Inc'] output is New Truck, given input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_company_name(input_str):
    try:
        # Input: 'Trucking Inc.'
        # Output: 'Trucking'
        
        # Input: 'New Truck Inc'
        # Output: 'New Truck'
        
        # Input: 'ABV Trucking Inc, LLC'
        # Output: 'ABV Trucking'
        
        # Remove any extra characters at the end of the string
        input_str = input_str.split(',')[0].strip()
        
        # Split the string by spaces
        words = input_str.split()
        
        # Check if the last word is 'Inc.' or 'Inc'
        if words[-1] == 'Inc.' or words[-1] == 'Inc':
            words.pop()
        
        # Join the words back together
        output_str = ' '.join(words)
        
        return output_str
    
    except Exception as e:
        print("Error:", e)
        return None

# Test cases
print(extract_company_name('Trucking Inc.'))  # Output: Trucking
print(extract_company_name('New Truck Inc'))  # Output: New Truck
print(extract_company_name('ABV Trucking Inc, LLC'))  # Output: ABV Trucking

# End time: 2024-03-30 19:53:05.248095
# Elapsed time in seconds: 2.8817093590005243