# Prompt: return the first decimal (from the left) to the tenths place
# Input: ['AIX 5.1'], Output: 5.1
# Input: ['VMware ESX Server 3.5.0 build-110268'], Output: 3.5
# Input: ['Linux Linux 2.6 Linux'], Output: 2.6
# Input: ['Red Hat Enterprise AS 4 <2.6-78.0.13.ELlargesmp>'], Output: 2.6
# Input: ['Microsoft <R> Windows <R> 2000 Advanced Server 1.0'], Output: 1.0
# Input: ['Microsoft Windows XP Win2008R2 6.1.7601'], Output: 6.1

def extract_decimal(input_str):
    import re
    decimal = re.search(r'\d+\.\d', input_str)
    if decimal:
        return decimal.group()
    else:
        return None

# Test cases
print(extract_decimal('AIX 5.1'))  # Output: 5.1
print(extract_decimal('VMware ESX Server 3.5.0 build-110268'))  # Output: 3.5
print(extract_decimal('Linux Linux 2.6 Linux'))  # Output: 2.6
print(extract_decimal('Red Hat Enterprise AS 4 <2.6-78.0.13.ELlargesmp>'))  # Output: 2.6
print(extract_decimal('Microsoft <R> Windows <R> 2000 Advanced Server 1.0'))  # Output: 1.0
print(extract_decimal('Microsoft Windows XP Win2008R2 6.1.7601'))  # Output: 6.1
5.1
3.5
2.6
2.6
1.0
6.1
