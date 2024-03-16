def return_first_three_numbers(input_list):
    output = []
    for sublist in input_list:
        output.append(sublist[0][:3])
    return output

# Test the function with the provided input
input_list = [['938-242-504'], ['938-242-504'], ['938-242-504'], ['308-916-545'], ['308-916-545'], ['308-916-545'], ['623-599-749'], ['623-599-749'], ['623-599-749'], ['981-424-843'], ['981-424-843'], ['981-424-843'], ['118-980-214'], ['118-980-214'], ['118-980-214'], ['244-655-094'], ['244-655-094'], ['244-655-094'], ['830-941-991'], ['830-941-991'], ['830-941-991'], ['911-186-562'], ['911-186-562'], ['911-186-562'], ['002-500-200'], ['002-500-200'], ['002-500-200'], ['113-860-034'], ['113-860-034'], ['113-860-034'], ['457-622-959'], ['457-622-959'], ['457-622-959'], ['986-722-311'], ['986-722-311'], ['986-722-311'], ['110-170-771'], ['110-170-771'], ['110-170-771'], ['469-610-118'], ['469-610-118'], ['469-610-118'], ['817-925-247'], ['817-925-247'], ['817-925-247'], ['256-899-439'], ['256-899-439'], ['256-899-439'], ['886-911-726'], ['886-911-726'], ['886-911-726'], ['562-950-358'], ['562-950-358'], ['562-950-358'], ['693-049-588'], ['693-049-588'], ['693-049-588'], ['840-503-234'], ['840-503-234'], ['840-503-234'], ['698-815-340'], ['698-815-340'], ['698-815-340'], ['498-808-434'], ['498-808-434'], ['498-808-434'], ['329-545-000'], ['329-545-000'], ['329-545-000'], ['380-281-597'], ['380-281-597'], ['380-281-597'], ['332-395-493'], ['332-395-493'], ['332-395-493'], ['251-903-028'], ['251-903-028'], ['251-903-028'], ['176-090-894'], ['176-090-894'], ['176-090-894'], ['336-611-100'], ['336-611-100'], ['336-611-100'], ['416-390-647'], ['416-390-647'], ['416-390-647'], ['019-430-596'], ['019-430-596'], ['019-430-596'], ['960-659-771'], ['960-659-771'], ['960-659-771'], ['475-505-007'], ['475-505-007'], ['475-505-007'], ['424-069-886'], ['424-069-886'], ['424-069-886'], ['941-102-117'], ['941-102-117'], ['941-102-117'], ['331-728-008'], ['331-728-008'], ['331-728-008'], ['487-726-198'], ['487-726-198'], ['487-726-198'], ['612-419-942'], ['612-419-942'], ['612-419-942'], ['594-741-346'], ['594-741-346'], ['594-741-346'], ['320-984-742'], ['320-984-742'], ['320-984-742'], ['060-919-361'], ['060-919-361'], ['060-919-361'], ['275-536-998'], ['275-536-998'], ['275-536-998'], ['548-835-065'], ['548-835-065'], ['548-835-065'], ['197-485-507'], ['197-485-507'], ['197-485-507'], ['455-776-949'], ['455-776-949'], ['455-776-949'], ['085-421-340'], ['085-421-340'], ['085-421-340'], ['785-713-099'], ['785-713-099'], ['785-713-099'], ['426-712-861'], ['426-712-861'], ['426-712-861'], ['386-994-906'], ['386-994-906'], ['386-994-906'], ['918-304-840'], ['918-304-840'], ['918-304-840'], ['247-153-598'], ['247-153-598'], ['247-153-598'], ['075-497-069'], ['075-497-069'], ['075-497-069'], ['140-726-583'], ['140-726-583'], ['140-726-583'], ['049-413-248'], ['049-413-248'], ['049-413-248'], ['977-386-462'], ['977-386-462'], ['977-386-462'], ['058-272-455'], ['058-272-455'], ['058-272-455'], ['428-629-927'], ['428-629-927'], ['428-629-927'], ['449-122-191'], ['449-122-191'], ['449-122-191'], ['568-759-670'], ['568-759-670'], ['568-759-670'], ['312-846-053'], ['312-846-053'], ['312-846-053'], ['943-037-297'], ['943-037-297'], ['943-037-297'], ['014-270-177'], ['014-270-177'], ['014-270-177'], ['658-877-878'], ['658-877-878'], ['658-877-878'], ['888-594-038'], ['888-594-038'], ['888-594-038'], ['232-253-254'], ['232-253-254'], ['232-253-254'], ['308-722-292'], ['308-722-292'], ['308-722-292'], ['342-145-742'], ['342-145-742'], ['342-145-742'], ['568-181-515'], ['568-181-515'], ['568-181-515'], ['300-140-756'], ['300-140-756'], ['300-140-756'], ['099-684-216'], ['099-684-216'], ['099-684-216'], ['575-296-621'], ['575-296-621'], ['575-296-621'], ['994-443-794'], ['994-443-794'], ['994-443-794'], ['400-334-692'], ['400-334-692'], ['400-334-692'], ['684-711-883'], ['684-711-883'], ['684-711-883'], ['539-636-358'], ['539-636-358'], ['539-636-358'], ['009-878-919'], ['009-878-919'], ['009-878-919'], ['919-545-701'], ['919-545-701'], ['919-545-701'], ['546-399-239'], ['546-399-239'], ['546-399-239'], ['993-608-757'], ['993-608-757'], ['993-608-757'], ['107-652-845'], ['107-652-845'], ['107-652-845'], ['206-805-793'], ['206-805-793'], ['206-805-793'], ['198-857-684'], ['198-857-684'], ['198-857-684'], ['912-827-430'], ['912-827-430'], ['912-827-430'], ['560-951-766'], ['560-951-766'], ['560-951-766'], ['142-178-290'], ['142-178-290'], ['142-178-290'], ['732-196-946'], ['732-196-946'], ['732-196-946'], ['963-875-745'], ['963-875-745'], ['963-875-745'], ['881-865-867'], ['881-865-867'], ['881-865-867'], ['234-686-715'], ['234-686-715'], ['234-686-715'], ['720-330-583'], ['720-330-583'], ['720-330-583'], ['593-065-126'], ['593-065-126'], ['593-065-126'], ['671-778-064'], ['671-778-064'], ['671-778-064'], ['252-029-036'], ['252-029-036'], ['252-029-036'], ['700-322-036'], ['700-322-036'], ['700-322-036'], ['882-587-473'], ['882-587-473'], ['882-587-473'], ['964-134-953'], ['964-134-953'], ['964-134-953'], ['038-300-876'], ['038-300-876'], ['038-300-876'], ['158-894-947'], ['158-894-947'], ['158-894-947'], ['757-454-374'], ['757-454-374'], ['757-454-374'], ['872-513-190'], ['872-513-190'], ['872-513-190'], ['566-086-726'], ['566-086-726'], ['566-086-726'], ['938-242-504'], ['308-916-545'], ['623-599-749'], ['981-424-843'], ['118-980-214'], ['244-655-094'], ['830-941-991'], ['911-186-562'], ['002-500-200'], ['113-860-034'], ['457-622-959'], ['986-722-311'], ['110-170-771'], ['469-610-118'], ['817-925-247'], ['256-899-439'], ['886-911-726'], ['562-950-358'], ['693-049-588'], ['840-503-234'], ['698-815-340'], ['498-808-434'], ['329-545-000'], ['380-281-597'], ['332-395-493'], ['251-903-028'], ['176-090-894'], ['336-611-100'], ['416-390-647'], ['019-430-596'], ['960-659-771'], ['475-505-007'], ['424-069-886'], ['941-102-117'], ['331-728-008'], ['487-726-198'], ['612-419-942'], ['594-741-346'], ['320-984-742'], ['060-919-361'], ['275-536-998'], ['548-835-065'], ['197-485-507'], ['455-776-949'], ['085-421-340'], ['785-713-099'], ['426-712-861'], ['386-994-906'], ['918-304-840'], ['247-153-598'], ['075-497-069'], ['140-726-583'], ['049-413-248'], ['977-386-462'], ['058-272-455'], ['428-629-927'], ['449-122-191'], ['568-759-670'], ['312-846-053'], ['943-037-297'], ['014-270-177'], ['658-877-878'], ['888-594-038'], ['232-253-254'], ['308-722-292'], ['342-145-742'], ['568-181-515'], ['300-140-756'], ['099-684-216'], ['575-296-621'], ['994-443-794'], ['400-334-692'], ['684-711-883'], ['539-636-358'], ['009-878-919'], ['919-545-701'], ['546-399-239'], ['993-608-757'], ['107-652-845'], ['206-805-793'], ['198-857-684'], ['912-827-430'], ['560-951-766'], ['142-178-290'], ['732-196-946'], ['963-875-745'], ['881-865-867'], ['234-686-715'], ['720-330-583'], ['593-065-126'], ['671-778-064'], ['252-029-036'], ['700-322-036'], ['882-587-473'], ['964-134-953'], ['038-300-876'], ['158-894-947'], ['757-454-374'], ['872-513-190'], ['566-086-726']]
print(return_first_three_numbers(input_list))
