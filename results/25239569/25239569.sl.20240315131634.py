def unabbreviate_expression(input_list):
    output_list = []
    for item in input_list:
        unabbreviated_item = item[0].replace('STD', 'Standard').replace('_BRD', ' Branding').replace('_LDS', ' Leads').replace('_DRS', ' Direct Response')
        output_list.append(unabbreviated_item)
    return output_list

input_list = [['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'], ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'], ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK']]
print(unabbreviate_expression(input_list))
