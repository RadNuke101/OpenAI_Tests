def unabbreviate(input_list):
    output_list = []
    for item in input_list:
        unabbreviated = item[0].replace('STD', 'Standard')
        unabbreviated = unabbreviated.replace('_BRD', ' Branding')
        unabbreviated = unabbreviated.replace('_LDS', ' Leads')
        unabbreviated = unabbreviated.replace('_RTG', ' Rating')
        unabbreviated = unabbreviated.replace('_DRS', ' Direct Response')
        unabbreviated = unabbreviated.replace('_NRT', ' Non-Retargeting')
        unabbreviated = unabbreviated.replace('_NOR', ' Normal')
        output_list.append(unabbreviated)
    return output_list

input_list = [['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'], ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'], ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK']]
print(unabbreviate(input_list))
