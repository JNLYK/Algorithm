'''
【样例输入】
12
4
4 6 6 12
6 4 4 8
【样例输出】
最优解为：2 4
即选择第2、4物品。
当m[2, 12]，和m[3, 12]（表示不选第2个物品）以及m[3, 12-4]+6（表示选第2个物品）值一样时，
即表示不选当前第3个物品。
'''
def bag(n, c, w, v):
    # 初始化表格以存储子问题的最大值
    value = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

    # 填充表格
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            # 如果当前物品的重量小于等于背包容量，选择装入或不装入背包的最大值
            if w[i - 1] <= j:
                value[i][j] = max(value[i - 1][j], v[i - 1] + value[i - 1][j - w[i - 1]])
            else:
                # 如果当前物品的重量大于背包容量，不装入背包
                value[i][j] = value[i - 1][j]

    return value

def show(n, c, w, value):
    print(value[n][c])

    # 回溯找出所选择的物品
    i, j = n, c
    selected_items = []

    while i > 0 and j > 0:
        if value[i][j] != value[i - 1][j]:
            selected_items.append(i)
            j -= w[i - 1]
        i -= 1

    selected_items.reverse()
    for i in selected_items:
        print(i,end=' ')

# 输入
c = int(input())
n = int(input())
v = list(map(int, input().split()))
w = list(map(int, input().split()))

# 计算最大价值表格
value = bag(n, c, w, v)

# 显示结果
show(n, c, w, value)

'''
c = int(input())
n = int(input())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

f = [[0] * (c + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(c + 1):
        f[i][j] = f[i - 1][j]
        if j >= v[i - 1]:
            if f[i][j] < f[i - 1][j - v[i - 1]] + w[i - 1]:
                f[i][j] = f[i - 1][j - v[i - 1]] + w[i - 1]

print(f[n][c])

'''


