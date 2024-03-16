def unabbreviate(input_list):
    output_list = []
    for item in input_list:
        unabbreviated = item[0].replace('_STD ', '_Standard ')
        unabbreviated = unabbreviated.replace('_BRD ', '_Branding ')
        unabbreviated = unabbreviated.replace('_NRT ', '_NRT ')
        unabbreviated = unabbreviated.replace('_DCK', '_DCK')
        unabbreviated = unabbreviated.replace('_LDS ', '_Leads ')
        unabbreviated = unabbreviated.replace('_RTG ', '_RTG ')
        unabbreviated = unabbreviated.replace('_DRS ', '_Direct Response ')
        unabbreviated = unabbreviated.replace('_NOR ', '_NOR ')
        output_list.append(unabbreviated)
    return output_list

input_list = [['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'], ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'], ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK']]
output = unabbreviate(input_list)
print(output)
