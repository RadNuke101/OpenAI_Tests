def unabbreviate(input_str):
    parts = input_str.split('_')
    for i in range(len(parts)):
        if parts[i] == 'STD':
            next_phrase = parts[i+1]
            unabbreviated_phrase = ''
            if next_phrase == 'BRD':
                unabbreviated_phrase = 'Branding'
            elif next_phrase == 'LDS':
                unabbreviated_phrase = 'Leads'
            elif next_phrase == 'DRS':
                unabbreviated_phrase = 'Direct Response'
            parts[i+1] = unabbreviated_phrase
    return '_'.join(parts)

# Input: 'Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'
# Output: 'Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK'

# Input: 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'
# Output: 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK'

# Input: 'Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'
# Output: 'Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK'
