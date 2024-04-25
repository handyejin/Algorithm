n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)
group1 = input()
group2 = input()
check = False

t = int(input())
# 방향 리스트
d_list = []
# 개미열 리스트
c_list = []
# 개미열
col = "".join(reversed(group1)) + group2
for i in range(n1-1, -1, -1):
    c_list.append(group1[i])
    d_list.append(1)
for i in range(n2):
    c_list.append(group2[i])
    d_list.append(2)

for i in range(t):
    for j in range(len(c_list)-1):
        if check:
            check = False
            continue
        if d_list[j] == 1 and d_list[j+1] == 2:
            d_list[j] = 2
            d_list[j+1] = 1
            c_list[j], c_list[j+1] = c_list[j+1], c_list[j]
            check = True

for c in c_list:
    print(c, end='')