import random as r

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
        winner = 0
        for j in i:
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
moves = ['X','O']
player = 1
print("2 Players or play against computer? Press 1 for 2P and 2 to play against computer: ")
n = eval(raw_input())
print("Player 0's symbol.Press 0 for X and 1 for O:")
s = eval(raw_input())
print("Player 0's move: ")
x = eval(raw_input())
makeMove(moves[s],pos[x][0],pos[x][1])
printboard(board)
while not over:
    
    if n == 2 and player == 1:
        print("Player {}".format(player)+"'s move: ")
        x = r.randint(1,9)
        if board[pos[x][0]][pos[x][1]] != '_':
            print("Cell already taken. Pick another one: ")
            continue
        s = (s+1)%2
        makeMove(moves[s],pos[x][0],pos[x][1])
    else:
        print("Player {}".format(player)+"'s move: ")
        x = eval(raw_input())
        if board[pos[x][0]][pos[x][1]] != '_':
            print("Cell already taken. Pick another one: ")
            continue
        s = (s+1)%2
        makeMove(moves[s],pos[x][0],pos[x][1])

    if checkWins(board,moves[s],pos[x]):
        print "Player {}".format(player)+" wins!!"
        over = True
    player = (player + 1)%2
    printboard(board)    
