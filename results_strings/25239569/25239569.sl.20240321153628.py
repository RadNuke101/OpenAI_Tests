def unabbreviate(input_str):
    parts = input_str.split('_')
    for i in range(len(parts)):
        if parts[i] == 'STD':
            next_phrase = parts[i+1]
            if next_phrase == 'BRD':
                parts[i+1] = 'Branding'
            elif next_phrase == 'LDS':
                parts[i+1] = 'Leads'
            elif next_phrase == 'DRS':
                parts[i+1] = 'Direct Response'
    return '_'.join(parts)

# Prompt: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response)
# Input: 'Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'
# Output: 'Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK'

# Input: 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'
# Output: 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK'

# Input: 'Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'
# Output: 'Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK'

input_str = 'Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'
print(unabbreviate(input_str))

input_str = 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'
print(unabbreviate(input_str))

input_str = 'Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'
print(unabbreviate(input_str))
Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK
MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK
Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK
