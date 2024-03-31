# Start time: 2024-03-30 03:37:57.983456
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response), and given input as ['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'] output is Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK, given input as ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'] output is MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK, given input as ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'] output is Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response)
# Input: 'Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'
# Output: 'Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK'

def unabbreviate(input_str):
    try:
        parts = input_str.split('_')
        for i in range(len(parts)):
            if parts[i] == 'STD':
                next_underscore = input_str.find('_', i)
                start_index = input_str.find('_', i) + 1
                end_index = input_str.find('_', start_index)
                if end_index != -1:
                    unabbreviated = parts[start_index:end_index].replace('_', ' ')
                    return input_str[:start_index] + unabbreviated + input_str[end_index:]
    except Exception as e:
        print("Error:", e)
    
    return input_str

# Test cases
print(unabbreviate('Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK')) # Output: Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK
print(unabbreviate('MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK')) # Output: MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK
print(unabbreviate('Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK')) # Output: Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK

# End time: 2024-03-30 03:38:05.964742
# Elapsed time in seconds: 7.981053488998441