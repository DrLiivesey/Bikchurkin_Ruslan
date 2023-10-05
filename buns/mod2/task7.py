binary = input()
count_0 = 0
count_1 = 0
for i in binary:
    if i == "0":
        count_0 += 1
    elif i == "1":
        count_1 += 1
if count_0 == count_1:
    print("yes")
else:
    print("no")