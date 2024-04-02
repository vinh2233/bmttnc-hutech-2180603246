import re

chuoi = "-100#^sdfkj8902w3ir021@swf-20"

positive_sum = 0
negative_sum = 0

for so in re.findall(r"[-+]?\d+", chuoi):
    number = int(so)
    if number > 0:
        positive_sum += number
    elif number < 0:
        negative_sum += number

print("Sum of positive integers:", positive_sum)
print("Sum of negative integers:", negative_sum)