#Linear search,Bubble sort and Insersion sort 

import random

#Linear search
class linear_search():
    def __init__(self):
        self.array=["RED","BLUE","GREEN","YELLOW"]

    def add(self,data):
        data=data.upper()
        found=False
        for item in self.array:
            if item==data:
                found=True
                break
        if found==True:
            print ("LINEAR SEARCH: "+data+" already in list")
        else:
            self.array.append(data)
            print ("LINEAR SEARCH: "+str(self.array)+" has been added to the list")
        print("")

    def search(self,data):
        data=data.upper()
        found=False
        for item in self.array:
            if item==data:
                found=True
                break
        if found==True:
            print ("["+data+"] has been found!")
        else:
            print ("["+data+"] has not been found")
        print ("")






#Bubble sort
class bubble_sort():
    def __init__(self):
        self.array=[2,5,4,1,3]

    def make_new_list(self,data):
        self.array=data
        print ("The array has been overwritten")

    def sort(self):
        print("[BEFORE SORT] "+str(self.array))
        loop=True
        while loop==True:
            reset=False
            pos=0
            for item in self.array:
                if pos==int(len(self.array)-1):
                    pos=0
                    print (str(self.array))
                else:
                    if item>self.array[pos+1]:
                        temp=item
                        self.array[pos]=self.array[pos+1]
                        self.array[pos+1]=temp
                        reset=True
                        print (str(self.array))
                    pos+=1
            if reset==False:
                loop=False
        print ("[ORDERED] "+str(self.array))
        print("")






#insersion sort
class insersion_sort():
    def __init__(self):
        self.array=[1,5,4,2,3]

    def make_new_list(self,data):
        self.array=data
        print ("[INSERSION SORT] The array has been overwritten")

    def sort(self):
        comp_count=0 #comparison count?
        pos_count=1  #position count
        print ("[BEFORE SORT] "+str(self.array))

        while pos_count!=int(len(self.array)):
            if self.array[pos_count]<self.array[comp_count]:
                loop=False
                while loop!=True:
                    if self.array[pos_count]<self.array[comp_count] and comp_count>=0: #note: corrected from "and comp_count!=0"
                        comp_count-=1
                    else:
                        loop=True
                        temp=self.array[pos_count]
                        self.array.pop(pos_count)
                        self.array.insert(comp_count+1,temp)
                        print (str(self.array))
            else:
                pos_count+=1
            comp_count=pos_count-1
        print ("[ORDERED] "+str(self.array))
        print ("")









#Instanciates all of the classes
insersion=insersion_sort()
bubble=bubble_sort()
linear=linear_search()

#Criteria for the loop
done=0

#A loop to keep the program going
while done==0:
    #User interface to allow the user to pick what class/feature they want to use
    choice=int(input("What do you want to do:\n\
1) Bubble sort\n\
2) Insersion sort\n\
3) Linear search\n\
4) Quit\n\
:  "))
    print ("")


#######################BUBBLE SORT#####################

    #Handles the bubble sort feature/class
    if choice==1:
        #Allows the user to specify what they want to do to the array in the bubble sort class
        choice=int(input("[BUBBLE SORT] What do you want to do:\n\
1) Make a new array (numbers only)\n\
2) sort the array (numbers only)\n\
:  "))
        print("")
        #Handles the creation of a new list for the bubble sort class
        if choice==1:
            index=int(input("How many numbers do you want the array to hold\n\
:  "))
            print("")
            array=[]
            while index!=0:
                value=int(input("Enter a number\n\
:  "))
                print("")
                array.append(value)
                index-=1
            bubble.make_new_list(array)

        #Handles the sorting of the array in the bubble sort class
        else:
            bubble.sort()

########################INSERSION SORT######################

    elif choice==2:
        choice=int(input("[INSERSION SORT] What do you want to do:\n\
1) Make a new array (numbers only)\n\
2) Sort the array\n\
:  "))
        print ("")
        if choice==1:
            index=int(input("How many numbers do you want the array to hold\n\
:  "))
            print("")
            array=[]
            while index!=0:
                value=int(input("Enter a number\n\
:  "))
                print("")
                array.append(value)
                index-=1
            insersion.make_new_list(array)

        elif choice==2:
            print(str(insersion.sort()))

########################LINEAR SEARCH#######################

    elif choice==3:
        choice=int(input("[LINEAR SEARCH] What do you want to do:\n\
1) Add an item to the list\n\
2) Search for an item\n\
:  "))
        print ("")
        if choice==1:
            data=input("Enter the data that you want to add\n\
:  ")
            print("")
            data_list=list(data)
            last_space=int(len(data_list)-1)
            if data_list[last_space]==" ":
                while data_list[last_space]==" ":
                    data_list.pop(last_space)
                    last_space-=1
            data=""
            for item in data_list:
                data=data+item
            linear.add(data)

        elif choice==2:

            data=input("Enter the data that you are looking for\n\
:  ")
            print("")
            data_list=list(data)
            last_space=int(len(data_list)-1)
            if data_list[last_space]==" ":
                while data_list[last_space]==" ":
                    data_list.pop(last_space)
                    last_space-=1
            data=""
            for item in data_list:
                data=data+item
            linear.search(data)
    elif choice==4:
        done=1
