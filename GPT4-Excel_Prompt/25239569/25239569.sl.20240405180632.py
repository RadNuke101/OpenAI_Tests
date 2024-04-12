# Start time: 2024-04-05 18:37:33.459620

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response), and input as ['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'] output is Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK, input as ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'] output is MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK, input as ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'] output is Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Dictionary mapping abbreviations to their unabbreviated forms
    abbreviations = {
        "BRD": "Branding",
        "LDS": "Leads",
        "DRS": "Direct Response"
    }
    
    # Split the input string to find the first abbreviation after "STD"
    parts = input_string.split("STD")
    
    # Ensure there are at least two parts and the second part is not empty to avoid IndexError
    if len(parts) > 1 and parts[1]:
        # Split the second part by "_" to find individual elements
        elements = parts[1].split("_")
        
        # Iterate through elements to find and replace the first abbreviation
        for i, element in enumerate(elements):
            if element in abbreviations:
                # Replace the abbreviation with its unabbreviated form
                elements[i] = abbreviations[element]
                break  # Stop after replacing the first abbreviation
        
        # Reconstruct the second part of the input string
        parts[1] = "_".join(elements)
        
    # Reconstruct the full input string with the abbreviation replaced
    output_string = "STD".join(parts)
    
    return output_string

# Test cases
print(generated_function('Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'))
print(generated_function('MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'))
print(generated_function('Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'))
print(generated_function("Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK"))  ## Output: Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK
print(generated_function("MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK"))  ## Output: MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK
print(generated_function("Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK"))  ## Output: Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK

# End time: 2024-04-05 18:37:42.835239
# Elapsed time in seconds: 9.375442702999862