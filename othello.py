from graphics import *
from state import *
import time


   
def createGrid(win,State,list):
    
    x=100
    y=100
    size = 50
    for i in range(0,8):
        y=100
        for j in range(0,8): 
            if State.grid[i][j] == 1:
                circle = Circle(Point(y+25,x+25), 20)
                circle.setOutline(color_rgb(0,255,255))
                circle.setFill(color_rgb(0,0,0))
                circle.draw(win)
            elif State.grid[i][j] == 2:
                circle = Circle(Point(y+25,x+25), 20)
                circle.setOutline(color_rgb(0,255,255))
                circle.setFill(color_rgb(255,255,255))
                circle.draw(win)
            y=y+size
        x=x+size

    for  i in list:
        i.undraw()
    list[0].setText(str(len(State.blackList))) 
    list[1].setText(str(len(State.whiteList)))

    for i in list:
        i.draw(win)    
    #win.getMouse()
    
    


def miniMax(currState, depth ,isMax,player):
    if depth == 0:
        return currState.evaluationFunction(player) , currState
    else:
        if(isMax):
            bestVal = int(-9999)
            successorList = currState.successorFunction(player)
            player=2
            bestVal = currState.alpha
            bestState = currState
            for i in successorList:   
               value ,s1=  miniMax(i,depth-1,not isMax,player)
               if bestVal < value:
                    bestState = i
                    bestVal = value
               currState.alpha = max(currState.alpha,bestVal)
               if currState.beta <= currState.alpha:
                   break

            return bestVal,bestState

        elif not isMax:
            bestVal = int(9999)
            successorList = currState.successorFunction(player)
            player = 1

            bestVal = currState.beta
            bestState = currState
            for i in successorList:   
               value,s1 =  miniMax(i,depth-1,not isMax,player)
            
               if bestVal > value:
                    bestState = i
                    bestVal = value
               currState.beta = min(currState.beta,bestVal)
               if currState.beta <= currState.alpha:
                   break

            return bestVal,bestState



def main():
    win = GraphWin('othello', 600, 600)
    win.setBackground(color_rgb(128,128,128))  

    gname = Text(Point(300,200),'OTHELLO')
    gname.setTextColor('pink')
    gname.setStyle('bold')
    gname.setSize(35)
    gname.draw(win)

    diff = Text(Point(300,250),'SELECT DIFFICULTY LEVEL')
    diff.setStyle('bold')
    diff.draw(win)

    square = Rectangle(Point(150,300),Point(250,350))
    square.setOutline(color_rgb(0,0,0))
    square.setFill('pink')
    square.draw(win)

    text = Text(Point(200,325),'EASY')
    text.setStyle('bold')
    text.draw(win)

    square = Rectangle(Point(350,300),Point(450,350))
    square.setOutline(color_rgb(0,0,0))
    square.setFill('pink')
    square.draw(win)

    text1 = Text(Point(400,325),'HARD')
    text1.setStyle('bold')
    text1.draw(win)

    
    level = Text(Point(460,55),2) 
    level1 = Text(Point(160,55),2)
    level.setTextColor('black')
    level.setStyle('bold')
    level1.setStyle('bold')
    # level.draw(win)
    # level1.draw(win)
    circle1 = Circle(Point(400+25,30+25), 20)
    circle1.setOutline(color_rgb(0,255,255))
    circle1.setFill(color_rgb(0,0,0))
    # circle1.draw(win)
    circle2 = Circle(Point(100+25,30+25), 20)
    circle2.setOutline(color_rgb(0,255,255))
    circle2.setFill(color_rgb(255,255,255))
    # circle2.draw(win)

    items =[level, level1,circle1,circle2]

    while(True):
        p = win.getMouse()
        print(p)
        if p.getX() >= 150 and p.getX() <=250 and p.getY() <=350 and p.getY() >= 300:
            depth = 1
            break
        elif  p.getX() >= 350 and p.getX() <=450 and p.getY() <=350 and p.getY() >= 300:
            depth = 3
            break

    x=100
    y=100
    size = 50
    for i in range(0,8):
        y=100
        for j in range(0,8):
            square = Rectangle(Point(x,y),Point(x+size,y+size))
            square.setOutline(color_rgb(0,0,0))
            square.setFill('pink')
            square.draw(win)
            y=y+size
        x=x+size

    grid = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],]
    grid[3][3] = 1
    grid[3][4] = 2
    grid[4][3] = 2
    grid[4][4] = 1
    grid[2][3] = 0
    grid[1][2] = 0

    blist = [(3,3),(4,4)]
    wlist = [(3,4),(4,3)]
    state1 = state(-9999,9999,grid,blist,wlist)
    createGrid(win,state1,items)
    ENDSTATE = None
    isMax = True

    

    while(True):
        a,oppState = miniMax(state1,depth,isMax,1)
        createGrid(win,oppState,items)
        if(endGame(oppState)):
            ENDSTATE = oppState
            break
        userState = userInput(win,oppState)
        createGrid(win,userState,items)
        if(endGame(userState)):
            ENDSTATE =userState
            break 
        state1= userState
        time.sleep(1)
    
    if len(ENDSTATE.blackList) > len(ENDSTATE.whiteList):
        winner = 'CPU WON'
    elif len(ENDSTATE.blackList) < len(ENDSTATE.whiteList):
        winner = 'YOU WON'
    elif len(ENDSTATE.blackList) == len(ENDSTATE.whiteList):
        winner = 'DRAW'
    
    circle = Circle(Point(300,300), 200)
    circle.setOutline(color_rgb(0,255,255))
    circle.setFill(color_rgb(255,255,255))
    circle.draw(win)

    playerwon = Text(Point(300,200),'GAME OVER')
    playerwon.setTextColor('pink')
    playerwon.setStyle('bold')
    playerwon.setSize(35)
    playerwon.draw(win)

    playerwon = Text(Point(300,300),winner)
    playerwon.setTextColor('pink')
    playerwon.setStyle('bold')
    playerwon.setSize(35)
    playerwon.draw(win)

    win.getMouse()



def endGame(State):

    for i in range(0,8):
        for j in range(0,8): 
            if State.grid[i][j] == 0:
                return False
    return True

def userInput(win,oppState):
        
    p1 = win.getMouse()
    y = int(((p1.getX()-(p1.getX()%50)) -100)/50)
    x = int(((p1.getY()-(p1.getY()%50)) -100)/50)
    print(x)
    print(y)
    validMove = checkValidMove(x,y,oppState.grid)
    if (oppState.successorFunction2(2)):
        while(validMove != 2):
            print("invalid move")
            p1 = win.getMouse()
            y = int(((p1.getX()-(p1.getX()%50)) -100)/50)
            x = int(((p1.getY()-(p1.getY()%50)) -100)/50)
            validMove = checkValidMove(x,y,oppState.grid)   
        

    if validMove == 2:    
        userState = state(oppState.alpha,oppState.beta,oppState.grid,None,None)
        userState.flipAllBalls(x,y,2,False)
        if oppState.grid != userState.grid:  
            userState.grid[x][y] = 2
        userState.storeCoordinates()
        return userState
    else:
        return oppState

def checkValidMove(x,y,grid):
    b=1
    a=2
    if grid[x][y] == 0:
        if y+1 <= 7:
            if grid[x][y+1] == b:    
                for i in range(y+1,8):      #rightcheck
                    if grid[x][i] == a:
                        return 2
                    elif grid[x][i] != b:
                        break 
        if y-1 >= 0 :        
                if grid[x][y-1] == b:
                    for i in range(y-1,-1,-1):   #left check
                        if grid[x][i] == a:
                            return 2
                        elif grid[x][i] != b:
                            break
        if x-1 >= 0 :
                if grid[x-1][y] == b:
                    for i in range(x-1,-1,-1):    #up check
                        if grid[i][y] == a:
                            return 2
                        elif grid[i][y] != b:
                            break 

            # if x+1 <= 7:
        if x+1 <= 7:
            if grid[x+1][y] == b:
                for i in range(x+1,8):    #down check
                    if grid[i][y] == a:
                        return 2
                    elif grid[i][y] != b:
                        break 

            # if x+1 <= 7 and y-1 >= 0: 
            #if x+1 != 7 and y-1 != 0:
        if x+1 <= 6 and y-1 >= 1:
             
            if grid[x+1][y-1] == b:
                k=y
                for i in range(x+1,8):    #bottom left
                    if k>0:
                        k-=1
                        if grid[i][k] == a:
                            return 2
                        elif grid[i][k] != b:
                            break 
                    else:
                        break
        # if x+1 <=7 and y+1 <=7:
        if x+1 <=6 and y+1 <=6:
            if grid[x+1][y+1] == b:
                k=y
                for i in range(x+1,8) :    #bottom right
                    if k<7:
                        k+=1
                        if grid[i][k] == a:
                            return 2
                        elif grid[i][k] != b:
                            break                   
                    else:
                        break
        #if x-1 >=0 and y+1 <=7:
        if x-1 >=1 and y+1 <=6:
            if grid[x-1][y+1] == b:
                k=y
                for i in range(x-1,-1,-1):    #top right
                    if k<7:
                        k+=1
                        if grid[i][k] == a:
                            return 2
                        elif grid[i][k] != b:
                            break     
                    else:
                        break
        #if x-1 >= 0 and y-1 >=0:
        if x-1 >= 1 and y-1 >=1:
            if grid[x-1][y-1] == b:
                k=y
                for i in range(x-1,-1,-1):    #top left
                    if k>0:
                        k-=1
                        if grid[i][k] == a:
                            return 2
                        elif grid[i][k] != b:
                            break
                    else:
                        break 
        return 0
    else:
        return 1

main()    