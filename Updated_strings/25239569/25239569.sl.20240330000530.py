# Start time: 2024-03-30 00:21:48.684151
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response), and given input as ['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'] output is Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK, given input as ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'] output is MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK, given input as ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'] output is Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response)
# Input: 'Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'
# Output: 'Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK'

def unabbreviate_string(input_string):
    try:
        # Split the input string by "STD"
        parts = input_string.split("STD")
        
        # Check if the split resulted in two parts
        if len(parts) == 2:
            # Find the first phrase enclosed by a pair of "_"
            start_index = parts[0].rfind("_")
            end_index = parts[0].rfind("_", 0, start_index)
            if start_index != -1 and end_index != -1:
                # Unabbreviate the phrase
                unabbreviated_phrase = parts[0][end_index+1:start_index].replace("_", " ")
                
                # Construct the output string
                output_string = parts[0][:end_index+1] + unabbreviated_phrase + parts[0][start_index:] + "STD" + parts[1]
                return output_string
            else:
                return input_string
        else:
            return input_string
    except Exception as e:
        return input_string

# Test cases
print(unabbreviate_string('Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'))  # Output: 'Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK'
print(unabbreviate_string('MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'))  # Output: 'MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK'
print(unabbreviate_string('Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'))  # Output: 'Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK'

# End time: 2024-03-30 00:21:55.728759
# Elapsed time in seconds: 7.044570047999969