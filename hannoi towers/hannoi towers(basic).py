#This class is going to manage the towers:
#   the amount of towers in play
#   the moving of the discs
#   validate nthe moves/ enforce the rules
class Towers():
    def __init__(self):
        self.tower=[]

    #Gets the disc object
    #Compares its weight to the weight of the previous disc
    #if the weight of the previous disc os bigger, adds it to the tower
    def addDisc(self,disc):
        #Checks id the tower is not 'empty'
        if int(len(self.tower))>0:
            #Checking the weight of the disc against the previous disc
            #Checking if the move is valid
            if self.tower[int(len(self.tower))-1].getWeight()>disc.getWeight():
                #Adding the disc to the tower
                self.tower.append(disc)
                
        else:
            self.tower.append(disc)

    #This method returns every disc that is stored in it
    def getTowerDiscs(self):
        show=[]
        if int(len(self.tower))!=0:
            for disc in self.tower:
                show.append(disc.getWeight())
                #print(show)
        else:
            show.append("EMPTY")
        return show

    #The tower is essentially a glorified stack
    def pull(self):
        #stores the value of the last item
        temp=self.tower[int(len(self.tower))-1]
        #removes the last item from the list
        #print(str(self.tower[int(len(self.tower))-1].getWeight()))
        self.tower.pop(int(len(self.tower))-1)
        return temp

    def getLength(self):
        return int(len(self.tower))
            
#This class is going to manage the discs:
    #   Assign thier size
class discs():
    def __init__(self,weight):
        self.weight=weight

    def getWeight(self):
        return self.weight

    
#-----------------------------------------------------------------------------------
#[FUNCTION]
#Add all of the discs to the first tower
def getStart(towers,discs):
    count=0
    for item in discs:
        #Adding each individual disc to the first tower
        towers[0].addDisc(discs[count])
        count+=1

def getWin(towers):
    return int(len(towers[0].getTowerDiscs()))
    
        
def display(towers):
    #This creates a counter which is used for the UI
    #The loop is intended to desplay everything that is in the tower
    count=0
    for tower in towers:
        count+=1
        print ("Tower "+str(count))
        print(tower.getTowerDiscs())

def checkTower(tower):
    if tower.getTowerDiscs()==["EMPTY"]:
        return False
    else:
        return True
        
#Decides how many towers and discs will be in play
amountOfDiscs=int(input("[has to be three or more]\n\
How many discs/towers do you want to play?: "))
if amountOfDiscs<3:
    while amountOfDiscs<3:
        amountOfDiscs=int(input("[invalid number]\n\
[has to be three or more]\n\
How many discs do you want to play?: "))
        
#Array to store all of the tower objects
towersArray=[]
#Array to store all of the disc objects
discsArray=[]
amountTemp=amountOfDiscs
#loop that creates all of the objects needed for the game
#for item in amountOfDiscs:
while amountTemp!=0:
    #Creates a disc object and adds it to the array of disc objects
    disc=discs(amountTemp)
    discsArray.append(disc)

    #creates a tower object and adds it to the array of tower objects
    tower=Towers()
    towersArray.append(tower)
    amountTemp-=1
    
#sets the start state of the game
getStart(towersArray,discsArray)
win=getWin(towersArray)
#display(towersArray)

print (str(win))
#gameplay loop
while towersArray[int(len(towersArray))-1].getLength()!=win:
    print("--------------------------")
    #shows the contents of each tower before each move
    display(towersArray)

    moveTower=int(input("[The tower you pick has to be populated with at least 1 disc]\n\
which tower do you want to select: \n"))
    if moveTower>int(len(towersArray)) or moveTower<1 or checkTower(towersArray[moveTower-1])==False:
        while moveTower>int(len(towersArray)) or moveTower<1 or checkTower(towersArray[moveTower-1])==False:
            moveTower=int(input("[The tower you have chosen does not exist or has nothing in it]\n\
                                [The tower you pick has to be populated with at least 1 disc]\n\
which tower do you want to select: \n"))

    desisredDisc = towersArray[moveTower-1].pull()

    display(towersArray)
    
    print("The disc you have taken is: "+str(desisredDisc.getWeight())+"\n")

    placeTower=int(input("[The tower you choose has to be empty or have a disc of bigger size]\n\
Which tower do you want to put the disc on?: "))

    if placeTower>int(len(towersArray)) or placeTower<1:
        while placeTower>int(len(towersArray)) or placeTower<1:
            placeTower=int(input("[The tower you choose has to be empty or have a disc of bigger size]\n\
[That tower does not exist]\n\
Which tower do you want to put the disc on?: "))

    towersArray[placeTower-1].addDisc(desisredDisc)

    print("\n")
    
print ("WIN!!!")
    
    
    
