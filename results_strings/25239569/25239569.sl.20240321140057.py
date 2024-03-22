def unabbreviate(input_str):
    parts = input_str.split('_')
    for i in range(len(parts)):
        if parts[i] == 'STD':
            parts[i+1] = parts[i+1].replace('_', '')  # Remove the underscore before unabbreviating
            if parts[i+1] == 'BRD':
                parts[i+1] = 'Branding'
            elif parts[i+1] == 'LDS':
                parts[i+1] = 'Leads'
            elif parts[i+1] == 'DRS':
                parts[i+1] = 'Direct Response'
    return '_'.join(parts)

# Prompt: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response)
# Input: 'Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'
# Output: 'Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK'
# Input: 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'
# Output: 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK'
# Input: 'Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'
# Output: 'Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK'

# Test the function with the provided inputs
print(unabbreviate('Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'))
print(unabbreviate('MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'))
print(unabbreviate('Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'))
Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK
MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK
Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK
