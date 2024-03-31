# Start time: 2024-03-30 03:20:17.152068
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response), and given input as ['Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'] output is Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK, given input as ['MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK'] output is MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK, given input as ['Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK'] output is Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: after "STD", unabbreviate the first phrase enclosed by a pair of "_" (BRD unabbreviated is Branding, LDS unabbreviated is Leads, DRS unabbreviated is Direct Response)
# Input: 'Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK'
# Output: 'Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK'

def unabbreviate_string(input_str):
    try:
        # Split the input string by "STD"
        parts = input_str.split("STD")
        
        # Check if there are two parts after splitting
        if len(parts) == 2:
            # Find the first phrase enclosed by a pair of "_"
            start_idx = parts[1].find("_") + 1
            end_idx = parts[1].find("_", start_idx)
            phrase_to_unabbreviate = parts[1][start_idx:end_idx]
            
            # Unabbreviate the phrase
            unabbreviated_phrase = ""
            if phrase_to_unabbreviate == "BRD":
                unabbreviated_phrase = "Branding"
            elif phrase_to_unabbreviate == "LDS":
                unabbreviated_phrase = "Leads"
            elif phrase_to_unabbreviate == "DRS":
                unabbreviated_phrase = "Direct Response"
            
            # Construct the output string
            output_str = parts[0] + "STD " + unabbreviated_phrase + parts[1][end_idx:]
            return output_str
        else:
            return "Invalid input format"
    except Exception as e:
        return str(e)

# Test cases
print(unabbreviate_string('Adf_ROCLeader_BAN_728x90_CPM_STD _BRD _NRT_DCK')) # Output: Adf_ROCLeader_BAN_728x90_CPM_STD _Branding _NRT_DCK
print(unabbreviate_string('MMC_ContextualLarRec_BAN_336x280_CPM_STD _LDS _RTG_DCK')) # Output: MMC_ContextualLarRec_BAN_336x280_CPM_STD _Leads _RTG_DCK
print(unabbreviate_string('Adf_ROC_DLBD_728x90_CPM_STD_DRS_NRT_NOR_DCK')) # Output: Adf_ROC_DLBD_728x90_CPM_STD_Direct Response_NRT_NOR_DCK

# End time: 2024-03-30 03:20:24.545466
# Elapsed time in seconds: 7.393189363998317