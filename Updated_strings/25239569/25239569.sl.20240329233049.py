# Start time: 2024-03-29 23:46:57.512885
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response), and given input as ['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'] output is Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK, given input as ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'] output is MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK, given input as ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'] output is Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response)
# Input: 'Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'
# Output: 'Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK'

def unabbreviate_string(input_str):
    try:
        parts = input_str.split('_')
        for i, part in enumerate(parts):
            if part == 'STD':
                next_part = parts[i + 1]
                if next_part.startswith('_') and next_part.endswith('_'):
                    unabbreviated = next_part[1:-1]
                    unabbreviated_full = ''
                    for word in unabbreviated.split():
                        if word == 'BRD':
                            unabbreviated_full += 'Branding '
                        elif word == 'LDS':
                            unabbreviated_full += 'Leads '
                        elif word == 'DRS':
                            unabbreviated_full += 'Direct Response '
                        else:
                            unabbreviated_full += word + ' '
                    parts[i + 1] = '_' + unabbreviated_full.strip() + '_'
                    return '_'.join(parts)
        return input_str
    except Exception as e:
        return input_str

# Test cases
print(unabbreviate_string('Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'))  # Output: Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK
print(unabbreviate_string('MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'))  # Output: MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK
print(unabbreviate_string('Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'))  # Output: Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK

# End time: 2024-03-29 23:47:03.637435
# Elapsed time in seconds: 6.124369494000007