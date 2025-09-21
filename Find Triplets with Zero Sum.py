num = [-1, 0, 1, 2, -1, -4]
num.sort()
res = []

for i in range(len(num) - 2):
    l, r = i + 1, len(num) - 1
    while l < r:
        s = num[i] + num[l] + num[r]
        if s == 0:
            res.append([num[i], num[l], num[r]])
            l += 1
            r -= 1
        elif s < 0:
            l += 1
        else:
            r -= 1

print(res)
