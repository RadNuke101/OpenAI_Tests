# Start time: 2024-03-30 19:03:13.118121

# Content: Given that given input as ['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'] output is Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK, given input as ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'] output is MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK, given input as ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'] output is Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def transform_string(input_str):
    try:
        # Input: 'Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'
        # Output: 'Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK'
        parts = input_str.split('_')
        if len(parts) >= 5:
            parts[4] = 'Branding' if parts[4] == 'BRD' else parts[4]
            return '_'.join(parts)
        
        # Input: 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'
        # Output: 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK'
        parts = input_str.split('_')
        if len(parts) >= 5:
            parts[4] = 'Leads' if parts[4] == 'LDS' else parts[4]
            return '_'.join(parts)
        
        # Input: 'Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'
        # Output: 'Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK'
        parts = input_str.split('_')
        if len(parts) >= 5:
            parts[4] = 'Direct Response' if parts[4] == 'DRS' else parts[4]
            return '_'.join(parts)
        
        return input_str
    except Exception as e:
        print(f"Error: {e}")
        return input_str

# Test cases
print(transform_string('Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'))  # Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK
print(transform_string('MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'))  # MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK
print(transform_string('Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'))  # Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK

# End time: 2024-03-30 19:03:26.510873
# Elapsed time in seconds: 13.392321724999874