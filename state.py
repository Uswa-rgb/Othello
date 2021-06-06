import copy 
class state:

    def __init__(self,alpha,beta,currstate,bList,wList):
        self.alpha =alpha
        self.beta= beta
        self.grid = copy.deepcopy(currstate)
        if bList is not None:
            self.blackList = copy.deepcopy(bList)
        else:
            self.blackList =[]
        if wList is not None:
            self.whiteList = copy.deepcopy(wList)
        else:
            self.whiteList =[]
        self.exists = False

    def printdata(self):
        print(self.alpha, " " , + self.beta)
    
    def evaluationFunction(self,player):
            return len(self.blackList)-len(self.whiteList)

    def storeCoordinates(self):
        for i in range(0,8):
            for j in range(0,8):
                if self.grid[i][j] == 1:
                     self.blackList.append((i,j))
                if self.grid[i][j] == 2:
                     self.whiteList.append((i,j))

    def successorFunction(self,player):
        print(player)
        if player == 1 :
            List = self.whiteList
        elif player == 2:
            List = self.blackList

        successorList = []

        for w in List:
            if  w[1] < 7 and self.grid[w[0]][w[1]+1] == 0: #right
                    state1 = state(self.alpha,self.beta,self.grid,None,None)              
                    state1.flipAllBalls(w[0],w[1]+1,player,False)
                    #set new coordinates
                    if self.grid != state1.grid:
                        state1.storeCoordinates()
                        successorList.append(state1)
                

            
            if  w[1] > 0 and self.grid[w[0]][w[1]-1] == 0 : #left
                    state1 = state(self.alpha,self.beta,self.grid,None,None)
                    state1.flipAllBalls(w[0],w[1]-1,player,False)
                    #set new coordinates
                    if self.grid != state1.grid:
                        state1.storeCoordinates()
                        successorList.append(state1)

            if  w[0] < 7 and self.grid[w[0]+1][w[1]] == 0: #down
                    state1 = state(self.alpha,self.beta,self.grid,None,None)
                    state1.flipAllBalls(w[0]+1,w[1],player,False)
                    #set new coordinates
                    if self.grid != state1.grid:
                        state1.storeCoordinates()
                        successorList.append(state1)
            

            if  w[0] > 0 and self.grid[w[0]-1][w[1]] == 0 : #up
                    state1 = state(self.alpha,self.beta,self.grid,None,None)
                    state1.flipAllBalls(w[0]-1,w[1],player,False)
                    #set new coordinates
                    if self.grid != state1.grid:
                        state1.storeCoordinates()
                        successorList.append(state1)
                
                

            if w[0] < 7 and w[1] > 0 and self.grid[w[0]+1][w[1]-1] == 0 :   #bottom-left
                if player ==1:
                    state1 = state(self.alpha,self.beta,self.grid,None,None)
                    state1.flipAllBalls(w[0]+1,w[1]-1,player,False)
                    #set new coordinates
                    if self.grid != state1.grid:
                        state1.storeCoordinates()
                        successorList.append(state1)

            if  w[0] < 7 and w[1] < 7 and self.grid[w[0]+1][w[1]+1] == 0 :   #bttom-right

                    state1 = state(self.alpha,self.beta,self.grid,None,None)
                   
                    state1.flipAllBalls(w[0]+1,w[1]+1,player,False)
                    #set new coordinates
                    if self.grid != state1.grid:
                        state1.storeCoordinates()
                        successorList.append(state1)
                

            if  w[0] > 0 and w[1] < 7 and self.grid[w[0]-1][w[1]+1] == 0:   #top-right
 
                    state1 = state(self.alpha,self.beta,self.grid,None,None)
                   
                    state1.flipAllBalls(w[0]-1,w[1]+1,player,False)
                    #set new coordinates
                    if self.grid != state1.grid:
                        state1.storeCoordinates()
                        successorList.append(state1)
                

            if  w[0] >0 and w[1] > 0 and self.grid[w[0]-1][w[1]-1] == 0:   #top-left

                    state1 = state(self.alpha,self.beta,self.grid,None,None)
                  
                    state1.flipAllBalls(w[0]-1,w[1]-1,player,False)
                    #set new coordinates
                    if self.grid != state1.grid:
                        state1.storeCoordinates()
                        successorList.append(state1)
      
        return successorList       

    def flipAllBalls(self,x,y,player, MoveCheck):
        if player == 1:
            a=1
            b=2
        elif player == 2:
            a=2
            b=1 

        # if y+1 <= 7:
        if y+1 <= 6:
            if self.grid[x][y+1] == b:    
                for i in range(y+1,8):      #rightcheck
                    if self.grid[x][i] == a:
                        if MoveCheck == False:
                            self.grid[x][y] = a
                            for j in range(i,y-1,-1):
                                self.grid[x][j] = a
                            break
                        elif MoveCheck == True:
                            return True
                    elif self.grid[x][i] != b:
                        break

        # if y-1 >= 0 :
        if y-1 >= 1 :        
            if self.grid[x][y-1] == b:
                for i in range(y-1,-1,-1):   #left check
                    if self.grid[x][i] == a:
                        if MoveCheck == False:
                            self.grid[x][y] = a
                            for j in range(i,y+1):
                                self.grid[x][j] = a
                            break
                        elif MoveCheck == True:
                            return True
                    elif self.grid[x][i] != b:
                        break

        #if x-1 >=0 :
        if x-1 >= 1 :
            if self.grid[x-1][y] == b:
                for i in range(x-1,-1,-1):    #up check
                    if self.grid[i][y] == a:
                        if MoveCheck ==False:
                            self.grid[x][y] = a
                            for j in range(i,x+1):
                                self.grid[j][y] = a
                            break
                        elif MoveCheck==True:
                            return True
                    elif self.grid[i][y] != b:
                        break 

        # if x+1 <= 7:
        if x+1 <= 6:
            if self.grid[x+1][y] == b:
                for i in range(x+1,8):    #down check
                    if self.grid[i][y] == a:
                        if MoveCheck ==False:
                            self.grid[x][y] = a
                            for j in range(i,x-1,-1):
                                self.grid[j][y] = a
                            break
                        elif MoveCheck ==True:
                            return True
                    elif self.grid[i][y] != b:
                        break 

        # if x+1 <= 7 and y-1 >= 0:
        # #if x+1 != 7 and y-1 != 0: 
        if x+1 <= 6 and y-1 >= 1:
             
            if self.grid[x+1][y-1] == b:
                k=y
                for i in range(x+1,8):    #bottom left
                    if k>0:
                        k-=1
                        if self.grid[i][k] == a:
                            if MoveCheck ==False:
                                self.grid[x][y] = a
                                for j in range(i,x-1,-1):
                                    self.grid[j][k] = a
                                    k+=1
                                break
                            elif MoveCheck == True:
                                return True
                        elif self.grid[i][k] != b:
                            break 
                    else:
                        break

        # if x+1 <=7 and y+1 <=7:
        if x+1 <=6 and y+1 <=6:
            if self.grid[x+1][y+1] == b:
                k=y
                for i in range(x+1,8) :    #bottom right
                    if k<7:
                        k+=1
                        if self.grid[i][k] == a:
                            if MoveCheck ==False :
                                self.grid[x][y] = a
                                for j in range(i,x-1,-1):
                                    self.grid[j][k] = a
                                    k-=1
                                break
                            elif MoveCheck ==True:
                                return True
                        elif self.grid[i][k] != b:
                            break                   
                    else:
                        break
        #if x-1 >=0 and y+1 <=7:
        if x-1 >=1 and y+1 <=6:
            if self.grid[x-1][y+1] == b:
                k=y
                for i in range(x-1,-1,-1):    #top right
                    if k<7:
                        k+=1
                        if self.grid[i][k] == a:
                            if MoveCheck ==False:
                                self.grid[x][y] = a
                                for j in range(i,x+1):
                                    self.grid[j][k] = a
                                    k-=1
                                break
                            elif MoveCheck ==True:
                                return True
                        elif self.grid[i][k] != b:
                            break     
                    else:
                        break
        #if x-1 >= 0 and y-1 >=0:
        if x-1 >= 1 and y-1 >=1:
            if self.grid[x-1][y-1] == b:
                k=y
                for i in range(x-1,-1,-1):    #top left
                    if k>0:
                        k-=1
                        if self.grid[i][k] == a:
                            if MoveCheck ==False:
                                self.grid[x][y] = a
                                for j in range(i,x+1):
                                    self.grid[j][k] = a
                                    k+=1
                                break
                            elif MoveCheck == True:
                                return True
                        elif self.grid[i][k] != b:
                            break
                    else:
                        break 
        return False

    def successorFunction2(self,player):

            flag =False
            List = self.blackList

            for w in List:
                if  w[1] < 7 and self.grid[w[0]][w[1]+1] == 0: #right
                        flag = self.flipAllBalls(w[0],w[1]+1,player,True)
                        if(flag):
                            return flag


                if  w[1] > 0 and self.grid[w[0]][w[1]-1] == 0 : #left
                        flag = self.flipAllBalls(w[0],w[1]-1,player,True)
                        if(flag):
                            return flag

                if  w[0] < 7 and self.grid[w[0]+1][w[1]] == 0: #down
                    flag = self.flipAllBalls(w[0]+1,w[1],player,True)
                    if(flag):
                        return flag 


                if  w[0] > 0 and self.grid[w[0]-1][w[1]] == 0 : #up
                    flag = self.flipAllBalls(w[0]-1,w[1],player,True)
                    if(flag):
                        return flag


                if w[0] < 7 and w[1] > 0 and self.grid[w[0]+1][w[1]-1] == 0 :   #bottom-left

                    flag = self.flipAllBalls(w[0]+1,w[1]-1,player,True)
                    if(flag):
                        return flag

                if  w[0] < 7 and w[1] < 7 and self.grid[w[0]+1][w[1]+1] == 0 :   #bttom-right
                    flag = self.flipAllBalls(w[0]+1,w[1]+1,player,True)
                    if(flag):
                        return flag

                if  w[0] > 0 and w[1] < 7 and self.grid[w[0]-1][w[1]+1] == 0:   #top-right
                        flag = self.flipAllBalls(w[0]-1,w[1]+1,player,True)
                        if(flag):
                            return flag

                if  w[0] >0 and w[1] > 0 and self.grid[w[0]-1][w[1]-1] == 0:   #top-left
                        flag = self.flipAllBalls(w[0]-1,w[1]-1,player,True)
                        if(flag):
                            return flag 

            return flag 

    