'''
【样例输入】
12
4
4 6 6 12
6 4 4 8
【样例输出】
最优解为：3 4
即选择第3、4物品。
当m[2, 12]，和m[3, 12]（表示不选第2个物品）以及m[3, 12-4]+6（表示选第2个物品）值一样时，
x[2]为0，即表示不选当前第2个物品。
'''
def knapsack(v, w, C, n):
    m = [[0 for _ in range(C + 1)] for _ in range(n + 1)]

    jMax = min(w[n - 1] - 1, C)
    for j in range(jMax + 1):
        m[n][j] = 0

    for j in range(w[n - 1], C + 1):
        m[n][j] = v[n - 1]

    for i in range(n - 1, 1, -1):
        jMax = min(w[i - 1] - 1, C)
        for j in range(jMax + 1):
            m[i][j] = m[i + 1][j]

        for j in range(w[i - 1], C + 1):
            m[i][j] = max(m[i + 1][j], m[i + 1][j - w[i - 1]] + v[i - 1])

    m[1][C] = m[2][C]

    if C >= w[0]:
        m[1][C] = max(m[1][C], m[2][C - w[0]] + v[0])

    return m


def traceback(m, w, c, n):
    x = [0] * (n+1)

    for i in range(1, n):
        if m[i][c] == m[i + 1][c]:
            x[i] = 0
        else:
            x[i] = 1
            c -= w[i - 1]

    x[n] = 1 if m[n][c] else 0

    return x



# 输入
c = int(input())
n = int(input())
v = list(map(int, input().split()))
w = list(map(int, input().split()))

# 计算最大价值表格
result = knapsack(v, w, c, n)

for i in result:
    print(i)

# 进行回溯得到选择的物品序列
selected_items = traceback(result, w, c, n)

# 输出最大价值
print(result[1][c])
print(selected_items)

# 输出选择的物品序列
for i in range(n+1):
    if selected_items[i] == 1:
        print(i, end=' ')
