# Start time: 2024-03-30 23:19:55.061237

# Content: Given that given input as ['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'] output is Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK, given input as ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'] output is MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK, given input as ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'] output is Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_string(input_str):
    try:
        # Input: 'Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'
        # Output: 'Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK'
        
        # Input: 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'
        # Output: 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK'
        
        # Input: 'Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'
        # Output: 'Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK'
        
        parts = input_str.split('_')
        if len(parts) >= 5:
            parts[4] = parts[4].capitalize()
            return '_'.join(parts)
        else:
            return input_str
    except Exception as e:
        print(f"Error: {e}")
        return input_str

# Test cases
print(format_string('Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'))
print(format_string('MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'))
print(format_string('Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'))

# End time: 2024-03-30 23:20:02.163813
# Elapsed time in seconds: 7.102405142999487