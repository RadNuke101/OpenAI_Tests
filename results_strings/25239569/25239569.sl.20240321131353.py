def unabbreviate(input_str):
    parts = input_str.split('_')
    for i in range(len(parts)):
        if parts[i] == 'STD':
            next_phrase = parts[i+1]
            unabbreviated = ''
            if next_phrase == 'BRD':
                unabbreviated = 'Branding'
            elif next_phrase == 'LDS':
                unabbreviated = 'Leads'
            elif next_phrase == 'DRS':
                unabbreviated = 'Direct Response'
            parts[i+1] = unabbreviated
    return '_'.join(parts)

# Test cases
print(unabbreviate('Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'))  # Output: Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK
print(unabbreviate('MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'))  # Output: MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK
print(unabbreviate('Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'))  # Output: Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK
Prompt: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response)
