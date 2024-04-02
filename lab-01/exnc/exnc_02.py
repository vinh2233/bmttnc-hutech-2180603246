import re

chuoi = "-100#^sdfkj8902w3ir021@swf-20"

sum_am = 0
sum_duong = 0

for so in re.findall(r"[-+]?\d+", chuoi):
    number = int(so)
    if number > 0:
        sum_duong += number
    elif number < 0:
        sum_am += number

print("Tổng các số nguyên dương:", sum_duong)
print("Tổng các số nguyên âm:", sum_am)
print("Tổng các số nguyên: ", sum_am+sum_duong)