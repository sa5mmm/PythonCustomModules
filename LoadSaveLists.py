##Python Programming
##Simple Load and Save Lists custom module

########Please do not change any code below this point! ##########
def loadList(listPar,fileName):
    #Open the file:
    try:
        file = open(fileName,'r+')#Sometimes python can't open the file properly so it needs to try one way then another way to acctually get it open!
    except:
        file = open(fileName,'a+')
    #Read each line in the file, then add it to the list!
    for line in file:
        newitem = line.strip()#This removes '\n' that shows up in our list and looks yucky!
        listPar.append(newitem)#We are putting the newitem in our list!
    file.close()#We have to close the file everytime we are done using it! Or we could cause problems!
    return listPar

def saveList(listPar,fileName):
    file = open(fileName,'w')#Open the file!
    for i in range(0,len(listPar),1):#Look at every item in the list!
        file.write("%s\n" % listPar[i])#Put every item in the list into the file!
    file.close()#We have to close the file everytime we are done using it! Or we could cause problems!