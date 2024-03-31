# Start time: 2024-03-30 21:03:03.108877

# Content: Given that given input as ['938-242-504'] output is 242, given input as ['308-916-545'] output is 916, given input as ['623-599-749'] output is 599, given input as ['981-424-843'] output is 424, given input as ['118-980-214'] output is 980, given input as ['244-655-094'] output is 655, given input as ['830-941-991'] output is 941, given input as ['911-186-562'] output is 186, given input as ['002-500-200'] output is 500, given input as ['113-860-034'] output is 860, given input as ['457-622-959'] output is 622, given input as ['986-722-311'] output is 722, given input as ['110-170-771'] output is 170, given input as ['469-610-118'] output is 610, given input as ['817-925-247'] output is 925, given input as ['256-899-439'] output is 899, given input as ['886-911-726'] output is 911, given input as ['562-950-358'] output is 950, given input as ['693-049-588'] output is 049, given input as ['840-503-234'] output is 503, given input as ['698-815-340'] output is 815, given input as ['498-808-434'] output is 808, given input as ['329-545-000'] output is 545, given input as ['380-281-597'] output is 281, given input as ['332-395-493'] output is 395, given input as ['251-903-028'] output is 903, given input as ['176-090-894'] output is 090, given input as ['336-611-100'] output is 611, given input as ['416-390-647'] output is 390, given input as ['019-430-596'] output is 430, given input as ['960-659-771'] output is 659, given input as ['475-505-007'] output is 505, given input as ['424-069-886'] output is 069, given input as ['941-102-117'] output is 102, given input as ['331-728-008'] output is 728, given input as ['487-726-198'] output is 726, given input as ['612-419-942'] output is 419, given input as ['594-741-346'] output is 741, given input as ['320-984-742'] output is 984, given input as ['060-919-361'] output is 919, given input as ['275-536-998'] output is 536, given input as ['548-835-065'] output is 835, given input as ['197-485-507'] output is 485, given input as ['455-776-949'] output is 776, given input as ['085-421-340'] output is 421, given input as ['785-713-099'] output is 713, given input as ['426-712-861'] output is 712, given input as ['386-994-906'] output is 994, given input as ['918-304-840'] output is 304, given input as ['247-153-598'] output is 153, given input as ['075-497-069'] output is 497, given input as ['140-726-583'] output is 726, given input as ['049-413-248'] output is 413, given input as ['977-386-462'] output is 386, given input as ['058-272-455'] output is 272, given input as ['428-629-927'] output is 629, given input as ['449-122-191'] output is 122, given input as ['568-759-670'] output is 759, given input as ['312-846-053'] output is 846, given input as ['943-037-297'] output is 037, given input as ['014-270-177'] output is 270, given input as ['658-877-878'] output is 877, given input as ['888-594-038'] output is 594, given input as ['232-253-254'] output is 253, given input as ['308-722-292'] output is 722, given input as ['342-145-742'] output is 145, given input as ['568-181-515'] output is 181, given input as ['300-140-756'] output is 140, given input as ['099-684-216'] output is 684, given input as ['575-296-621'] output is 296, given input as ['994-443-794'] output is 443, given input as ['400-334-692'] output is 334, given input as ['684-711-883'] output is 711, given input as ['539-636-358'] output is 636, given input as ['009-878-919'] output is 878, given input as ['919-545-701'] output is 545, given input as ['546-399-239'] output is 399, given input as ['993-608-757'] output is 608, given input as ['107-652-845'] output is 652, given input as ['206-805-793'] output is 805, given input as ['198-857-684'] output is 857, given input as ['912-827-430'] output is 827, given input as ['560-951-766'] output is 951, given input as ['142-178-290'] output is 178, given input as ['732-196-946'] output is 196, given input as ['963-875-745'] output is 875, given input as ['881-865-867'] output is 865, given input as ['234-686-715'] output is 686, given input as ['720-330-583'] output is 330, given input as ['593-065-126'] output is 065, given input as ['671-778-064'] output is 778, given input as ['252-029-036'] output is 029, given input as ['700-322-036'] output is 322, given input as ['882-587-473'] output is 587, given input as ['964-134-953'] output is 134, given input as ['038-300-876'] output is 300, given input as ['158-894-947'] output is 894, given input as ['757-454-374'] output is 454, given input as ['872-513-190'] output is 513, given input as ['566-086-726'] output is 086, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_middle_number(phone_number):
    try:
        number = phone_number.split('-')
        return int(number[1])
    except (IndexError, ValueError):
        return None

# Test cases
'''
print(extract_middle_number('938-242-504'))  # Output: 242
print(extract_middle_number('308-916-545'))  # Output: 916
print(extract_middle_number('623-599-749'))  # Output: 599
print(extract_middle_number('981-424-843'))  # Output: 424
print(extract_middle_number('118-980-214'))  # Output: 980
print(extract_middle_number('244-655-094'))  # Output: 655
print(extract_middle_number('830-941-991'))  # Output: 941
print(extract_middle_number('911-186-562'))  # Output: 186
print(extract_middle_number('002-500-200'))  # Output: 500
print(extract_middle_number('113-860-034'))  # Output: 860
print(extract_middle_number('457-622-959'))  # Output: 622
print(extract_middle_number('986-722-311'))  # Output: 722
print(extract_middle_number('110-170-771'))  # Output: 170
print(extract_middle_number('469-610-118'))  # Output: 610
print(extract_middle_number('817-925-247'))  # Output: 925
print(extract_middle_number('256-899-439'))  # Output: 899
print(extract_middle_number('886-911-726'))  # Output: 911
print(extract_middle_number('562-950-358'))  # Output: 950
print(extract_middle_number('693-049-588'))  # Output: 049
print(extract_middle_number('840-503-234'))  # Output: 503
print(extract_middle_number('698-815-340'))  # Output: 815
print(extract_middle_number('498-808-434'))  # Output: 808
print(extract_middle_number('329-545-000'))  # Output: 545
print(extract_middle_number('380-281-597'))  # Output: 281
print(extract_middle_number('332-395-493'))  # Output: 395
print(extract_middle_number('251-903-028'))  # Output: 903
print(extract_middle_number('176-090-894'))  # Output: 090
print(extract_middle_number('336-611-100'))  # Output: 611
print(extract_middle_number('416-390-647'))  # Output: 390
print(extract_middle_number('019-430-596'))  # Output: 430
print(extract_middle_number('960-659-771'))  # Output: 659
print(extract_middle_number('475-505-007'))  # Output: 505
print(extract_middle_number('424-069-886'))  # Output: 069
print(extract_middle_number('941-102-117'))  # Output: 102
print(extract_middle_number('331-728-008'))  # Output: 728
print(extract_middle_number('487-726-198'))  # Output: 726
print(extract_middle_number('612-419-942'))  # Output: 419
print(extract_middle_number('594-741-346'))  # Output: 741
print(extract_middle_number('320-984-742'))  # Output: 984
print(extract_middle_number('060-919-361'))  # Output: 919
print(extract_middle_number('275-536-998'))  # Output: 536
print(extract_middle_number('548-835-065'))  # Output: 835
print(extract_middle_number('197-485-507'))  # Output: 485
print(extract_middle_number('455-776-949'))  # Output: 776
print(extract_middle_number('085-421-340'))  # Output: 421
print(extract_middle_number('785-713-099'))  # Output: 713
print(extract_middle_number('426-712-861'))  # Output: 712
print(extract_middle_number('386-994-906'))  # Output: 994
print(extract_middle_number('918-304-840'))  # Output: 304
print(extract_middle_number('247-153-598'))  # Output: 153
print(extract_middle_number('075-497-069'))  # Output: 497
print(extract_middle_number('140-726-583'))  # Output: 726
print(extract_middle_number('049-413-248'))  # Output: 413
print(extract_middle_number('977-386-462'))  # Output: 386
print(extract_middle_number('058-272-455'))  # Output: 272
print(extract_middle_number('428-629-927'))  # Output: 629
print(extract_middle_number('449-122-191'))  # Output: 122
print(extract_middle_number('568-759-670'))  # Output: 759
print(extract_middle_number('312-846-053'))  # Output: 846
print(extract_middle_number('943-037-297'))  # Output: 037
print(extract_middle_number('014-270-177'))  # Output: 270
print(extract_middle_number('658-877-878'))  # Output: 877
print(extract_middle_number('888-594-038'))  # Output: 594
print(extract_middle_number('232-253-254'))  # Output: 253
print(extract_middle_number('308-722-292'))  # Output: 722
print(extract_middle_number('342-145-742'))  # Output: 145
print(extract_middle_number('568-181-515'))  # Output: 181
print(extract_middle_number('300-140-756'))  # Output: 140
print(extract_middle_number('099-684-216'))  # Output: 684
print(extract_middle_number('575-296-621'))  # Output: 296
print(extract_middle_number('994-443-794'))  # Output: 443
print(extract_middle_number('400-334-692'))  # Output: 334
print(extract_middle_number('684-711-883'))  # Output: 711
print(extract_middle_number('539-636-358'))  # Output: 636
print(extract_middle_number('009-878-919'))  # Output: 878
print(extract_middle_number('919-545-701'))  # Output: 545
print(extract_middle_number('546-399-239'))  # Output: 399
print(extract_middle_number('993-608-757'))  # Output: 608
print(extract_middle_number('107-652-845'))  # Output: 652
print(extract_middle_number('206-805-793'))  # Output: 805
print(extract_middle_number('198-857-684'))  # Output: 857
print(extract_middle_number('912-827-430'))  # Output: 827
print(extract_middle_number('560-951-766'))  # Output: 951
print(extract_middle_number('142-178-290'))  # Output: 178
print(extract_middle_number('732-196-946'))  # Output: 196
print(extract_middle_number('963-875-745'))  # Output: 875
print(extract_middle_number('881-865-867'))  # Output: 865
print(extract_middle_number('234-686-715'))  # Output: 686
print(extract_middle_number('720-330-583'))  # Output: 330
print(extract_middle_number('593-065-126'))  # Output: 065
print(extract_middle_number('671-778-064'))  # Output: 778
print(extract_middle_number('252-029-036'))  # Output: 029
print(extract_middle_number('700-322-036'))  # Output: 322
print(extract_middle_number('882-587-473'))  # Output: 587
print(extract_middle_number('964-134-953'))  # Output: 134
print(extract_middle_number('038-300-876'))  # Output: 300
print(extract_middle_number('158-894-947'))  # Output: 894
print(extract_middle_number('757-454-374'))  # Output: 454
print(extract_middle_number('872-513-190'))  # Output: 513
print(extract_middle_number('566-086-726'))  # Output: 086
'''

# End time: 2024-03-30 21:03:49.133083
# Elapsed time in seconds: 46.022987375999946