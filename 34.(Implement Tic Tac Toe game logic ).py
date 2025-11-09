def sum (a,b,c):
    return a+b+c
def printBoard(xState, cState):
    zero = {'X'if xState [0] else("0" if cState [0] else 0)}
    one = { 'X'if xState [1] else("0" if cState [1] else 1)}
    two = { 'X'if xState [2] else("0" if cState [2] else 2)}
    three= { 'X'if xState [3] else("0" if cState [3] else 3)}
    four= { 'X'if xState [4] else("0" if cState [4] else 4)}
    five= { 'X'if xState [5] else("0" if cState [5] else 5)}
    six= { 'X'if xState [6] else("0" if cState [6] else 6)}
    seven= { 'X'if xState [7] else("0" if cState [7] else 7)}
    eight= { 'X'if xState [8] else("0" if cState [8] else 8)}
    print(f"| {zero} | {one} | {two} |")
    print(f"|_____|_____|_____|")
    print(f"| {three} | {four} | {five} |")
    print(f"|_____|_____|_____|")
    print(f"| {six} | {seven} | {eight} |")
    print(f"|_____|_____|_____|")
def checkWin(xState, cState):
    wins = [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
    for win in wins:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]]) == 3):
            return 1
        print("x won the match")
        if(sum(cState[win[0]],cState[win[1]],cState[win[2]]) == 3):
            return 0
        print("0 won the match")
        return -1
if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    cState = [0,0,0,0,0,0,0,0,0]
    turn = 1
    print("Welcome to Ptic Mtac Toe")
    while (True):
        printBoard(xState, cState)
        if turn == 1:
            print("X's Chance")
            val = int(input("Enter the value :"))
            xState[val] = 1
        else:
            print("0's Chance")
            val = int(input("Enter the value :"))
            cState[val] = 1
        cwin = checkWin(xState, cState)
        if (cwin != -1):
            print("Match over")
            break

        turn = 1 - turn
      
