n = int(input())
planList = list(input().split())
direction_x = [0, 0, -1, 1]
direction_y = [-1, 1, 0, 0]
direction = ['L', 'R', 'U', 'D']
cur_x = 1
cur_y = 1
for plan in planList:
    for i in range(4):
        if plan == direction[i]:
            next_x = cur_x + direction_x[i]
            next_y = cur_y + direction_y[i]
            if next_x != 0 and next_x != n+1 and next_y != 0 and next_y != n+1:
                cur_x = next_x
                cur_y = next_y

print(cur_x, cur_y)




