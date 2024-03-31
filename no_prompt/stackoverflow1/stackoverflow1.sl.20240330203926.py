# Start time: 2024-03-30 20:41:46.581429

# Content: Given that given input as ['Trucking Inc.'] output is Trucking, given input as ['New Truck Inc'] output is New Truck, given input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_company_name(input_str):
    try:
        # Input: 'Trucking Inc.'
        # Output: 'Trucking'
        
        # Input: 'New Truck Inc'
        # Output: 'New Truck'
        
        # Input: 'ABV Trucking Inc, LLC'
        # Output: 'ABV Trucking'
        
        # Removing common suffixes from company names
        suffixes = ['Inc.', 'Inc', 'LLC', 'LLC.', 'Ltd', 'Ltd.', 'Co', 'Co.']
        for suffix in suffixes:
            if input_str.endswith(suffix):
                input_str = input_str.replace(suffix, '').strip()
        
        # Splitting the company name by space and returning the first part
        company_name = input_str.split()[0]
        
        return company_name
        
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test cases
print(extract_company_name('Trucking Inc.'))  # Output: Trucking
print(extract_company_name('New Truck Inc'))  # Output: New Truck
print(extract_company_name('ABV Trucking Inc, LLC'))  # Output: ABV Trucking

# End time: 2024-03-30 20:41:51.835553
# Elapsed time in seconds: 5.253988121000475