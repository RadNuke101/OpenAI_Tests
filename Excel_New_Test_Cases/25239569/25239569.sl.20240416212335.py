# Start time: 2024-04-16 21:34:44.891344

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response), and input as: "Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK" output is: Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK, input as: "MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK" output is: MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK, input as: "Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK" output is: Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

def generated_function(input_str):
    # Split the input string by "_"
    input_list = input_str.split("_")
    
    # Find the index of "STD" in the input list
    std_index = input_list.index("STD")
    
    # Unabbreviate the phrase after "STD" and enclosed by "_"
    for i in range(std_index+1, len(input_list)):
        if input_list[i][0] == "_":
            input_list[i] = input_list[i].replace("_", "")  # Remove the "_" at the beginning
            input_list[i] = input_list[i].replace(input_list[i], input_list[i].capitalize())  # Capitalize the phrase
            break
    
    # Join the input list back into a string
    output_str = "_".join(input_list)
    
    return output_str

# Test cases
print(generated_function("Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK"))
print(generated_function("MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK"))
print(generated_function("Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK"))



print(generated_function("MMC_ContextualLarRec_BAN_1440x960_CPM_STD _LDS _RTG"))  ### Output: "MMC_ContextualLarRec_BAN_1440x960_CPM_STD _LDS _RTG"
print(generated_function("Adf_BC_DL_728x90_CPM_STD_DRS_NRT_NOR"))  ### Output: "Adf_BC_DL_728x90_CPM_STD_DRS_NRT_NOR"
print(generated_function("Adf_ROCLeader_BAN_728x90_CPM _BRD _NRT"))  ### Output: "Adf_ROCLeader_BAN_728x90_CPM _BRD _NRT"


print(generated_function("Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK"))  ## Output: Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK
print(generated_function("MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK"))  ## Output: MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK
print(generated_function("Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK"))  ## Output: Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK



# End time: 2024-04-16 21:34:48.733973
# Elapsed time in seconds: 3.8425473259999308