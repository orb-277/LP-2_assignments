global N
N = 6
def solve(board,row,cols,ndiag,rdiag):
    if row == len(board):
        for r in board:
            print(r)
        print()
        return
    for i in range(len(board)):
        if not(cols[i]) and not(ndiag[i+row]) and not(rdiag[row-i+len(board)-1]):
            cols[i] = True
            ndiag[i+row] = True
            rdiag[row-i+len(board)-1] = True
            board[row][i] = True
            solve(board,row+1,cols,ndiag,rdiag)
            cols[i] = False
            ndiag[i+row] = False
            rdiag[row-i+len(board)-1] = False
            board[row][i] = False

board = [[False]* N for i in range(N)]
cols = [False]* N
rdiag = [False]* (2*N-1)
ndiag = [False]* (2*N-1)

solve(board,0,cols,ndiag,rdiag)



