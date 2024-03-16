def unabbreviate(input_list):
    output_list = []
    for item in input_list:
        unabbreviated = item[0].replace('STD', 'Standard').replace('_BRD', ' Branding').replace('_LDS', ' Leads').replace('_RTG', ' Rating').replace('_DRS', ' Direct Response').replace('_NRT', ' Non-Retargeting').replace('_NOR', ' Normal')
        output_list.append(unabbreviated)
    return output_list

input_list = [['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'], ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'], ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK']]
print(unabbreviate(input_list))
