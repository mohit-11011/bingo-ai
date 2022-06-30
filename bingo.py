#Pranit 
#102197025

#Mohit
#102197021

#2CS8
import random
import copy
class bingo:
    def __init__(self,AI_start,player_start,usrname):
        self.num_chosen=None
        self.AI_state=AI_start
        self.player_state=player_start
        self.num_left=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        self.AI_bingo=[0,0,0,0,0]
        self.player_bingo=[0,0,0,0,0]       
        self.Heuristic_val=self.heuristic()
        self.username=usrname
    def display(self):
        print("------------------")
        print(f"{self.username} State:")
        for i in range(5):
            for j in range(5):
                if(self.player_state[i][j]==0):
                    print("X",end="\t")
                else:
                    print(self.player_state[i][j],end="\t")
            print()
        print()
        print("B\tI\tN\tG\tO")
        for i in range(5):
            print(self.player_bingo[i],end="\t")
        print()
        print("------------------")
    def move(self,num):
        AI_coords=self.find_num(1,num)
        player_coords=self.find_num(0,num)
        self.AI_state[AI_coords[0]][AI_coords[1]] = 0
        self.player_state[player_coords[0]][player_coords[1]] = 0
        self.num_left.remove(num)
        self.bingo_check(AI_coords,player_coords)
        self.Heuristic_val=self.heuristic()
        self.num_chosen=num
    def bingo_check(self,AI_coords,player_coords):
        flag=True
        for i in range(5):
            if self.AI_state[AI_coords[0]][i]:
                flag=False
                break
        if flag:
            i=0
            while(self.AI_bingo[i]):
                i+=1
            self.AI_bingo[i]=1
            if i==4:
                return
        flag=True
        for i in range(5):
            if self.AI_state[i][AI_coords[1]]:
                flag=False
                break
        if flag:
            i=0
            while(self.AI_bingo[i]):
                i+=1
            self.AI_bingo[i]=1
            if i==4:
                return
        if AI_coords[0]==AI_coords[1]:
            flag=True
            for i in range(5):
                if self.AI_state[i][i]:
                    flag=False
                    break
            if flag:
                i=0
                while(self.AI_bingo[i]):
                    i+=1
                self.AI_bingo[i]=1
                if i==4:
                    return
        if AI_coords[0]+AI_coords[1]==4:
            flag=True
            for i in range(5):
                if self.AI_state[i][4-i]:
                    flag=False
                    break
            if flag:
                i=0
                while(self.AI_bingo[i]):
                    i+=1
                self.AI_bingo[i]=1
                if i==4:
                    return
        flag=True
        for i in range(5):
            if self.player_state[player_coords[0]][i]:
                flag=False
                break
        if flag:
            i=0
            while(self.player_bingo[i]):
                i+=1
            self.player_bingo[i]=1
            if i==4:
                return
        flag=True
        for i in range(5):
            if self.player_state[i][player_coords[1]]:
                flag=False
                break
        if flag:
            i=0
            while(self.player_bingo[i]):
                i+=1
            self.player_bingo[i]=1
            if i==4:
                return
        if player_coords[0]==player_coords[1]:
            flag=True
            for i in range(5):
                if self.player_state[i][i]:
                    flag=False
                    break
            if flag:
                i=0
                while(self.player_bingo[i]):
                    i+=1
                self.player_bingo[i]=1
                if i==4:
                    return
        if player_coords[0]+player_coords[1]==4:
            flag=True
            for i in range(5):
                if self.player_state[i][4-i]:
                    flag=False
                    break
            if flag:
                i=0
                while(self.player_bingo[i]):
                    i+=1
                self.player_bingo[i]=1
                if i==4:
                    return
    def heuristic(self):
        count1=0
        count2=0
        values=[]
        for i in range(5):
            for j in range(5):
                if self.AI_state[i][j]:
                    count1+=1
                if self.AI_state[j][i]:
                    count2+=1
            values.append(count1)
            values.append(count2)
            count1=0
            count2=0
        for i in range(5):
            if self.AI_state[i][i]:
                count1+=1
            if self.AI_state[i][4-i]:
                count2+=1
        values.append(count1)
        values.append(count2)
        values.sort()
        sum=0
        for i in range(5):
            sum+=values[i]
        return sum    
    def find_num(self,val,num):
        if(val):
            for i in range(5):
                for j in range(5):
                    if self.AI_state[i][j]==num:
                        return [i,j]
        else:
            for i in range(5):
                for j in range(5):
                    if self.player_state[i][j]==num:
                        return [i,j]
    def movegen(self):
        nextstates=[]
        for i in self.num_left:
            state=copy.deepcopy(self)
            state.move(i)
            nextstates.append(state)
        return nextstates
    
    def isGoalReached(self):
        flag=True
        for i in range(5):
            if self.player_bingo[i]==0:
                flag=False
                break
        if(flag):
            print(f"Bingo!!! {self.username} Wins")
            return True
        else:
            flag=True
            for i in range(5):
                if self.AI_bingo[i]==0:
                    flag=False
                    break
            if(flag):
                print("Bingo!!! AI Wins")
                print("------------------")
                return True
            else:
                return False
    def move_ai(self):
        print(f"ai chose : {self.num_chosen} ")








def game(prob):
    
    prob.display()
    while(True):
        x=int(input("Enter the number: "))
        if x in prob.num_left:
            prob.move(x)
            print("AFTER PLAYER MOVE")
            prob.display()
            if prob.isGoalReached():
                break
            NextStates=prob.movegen()
            min=prob.Heuristic_val
            for i in NextStates:
                if i.Heuristic_val<min:
                    min=i.Heuristic_val
                    node=i
            prob=node
            prob.move_ai()
            prob.display()
            if prob.isGoalReached():
                break
        else:
            print("Number not available pick another")
            continue







print("""
     ________    _______________
    |   ___  \\  /              /
    |  |   \\  |/              /\\
    |  |   |  |__  ___     __/ _\\____   ______
    |  |__/  /|  |/   \\   |  |/  ____\\ /  __  \\
    |   __  < |  |     \\  |  |  |     |  |  |  |
    |  |  \\  \\|  |  |\\  \\ |  |  |  ___|  |  |  |
    |  |   |  |  |  | \\  \\|  |  | /_  |  |  |  |
    |  |___/  |  |  |  \\     |  |__/  |  |__|  |
    |________/|__|\\_|  /\\___/ \\______/\\\\______/
      /               /\\               \\
     /______GAME_____/OF\\____NUMBERS____\\
""")
username=input("enter your name : ")
pllist=input("create your grid      Automatic : n     self : y ")
player_start=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
templist=[] 
if pllist=="y":
    i=0
    while(i<25):
        x=int(input("enter the element "))
        if x not in templist and x>=1 and x<=25:
            templist.append(x)
            i+=1
        else:
            print("the number is already there or invalid number")
            
        k=0
    for i in range(5):
        for j in range(5):
            player_start[i][j]=templist[k]
            k+=1
elif pllist=='n':
    print("creating player list automatically")
    t=random.sample(range(1,26), 25)
    k=0
    for i in range(5):
        for j in range(5):
            player_start[i][j]=t[k]
            k+=1
AI_start=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
aicopy=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
l=random.sample(range(1,26), 25)
k=0
for i in range(5):
    for j in range(5):
        AI_start[i][j]=l[k]
        aicopy[i][j]=l[k]
        k+=1
prob=bingo(AI_start,player_start,username)
game(prob)



print("Now you get to see ai grid")
for i in range(5):
            for j in range(5):
                if(aicopy[i][j]==0):
                    print("X",end="\t")
                else:
                    print(aicopy[i][j],end="\t")
            print()