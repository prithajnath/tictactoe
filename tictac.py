checks = {(0,0):[[(0,1),(0,2)],[(1,0),(2,0)],[(1,1),(2,2)]],
    (0,1):[[(0,0),(0,2)],[(1,1),(2,1)]],
    (0,2):[[(0,0),(0,1)],[(1,2),(2,2)],[(1,1),(2,1)]],
    (1,0):[[(1,1),(1,2)],[(0,0),(2,0)]],
    (1,1):[[(0,0),(2,2)],[(0,1),(2,1)],[(0,2),(2,0)],[(1,0),(1,2)]],
    (1,2):[[(0,2),(2,2)],[(1,0),(1,1)]],
    (2,0):[[(0,0),(1,0)],[(1,1),(0,2)],[(2,2),(2,1)]],
    (2,1):[[(2,0),(2,2)],[(1,1),(0,1)]],
    (2,2):[[(1,1),(0,0)],[(0,2),(1,2)],[(2,0),(2,1)]]
}

pos = {1:(0,0),
    2:(0,1),
    3:(0,2),
    4:(1,0),
    5:(1,1),
    6:(1,2),
    7:(2,0),
    8:(2,1),
    9:(2,2)
}

def makeMove(move,x,y):
    board[x][y] = move
    
def checkWins(board,move,tup):
    for i in checks[tup]:
        #print "This is i"
        #print i
        winner = 0
        for j in i:
            #print j
            if board[j[0]][j[1]] == move:
                winner += 1
        if winner == 2:
            return True
def printboard(board):
    print board[0]
    print board[1]
    print board[2]
                    
                    
board = [['_','_','_'] for i in range(3)]
over = False
player = 0
while not over:
    print("Player {}".format(player)+"'s move: ")
    s = raw_input()
    print("Player {}".format(player)+"'s position: ")
    x = eval(raw_input())
    if board[pos[x][0]][pos[x][1]] != '_':
        print("Cell already taken. Pick another one: ")
        continue
    makeMove(s,pos[x][0],pos[x][1])
    if checkWins(board,s,pos[x]):
        print "Player {}".format(player)+" wins!!"
        over = True
    player = (player + 1)%2
    printboard(board)
    
    
