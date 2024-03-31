# Start time: 2024-03-30 20:08:49.207319

# Content: Given that given input as ['Trucking Inc.'] output is Trucking, given input as ['New Truck Inc'] output is New Truck, given input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_company_name(input_str):
    try:
        # Input: 'Trucking Inc.'
        # Output: 'Trucking'
        
        # Input: 'New Truck Inc'
        # Output: 'New Truck'
        
        # Input: 'ABV Trucking Inc, LLC'
        # Output: 'ABV Trucking'
        
        if ',' in input_str:
            input_str = input_str.split(',')[0]
        
        input_str = input_str.replace(' Inc.', '').replace(' LLC', '')
        words = input_str.split()
        
        if len(words) == 1:
            return words[0]
        elif len(words) == 2:
            return ' '.join(words)
        else:
            return ' '.join(words[:-1])
    
    except Exception as e:
        print("Error:", e)
        return None

# Test cases
print(extract_company_name('Trucking Inc.'))  # Output: Trucking
print(extract_company_name('New Truck Inc'))  # Output: New Truck
print(extract_company_name('ABV Trucking Inc, LLC'))  # Output: ABV Trucking

# End time: 2024-03-30 20:08:53.310613
# Elapsed time in seconds: 4.103249656999651