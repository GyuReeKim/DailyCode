# 백준 11559번 Puyo Puyo

def puyo_delete(board, visited):
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                board[i][j] = '.'


def puyo_move(board):
    for j in range(M):
        temp = []
        blank_count = 0
        for i in range(N):
            if board[i][j] != '.':
                temp += [board[i][j]]
            else:
                blank_count += 1
        temp = ['.'] * blank_count + temp

        for i in range(N):
            board[i][j] = temp[i]


def color_4_up(i, j, color):
    global board, visited
    q = [''] * N * M
    visited = [[0 for b in range(M)] for a in range(N)]
    start, end = -1, -1

    visited[i][j] = 1
    end += 1
    q[end] = [i, j]

    while start != end:
        start += 1
        si, sj = q[start][0], q[start][1]
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if board[ni][nj] == colors[color]:
                    visited[ni][nj] = 1
                    end += 1
                    q[end] = [ni, nj]
    # print(temp)
    temp_cnt = 0
    for r in range(N):
        for c in range(M):
            if visited[r][c] == 1:
                temp_cnt += 1
    # print(temp_cnt)
    if temp_cnt >= 4:
        puyo_delete(board, visited)
        # pprint.pprint(board, indent=4, width=M * 10)
        return 1
    # print(board)
    return 0


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
colors = ['R', 'G', 'B', 'P', 'Y']

N, M = 12, 6
board = [list(input()) for _ in range(12)]

cnt = 0
while True:
    turn = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != '.':
                color = -1
                for k in range(len(colors)):
                    if board[i][j] == colors[k]:
                        color = k
                # 4개 이상 연속된 puyo 지워주기
                if color_4_up(i, j, color) == 1:
                    turn = 1
    # board 정렬하기
    if turn == 1:
        cnt += 1
        puyo_move(board)
        # pprint.pprint(board, indent=4, width=M * 10)
    if turn == 0:
        break
    # pprint.pprint(board, indent=4, width=M*10)
print(cnt)