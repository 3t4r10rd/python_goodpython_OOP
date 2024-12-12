a = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
]

s = []
for i in a:
    for j in i:
        s.append(j)

s = [0, 0, 1,
     1, 1, 0,
     0, 0, 1]

x = [s[0:3:], s[3:6:], s[6:9:], s[0::3], s[1::3], s[2::3], s[0::4], s[2:7:2]]

print(any(map(lambda i: i[0] == 1 and i[1] == 1 and i[2] == 1, x)))



