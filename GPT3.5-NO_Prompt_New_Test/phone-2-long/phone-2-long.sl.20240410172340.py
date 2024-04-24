# Start time: 2024-04-10 17:32:41.405590

'''
Prompt:
Given that input as ['938-242-504'] output is 504, input as ['308-916-545'] output is 545, input as ['623-599-749'] output is 749, input as ['981-424-843'] output is 843, input as ['118-980-214'] output is 214, input as ['244-655-094'] output is 094, input as ['830-941-991'] output is 991, input as ['911-186-562'] output is 562, input as ['002-500-200'] output is 200, input as ['113-860-034'] output is 034, input as ['457-622-959'] output is 959, input as ['986-722-311'] output is 311, input as ['110-170-771'] output is 771, input as ['469-610-118'] output is 118, input as ['817-925-247'] output is 247, input as ['256-899-439'] output is 439, input as ['886-911-726'] output is 726, input as ['562-950-358'] output is 358, input as ['693-049-588'] output is 588, input as ['840-503-234'] output is 234, input as ['698-815-340'] output is 340, input as ['498-808-434'] output is 434, input as ['329-545-000'] output is 000, input as ['380-281-597'] output is 597, input as ['332-395-493'] output is 493, input as ['251-903-028'] output is 028, input as ['176-090-894'] output is 894, input as ['336-611-100'] output is 100, input as ['416-390-647'] output is 647, input as ['019-430-596'] output is 596, input as ['960-659-771'] output is 771, input as ['475-505-007'] output is 007, input as ['424-069-886'] output is 886, input as ['941-102-117'] output is 117, input as ['331-728-008'] output is 008, input as ['487-726-198'] output is 198, input as ['612-419-942'] output is 942, input as ['594-741-346'] output is 346, input as ['320-984-742'] output is 742, input as ['060-919-361'] output is 361, input as ['275-536-998'] output is 998, input as ['548-835-065'] output is 065, input as ['197-485-507'] output is 507, input as ['455-776-949'] output is 949, input as ['085-421-340'] output is 340, input as ['785-713-099'] output is 099, input as ['426-712-861'] output is 861, input as ['386-994-906'] output is 906, input as ['918-304-840'] output is 840, input as ['247-153-598'] output is 598, input as ['075-497-069'] output is 069, input as ['140-726-583'] output is 583, input as ['049-413-248'] output is 248, input as ['977-386-462'] output is 462, input as ['058-272-455'] output is 455, input as ['428-629-927'] output is 927, input as ['449-122-191'] output is 191, input as ['568-759-670'] output is 670, input as ['312-846-053'] output is 053, input as ['943-037-297'] output is 297, input as ['014-270-177'] output is 177, input as ['658-877-878'] output is 878, input as ['888-594-038'] output is 038, input as ['232-253-254'] output is 254, input as ['308-722-292'] output is 292, input as ['342-145-742'] output is 742, input as ['568-181-515'] output is 515, input as ['300-140-756'] output is 756, input as ['099-684-216'] output is 216, input as ['575-296-621'] output is 621, input as ['994-443-794'] output is 794, input as ['400-334-692'] output is 692, input as ['684-711-883'] output is 883, input as ['539-636-358'] output is 358, input as ['009-878-919'] output is 919, input as ['919-545-701'] output is 701, input as ['546-399-239'] output is 239, input as ['993-608-757'] output is 757, input as ['107-652-845'] output is 845, input as ['206-805-793'] output is 793, input as ['198-857-684'] output is 684, input as ['912-827-430'] output is 430, input as ['560-951-766'] output is 766, input as ['142-178-290'] output is 290, input as ['732-196-946'] output is 946, input as ['963-875-745'] output is 745, input as ['881-865-867'] output is 867, input as ['234-686-715'] output is 715, input as ['720-330-583'] output is 583, input as ['593-065-126'] output is 126, input as ['671-778-064'] output is 064, input as ['252-029-036'] output is 036, input as ['700-322-036'] output is 036, input as ['882-587-473'] output is 473, input as ['964-134-953'] output is 953, input as ['038-300-876'] output is 876, input as ['158-894-947'] output is 947, input as ['757-454-374'] output is 374, input as ['872-513-190'] output is 190, input as ['566-086-726'] output is 726, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Extract the last part of the input string after the last hyphen
        output = input_str.split('-')[-1]
        return output
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('938-242-504'))  # Output: 504
print(generated_function('308-916-545'))  # Output: 545
print(generated_function('623-599-749'))  # Output: 749
# Add more test cases if needed
print(generated_function("938-242-504"))  ## Output: 504
print(generated_function("308-916-545"))  ## Output: 545
print(generated_function("623-599-749"))  ## Output: 749
print(generated_function("981-424-843"))  ## Output: 843
print(generated_function("118-980-214"))  ## Output: 214
print(generated_function("244-655-094"))  ## Output: 094
print(generated_function("830-941-991"))  ## Output: 991
print(generated_function("911-186-562"))  ## Output: 562
print(generated_function("002-500-200"))  ## Output: 200
print(generated_function("113-860-034"))  ## Output: 034
print(generated_function("457-622-959"))  ## Output: 959
print(generated_function("986-722-311"))  ## Output: 311
print(generated_function("110-170-771"))  ## Output: 771
print(generated_function("469-610-118"))  ## Output: 118
print(generated_function("817-925-247"))  ## Output: 247
print(generated_function("256-899-439"))  ## Output: 439
print(generated_function("886-911-726"))  ## Output: 726
print(generated_function("562-950-358"))  ## Output: 358
print(generated_function("693-049-588"))  ## Output: 588
print(generated_function("840-503-234"))  ## Output: 234
print(generated_function("698-815-340"))  ## Output: 340
print(generated_function("498-808-434"))  ## Output: 434
print(generated_function("329-545-000"))  ## Output: 000
print(generated_function("380-281-597"))  ## Output: 597
print(generated_function("332-395-493"))  ## Output: 493
print(generated_function("251-903-028"))  ## Output: 028
print(generated_function("176-090-894"))  ## Output: 894
print(generated_function("336-611-100"))  ## Output: 100
print(generated_function("416-390-647"))  ## Output: 647
print(generated_function("019-430-596"))  ## Output: 596
print(generated_function("960-659-771"))  ## Output: 771
print(generated_function("475-505-007"))  ## Output: 007
print(generated_function("424-069-886"))  ## Output: 886
print(generated_function("941-102-117"))  ## Output: 117
print(generated_function("331-728-008"))  ## Output: 008
print(generated_function("487-726-198"))  ## Output: 198
print(generated_function("612-419-942"))  ## Output: 942
print(generated_function("594-741-346"))  ## Output: 346
print(generated_function("320-984-742"))  ## Output: 742
print(generated_function("060-919-361"))  ## Output: 361
print(generated_function("275-536-998"))  ## Output: 998
print(generated_function("548-835-065"))  ## Output: 065
print(generated_function("197-485-507"))  ## Output: 507
print(generated_function("455-776-949"))  ## Output: 949
print(generated_function("085-421-340"))  ## Output: 340
print(generated_function("785-713-099"))  ## Output: 099
print(generated_function("426-712-861"))  ## Output: 861
print(generated_function("386-994-906"))  ## Output: 906
print(generated_function("918-304-840"))  ## Output: 840
print(generated_function("247-153-598"))  ## Output: 598
print(generated_function("075-497-069"))  ## Output: 069
print(generated_function("140-726-583"))  ## Output: 583
print(generated_function("049-413-248"))  ## Output: 248
print(generated_function("977-386-462"))  ## Output: 462
print(generated_function("058-272-455"))  ## Output: 455
print(generated_function("428-629-927"))  ## Output: 927
print(generated_function("449-122-191"))  ## Output: 191
print(generated_function("568-759-670"))  ## Output: 670
print(generated_function("312-846-053"))  ## Output: 053
print(generated_function("943-037-297"))  ## Output: 297
print(generated_function("014-270-177"))  ## Output: 177
print(generated_function("658-877-878"))  ## Output: 878
print(generated_function("888-594-038"))  ## Output: 038
print(generated_function("232-253-254"))  ## Output: 254
print(generated_function("308-722-292"))  ## Output: 292
print(generated_function("342-145-742"))  ## Output: 742
print(generated_function("568-181-515"))  ## Output: 515
print(generated_function("300-140-756"))  ## Output: 756
print(generated_function("099-684-216"))  ## Output: 216
print(generated_function("575-296-621"))  ## Output: 621
print(generated_function("994-443-794"))  ## Output: 794
print(generated_function("400-334-692"))  ## Output: 692
print(generated_function("684-711-883"))  ## Output: 883
print(generated_function("539-636-358"))  ## Output: 358
print(generated_function("009-878-919"))  ## Output: 919
print(generated_function("919-545-701"))  ## Output: 701
print(generated_function("546-399-239"))  ## Output: 239
print(generated_function("993-608-757"))  ## Output: 757
print(generated_function("107-652-845"))  ## Output: 845
print(generated_function("206-805-793"))  ## Output: 793
print(generated_function("198-857-684"))  ## Output: 684
print(generated_function("912-827-430"))  ## Output: 430
print(generated_function("560-951-766"))  ## Output: 766
print(generated_function("142-178-290"))  ## Output: 290
print(generated_function("732-196-946"))  ## Output: 946
print(generated_function("963-875-745"))  ## Output: 745
print(generated_function("881-865-867"))  ## Output: 867
print(generated_function("234-686-715"))  ## Output: 715
print(generated_function("720-330-583"))  ## Output: 583
print(generated_function("593-065-126"))  ## Output: 126
print(generated_function("671-778-064"))  ## Output: 064
print(generated_function("252-029-036"))  ## Output: 036
print(generated_function("700-322-036"))  ## Output: 036
print(generated_function("882-587-473"))  ## Output: 473
print(generated_function("964-134-953"))  ## Output: 953
print(generated_function("038-300-876"))  ## Output: 876
print(generated_function("158-894-947"))  ## Output: 947
print(generated_function("757-454-374"))  ## Output: 374
print(generated_function("872-513-190"))  ## Output: 190
print(generated_function("566-086-726"))  ## Output: 726

# End time: 2024-04-10 17:32:43.775587
# Elapsed time in seconds: 2.369969633999972


# APPEND TEST SCRIPTS...
print(generated_function("938-242-504"))  ## Output: 504
print(generated_function("308-916-545"))  ## Output: 545
print(generated_function("623-599-749"))  ## Output: 749
print(generated_function("981-424-843"))  ## Output: 843
print(generated_function("118-980-214"))  ## Output: 214
print(generated_function("244-655-094"))  ## Output: 094
print(generated_function("830-941-991"))  ## Output: 991
print(generated_function("911-186-562"))  ## Output: 562
print(generated_function("002-500-200"))  ## Output: 200
print(generated_function("113-860-034"))  ## Output: 034
print(generated_function("457-622-959"))  ## Output: 959
print(generated_function("986-722-311"))  ## Output: 311
print(generated_function("110-170-771"))  ## Output: 771
print(generated_function("469-610-118"))  ## Output: 118
print(generated_function("817-925-247"))  ## Output: 247
print(generated_function("256-899-439"))  ## Output: 439
print(generated_function("886-911-726"))  ## Output: 726
print(generated_function("562-950-358"))  ## Output: 358
print(generated_function("693-049-588"))  ## Output: 588
print(generated_function("840-503-234"))  ## Output: 234
print(generated_function("698-815-340"))  ## Output: 340
print(generated_function("498-808-434"))  ## Output: 434
print(generated_function("329-545-000"))  ## Output: 000
print(generated_function("380-281-597"))  ## Output: 597
print(generated_function("332-395-493"))  ## Output: 493
print(generated_function("251-903-028"))  ## Output: 028
print(generated_function("176-090-894"))  ## Output: 894
print(generated_function("336-611-100"))  ## Output: 100
print(generated_function("416-390-647"))  ## Output: 647
print(generated_function("019-430-596"))  ## Output: 596
print(generated_function("960-659-771"))  ## Output: 771
print(generated_function("475-505-007"))  ## Output: 007
print(generated_function("424-069-886"))  ## Output: 886
print(generated_function("941-102-117"))  ## Output: 117
print(generated_function("331-728-008"))  ## Output: 008
print(generated_function("487-726-198"))  ## Output: 198
print(generated_function("612-419-942"))  ## Output: 942
print(generated_function("594-741-346"))  ## Output: 346
print(generated_function("320-984-742"))  ## Output: 742
print(generated_function("060-919-361"))  ## Output: 361
print(generated_function("275-536-998"))  ## Output: 998
print(generated_function("548-835-065"))  ## Output: 065
print(generated_function("197-485-507"))  ## Output: 507
print(generated_function("455-776-949"))  ## Output: 949
print(generated_function("085-421-340"))  ## Output: 340
print(generated_function("785-713-099"))  ## Output: 099
print(generated_function("426-712-861"))  ## Output: 861
print(generated_function("386-994-906"))  ## Output: 906
print(generated_function("918-304-840"))  ## Output: 840
print(generated_function("247-153-598"))  ## Output: 598
print(generated_function("075-497-069"))  ## Output: 069
print(generated_function("140-726-583"))  ## Output: 583
print(generated_function("049-413-248"))  ## Output: 248
print(generated_function("977-386-462"))  ## Output: 462
print(generated_function("058-272-455"))  ## Output: 455
print(generated_function("428-629-927"))  ## Output: 927
print(generated_function("449-122-191"))  ## Output: 191
print(generated_function("568-759-670"))  ## Output: 670
print(generated_function("312-846-053"))  ## Output: 053
print(generated_function("943-037-297"))  ## Output: 297
print(generated_function("014-270-177"))  ## Output: 177
print(generated_function("658-877-878"))  ## Output: 878
print(generated_function("888-594-038"))  ## Output: 038
print(generated_function("232-253-254"))  ## Output: 254
print(generated_function("308-722-292"))  ## Output: 292
print(generated_function("342-145-742"))  ## Output: 742
print(generated_function("568-181-515"))  ## Output: 515
print(generated_function("300-140-756"))  ## Output: 756
print(generated_function("099-684-216"))  ## Output: 216
print(generated_function("575-296-621"))  ## Output: 621
print(generated_function("994-443-794"))  ## Output: 794
print(generated_function("400-334-692"))  ## Output: 692
print(generated_function("684-711-883"))  ## Output: 883
print(generated_function("539-636-358"))  ## Output: 358
print(generated_function("009-878-919"))  ## Output: 919
print(generated_function("919-545-701"))  ## Output: 701
print(generated_function("546-399-239"))  ## Output: 239
print(generated_function("993-608-757"))  ## Output: 757
print(generated_function("107-652-845"))  ## Output: 845
print(generated_function("206-805-793"))  ## Output: 793
print(generated_function("198-857-684"))  ## Output: 684
print(generated_function("912-827-430"))  ## Output: 430
print(generated_function("560-951-766"))  ## Output: 766
print(generated_function("142-178-290"))  ## Output: 290
print(generated_function("732-196-946"))  ## Output: 946
print(generated_function("963-875-745"))  ## Output: 745
print(generated_function("881-865-867"))  ## Output: 867
print(generated_function("234-686-715"))  ## Output: 715
print(generated_function("720-330-583"))  ## Output: 583
print(generated_function("593-065-126"))  ## Output: 126
print(generated_function("671-778-064"))  ## Output: 064
print(generated_function("252-029-036"))  ## Output: 036
print(generated_function("700-322-036"))  ## Output: 036
print(generated_function("882-587-473"))  ## Output: 473
print(generated_function("964-134-953"))  ## Output: 953
print(generated_function("038-300-876"))  ## Output: 876
print(generated_function("158-894-947"))  ## Output: 947
print(generated_function("757-454-374"))  ## Output: 374
print(generated_function("872-513-190"))  ## Output: 190
print(generated_function("566-086-726"))  ## Output: 726


print(generated_function("118-980-567"))  ### Output: 567
print(generated_function("981-424-456"))  ### Output: 456
print(generated_function("938-242-123"))  ### Output: 123
print(generated_function("623-599-345"))  ### Output: 345
print(generated_function("244-655-678"))  ### Output: 678
print(generated_function("308-916-234"))  ### Output: 234

# TEST SCRIPTS APPENDED!

