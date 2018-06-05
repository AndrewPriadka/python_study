a = [[-1, 2, 3], [-1, -5, 6], [7, -8, 9]]
n = len(a)
for i in range(n):
    for j in range(n):
        if a[i][j] < 0:
            a[i][j] = 0
        print(a[i][j])
print(a)
