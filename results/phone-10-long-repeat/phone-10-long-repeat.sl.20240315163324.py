def format_phone_numbers(input_list):
    output_list = []
    for item in input_list:
        phone_number = item[0]
        first_three_nums = phone_number.split('-')[0][:3]
        formatted_number = phone_number.replace('-', ' ', 1)
        formatted_number = formatted_number.replace(first_three_nums, f'({first_three_nums})', 1)
        output_list.append(formatted_number)
    return output_list

input_list = [['+106 769-858-438'], ['+106 769-858-438'], ['+106 769-858-438'], ['+83 973-757-831'], ['+83 973-757-831'], ['+83 973-757-831'], ['+62 647-787-775'], ['+62 647-787-775'], ['+62 647-787-775'], ['+172 027-507-632'], ['+172 027-507-632'], ['+172 027-507-632'], ['+72 001-050-856'], ['+72 001-050-856'], ['+72 001-050-856'], ['+95 310-537-401'], ['+95 310-537-401'], ['+95 310-537-401'], ['+6 775-969-238'], ['+6 775-969-238'], ['+6 775-969-238'], ['+174 594-539-946'], ['+174 594-539-946'], ['+174 594-539-946'], ['+155 927-275-860'], ['+155 927-275-860'], ['+155 927-275-860'], ['+167 405-461-331'], ['+167 405-461-331'], ['+167 405-461-331'], ['+10 538-347-401'], ['+10 538-347-401'], ['+10 538-347-401'], ['+60 971-986-103'], ['+60 971-986-103'], ['+60 971-986-103'], ['+13 258-276-941'], ['+13 258-276-941'], ['+13 258-276-941'], ['+2 604-746-137'], ['+2 604-746-137'], ['+2 604-746-137'], ['+25 998-898-180'], ['+25 998-898-180'], ['+25 998-898-180'], ['+151 862-946-541'], ['+151 862-946-541'], ['+151 862-946-541'], ['+118 165-041-038'], ['+118 165-041-038'], ['+118 165-041-038'], ['+144 170-592-272'], ['+144 170-592-272'], ['+144 170-592-272'], ['+94 462-008-482'], ['+94 462-008-482'], ['+94 462-008-482'], ['+82 685-122-086'], ['+82 685-122-086'], ['+82 685-122-086'], ['+82 675-366-472'], ['+82 675-366-472'], ['+82 675-366-472'], ['+80 066-433-096'], ['+80 066-433-096'], ['+80 066-433-096'], ['+163 039-436-166'], ['+163 039-436-166'], ['+163 039-436-166'], ['+138 808-083-074'], ['+138 808-083-074'], ['+138 808-083-074'], ['+42 643-245-738'], ['+42 643-245-738'], ['+42 643-245-738'], ['+169 822-542-726'], ['+169 822-542-726'], ['+169 822-542-726'], ['+176 767-782-369'], ['+176 767-782-369'], ['+176 767-782-369'], ['+47 414-369-343'], ['+47 414-369-343'], ['+47 414-369-343'], ['+138 885-618-512'], ['+138 885-618-512'], ['+138 885-618-512'], ['+104 158-671-355'], ['+104 158-671-355'], ['+104 158-671-355'], ['+188 280-087-526'], ['+188 280-087-526'], ['+188 280-087-526'], ['+50 268-571-336'], ['+50 268-571-336'], ['+50 268-571-336'], ['+183 225-960-024'], ['+183 225-960-024'], ['+183 225-960-024'], ['+58 191-982-491'], ['+58 191-982-491'], ['+58 191-982-491'], ['+9 507-092-535'], ['+9 507-092-535'], ['+9 507-092-535'], ['+64 061-601-398'], ['+64 061-601-398'], ['+64 061-601-398'], ['+189 831-591-877'], ['+189 831-591-877'], ['+189 831-591-877'], ['+129 425-765-844'], ['+129 425-765-844'], ['+129 425-765-844'], ['+94 856-734-046'], ['+94 856-734-046'], ['+94 856-734-046'], ['+35 082-845-261'], ['+35 082-845-261'], ['+35 082-845-261'], ['+185 394-622-272'], ['+185 394-622-272'], ['+185 394-622-272'], ['+163 905-707-740'], ['+163 905-707-740'], ['+163 905-707-740'], ['+23 448-213-807'], ['+23 448-213-807'], ['+23 448-213-807'], ['+42 634-077-089'], ['+42 634-077-089'], ['+42 634-077-089'], ['+18 051-287-382'], ['+18 051-287-382'], ['+18 051-287-382'], ['+29 773-545-520'], ['+29 773-545-520'], ['+29 773-545-520'], ['+43 249-097-743'], ['+43 249-097-743'], ['+43 249-097-743'], ['+158 674-736-891'], ['+158 674-736-891'], ['+158 674-736-891'], ['+45 124-771-454'], ['+45 124-771-454'], ['+45 124-771-454'], ['+180 029-457-654'], ['+180 029-457-654'], ['+180 029-457-654'], ['+75 227-250-652'], ['+75 227-250-652'], ['+75 227-250-652'], ['+5 528-317-854'], ['+5 528-317-854'], ['+5 528-317-854'], ['+81 849-629-290'], ['+81 849-629-290'], ['+81 849-629-290'], ['+46 005-119-176'], ['+46 005-119-176'], ['+46 005-119-176'], ['+108 150-380-705'], ['+108 150-380-705'], ['+108 150-380-705'], ['+40 122-224-247'], ['+40 122-224-247'], ['+40 122-224-247'], ['+68 890-680-027'], ['+68 890-680-027'], ['+68 890-680-027'], ['+169 060-204-504'], ['+169 060-204-504'], ['+169 060-204-504'], ['+95 620-820-945'], ['+95 620-820-945'], ['+95 620-820-945'], ['+43 592-938-846'], ['+43 592-938-846'], ['+43 592-938-846'], ['+7 023-296-647'], ['+7 023-296-647'], ['+7 023-296-647'], ['+20 541-401-396'], ['+20 541-401-396'], ['+20 541-401-396'], ['+64 751-365-934'], ['+64 751-365-934'], ['+64 751-365-934'], ['+163 546-119-476'], ['+163 546-119-476'], ['+163 546-119-476'], ['+198 557-666-779'], ['+198 557-666-779'], ['+198 557-666-779'], ['+14 673-759-017'], ['+14 673-759-017'], ['+14 673-759-017'], ['+161 086-020-168'], ['+161 086-020-168'], ['+161 086-020-168'], ['+65 970-575-488'], ['+65 970-575-488'], ['+65 970-575-488'], ['+2 455-126-377'], ['+2 455-126-377'], ['+2 455-126-377'], ['+196 728-585-376'], ['+196 728-585-376'], ['+196 728-585-376'], ['+33 117-430-125'], ['+33 117-430-125'], ['+33 117-430-125'], ['+195 488-831-768'], ['+195 488-831-768'], ['+195 488-831-768'], ['+86 468-718-108'], ['+86 468-718-108'], ['+86 468-718-108'], ['+194 278-716-950'], ['+194 278-716-950'], ['+194 278-716-950'], ['+43 730-685-847'], ['+43 730-685-847'], ['+43 730-685-847'], ['+140 794-289-551'], ['+140 794-289-551'], ['+140 794-289-551'], ['+21 679-740-834'], ['+21 679-740-834'], ['+21 679-740-834'], ['+98 717-997-323'], ['+98 717-997-323'], ['+98 717-997-323'], ['+47 401-100-231'], ['+47 401-100-231'], ['+47 401-100-231'], ['+143 726-462-368'], ['+143 726-462-368'], ['+143 726-462-368'], ['+147 864-005-968'], ['+147 864-005-968'], ['+147 864-005-968'], ['+130 590-757-665'], ['+130 590-757-665'], ['+130 590-757-665'], ['+197 700-858-976'], ['+197 700-858-976'], ['+197 700-858-976'], ['+158 344-541-946'], ['+158 344-541-946'], ['+158 344-541-946'], ['+56 242-901-234'], ['+56 242-901-234'], ['+56 242-901-234'], ['+132 313-075-754'], ['+132 313-075-754'], ['+132 313-075-754'], ['+130 517-953-149'], ['+130 517-953-149'], ['+130 517-953-149'], ['+158 684-878-743'], ['+158 684-878-743'], ['+158 684-878-743'], ['+52 836-582-035'], ['+52 836-582-035'], ['+52 836-582-035'], ['+138 117-484-671'], ['+138 117-484-671'], ['+138 117-484-671'], ['+50 012-148-873'], ['+50 012-148-873'], ['+50 012-148-873'], ['+105 048-919-483'], ['+105 048-919-483'], ['+105 048-919-483'], ['+18 209-851-997'], ['+18 209-851-997'], ['+18 209-851-997'], ['+176 938-056-084'], ['+176 938-056-084'], ['+176 938-056-084'], ['+141 018-132-973'], ['+141 018-132-973'], ['+141 018-132-973'], ['+199 936-162-415'], ['+199 936-162-415'], ['+199 936-162-415'], ['+33 547-051-264'], ['+33 547-051-264'], ['+33 547