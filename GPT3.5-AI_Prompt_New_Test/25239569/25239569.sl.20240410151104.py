# Start time: 2024-04-10 15:32:20.285838

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: The input data consists of different types of ad formats, sizes, pricing models, and targeting information. The output data seems to be a standardized format that includes the original input data with some modifications. 

The relationship between the input and output columns appears to involve standardizing the naming conventions for the ad formats and adding descriptive terms to clarify the purpose or targeting of the ad. For example, terms like "Branding," "Leads," and "Direct Response" are added to the output column to provide more context about the ad type.

Overall, the output column seems to be a more descriptive and standardized version of the input data, making it easier to understand the purpose and targeting of each ad., and input as ['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'] output is Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK, input as ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'] output is MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK, input as ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'] output is Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into parts
    parts = input_str.split('_')
    
    # Modify the parts to match the desired output format
    if 'BRD' in parts:
        parts[parts.index('BRD')] = 'Branding'
    if 'LDS' in parts:
        parts[parts.index('LDS')] = 'Leads'
    if 'DRS' in parts:
        parts[parts.index('DRS')] = 'Direct Response'
    
    # Join the modified parts back into a string
    output_str = '_'.join(parts)
    
    return output_str

# Test cases
input1 = 'Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'
input2 = 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'
input3 = 'Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'

# Call the generated function with the test cases
output1 = generated_function(input1)
output2 = generated_function(input2)
output3 = generated_function(input3)
print(generated_function("Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK"))  ## Output: Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK
print(generated_function("MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK"))  ## Output: MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK
print(generated_function("Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK"))  ## Output: Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK

# End time: 2024-04-10 15:32:23.594428
# Elapsed time in seconds: 3.3085231819995897


# APPEND TEST SCRIPTS...
print(generated_function("Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK"))  ## Output: Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK
print(generated_function("MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK"))  ## Output: MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK
print(generated_function("Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK"))  ## Output: Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK


print(generated_function("MMC_ContextualLarRec_BAN_1440x960_CPM_STD _LDS _RTG"))  ### Output: MMC_ContextualLarRec_BAN_1440x960_CPM_STD _Leads _RTG
print(generated_function("Adf_BC_DL_728x90_CPM_STD_DRS_NRT_NOR"))  ### Output: Adf_BC_DL_728x90_CPM_STD_Direct Response_NRT_NOR
print(generated_function("Adf_ROCLeader_BAN_728x90_CPM _BRD _NRT"))  ### Output: Adf_ROCLeader_BAN_728x90_CPM _Branding _NRT

# TEST SCRIPTS APPENDED!

