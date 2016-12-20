checks = {(0,0):[[(0,1),(0,2)],[(1,0),(2,0)],[(1,1),(2,2)]],
    (0,1):[[(0,0),(0,2)],[(1,1),(2,1)]],
    (0,2):[[(0,0),(0,1)],[(1,2),(2,2)],[(1,1),(2,1)]]
}

def makeMove(move,x,y):
    board[x][y] = move
    
def checkWins(board,move,tup):
    for i in checks[tup]:
        print "This is i"
        print i
        winner = 0
        for j in i:
            print j
            if board[j[0]][j[1]] == move:
                winner += 1
        if winner == 2:
            return True
                    
                    
board = [[0,0,0] for i in range(3)]
over = False
player = 0
while not over:
    print("Player {}".format(player)+"'s move: ")
    s = raw_input()
    print("Player {}".format(player)+"'s position: ")
    x,y = eval(raw_input()),eval(raw_input())
    makeMove(s,x,y)
    if checkWins(board,s,(x,y)):
        print "We have a winner"
        over = True
    player = (player + 1)%2
    print board
    
    
