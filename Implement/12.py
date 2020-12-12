def build_stick(sticks, bos ,x,y) :
    if y == 0 or sticks[x][y-1] : 
        return True
    if x>0 and bos[x-1][y] or bos[x][y] :	
        return True
    return False

def build_bo(sticks, bos ,x,y,n) :
    #보의 한쪽 끝 부분이 기둥 위에 있거나
    if sticks[x][y-1] or sticks[x+1][y-1] :
        return True
    # 양쪽 끝부분이 다른 보와 동시에 연결되어 있는 경우
    if x > 0 and bos[x-1][y] and bos[x+1][y] :
        return True
    return False

def remove(sticks, bos,x, y,n) :
    for i in range(n+1) :
        for j in range(n+1) :
            if sticks[i][j] :
                if not build_stick(sticks, bos,i, j) :
                    return False
            if bos[i][j] :
                if not build_bo(sticks, bos ,i,j,n) :
                    return False
    return True

def solution(n, build_frame):

    sticks = [[0] * (n+1) for i in range(n+1)]
    bos = [[0] * (n+1) for i in range(n+1)]
    answer = []

    for x, y, a, b in build_frame :
        if b == 1 : 
            if a == 0 :
                if build_stick(sticks, bos, x,y) :
                    sticks[x][y] = 1
            elif a == 1 : 
                if build_bo(sticks, bos, x,y,n) :
                    bos[x][y] = 1
        elif b == 0 :
            if a == 0 :
                sticks[x][y] = 0
            elif a == 1 :
                bos[x][y] = 0
            if not remove(sticks, bos,x,y,n) :
                if a == 0:
                    sticks[x][y] = 1
                else :
                    bos[x][y] = 1
                    
    for i in range(len(sticks[0])) :
        for j in range(len(sticks))	:
            if sticks[i][j] == 1 :
                answer.append([i,j,0])
            if bos[i][j] == 1 :
                answer.append([i,j,1])

    return answer