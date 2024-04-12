# Start time: 2024-04-09 17:52:40.958166

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input column consists of a series of names, each entry containing two parts presumably representing a first name and a last name, although the order is not consistent across all entries. The names appear to be of East Asian origin, specifically Korean, given the common surnames "Kim" and "Lee" which are prevalent in Korean culture. The variation in the order of names within each entry suggests a mix of Westernized (first name followed by last name) and traditional East Asian (last name followed by first name) naming conventions. This inconsistency in naming order within the dataset indicates a need to discern the surname from the given name for each entry, which is crucial for understanding the relationship between the input and the output.

### Output Column Summary:

The output column consistently presents a single name for each entry, which, based on the examples provided, appears to always be the surname from the corresponding input entry. This suggests that the process or rule applied to generate the output from the input involves identifying and extracting the surname from each full name in the input column. The output, therefore, represents a simplified, uniform format focusing solely on the surname component of each full name, disregarding the given names.

### Relationship Summary:

The relationship between the input and output columns is characterized by the extraction and isolation of the surname from a full name that includes both a given name and a surname. This process appears to be agnostic to the order of the names in the input, effectively identifying the surname whether it precedes or follows the given name. The transformation from input to output simplifies the data by reducing each full name to its surname component, providing a consistent, singular focus on family names. This could serve purposes such as grouping, sorting, or analyzing the data based on familial or ancestral lineage, which is significant in cultures where surnames carry substantial social and historical significance. The method of deriving the output from the input demonstrates an understanding of naming conventions and the importance of surnames in the context of the data provided., and input as ['Park Kim'] output is Kim, input as ['Lee Kim'] output is Kim, input as ['Kim Lee'] output is Lee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(full_name):
    # Split the full name into parts
    name_parts = full_name.split()
    
    # Common Korean surnames
    common_surnames = ["Kim", "Lee", "Park"]
    
    # Identify and return the surname
    for part in name_parts:
        if part in common_surnames:
            return part

# Test cases based on the provided examples
print(generated_function("Park Kim"))  # Expected output: Kim
print(generated_function("Lee Kim"))   # Expected output: Kim
print(generated_function("Kim Lee"))   # Expected output: Lee
print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee

# End time: 2024-04-09 17:52:46.382838
# Elapsed time in seconds: 5.42449375599972