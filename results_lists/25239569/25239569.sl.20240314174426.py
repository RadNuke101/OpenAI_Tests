def unabbreviate(input_list):
    output_list = []
    for item in input_list:
        unabbreviated_item = item[0].replace('_STD', '_Standard')
        unabbreviated_item = unabbreviated_item.replace('_BRD', '_Branding')
        unabbreviated_item = unabbreviated_item.replace('_LDS', '_Leads')
        unabbreviated_item = unabbreviated_item.replace('_RTG', '_Retargeting')
        unabbreviated_item = unabbreviated_item.replace('_DRS', '_Direct Response')
        unabbreviated_item = unabbreviated_item.replace('_NRT', '_NRT')
        unabbreviated_item = unabbreviated_item.replace('_NOR', '_NOR')
        output_list.append(unabbreviated_item)
    return output_list

input_list = [['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'], ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'], ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK']]
print(unabbreviate(input_list))
