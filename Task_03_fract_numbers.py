max_denum = 11
flag = True
for num in range(1, max_denum):
    for denum in range(num, max_denum + 1):
        for i in range(2, num + 1):
            if (num % i == 0 and denum % i == 0):
                flag = False
        if flag and denum != 1:
            print(f"{num}/{denum}", end=' ')
        flag = True
