'''
This script requires that the AAA mounts are placed in Blender in this order: left facing guns first, right facing guns second, and rear facing guns last
    -If you want to change this, then you have the edit the order the strings are concatenated in the final print statement
The script aslo requires that the AAA mount empties are named "AAA0, AAA1, AAA2, AAA3..." 
Ensure the parent AAA empty has the blue arrow facing directly forwards in local orientation mode in Blender
    -Both the left and right facing guns should have their blue arrows facing the same way as the parent in Blender
    -The rear facing guns should have their blue arrows pointing towards the rear of the ship or the opposite direction as the rest of them
There are only 3 different AAA sectors supported by this script: 
    -the left side, which encompasses the entire 180 degree arc of the left side of the ship
    -the right side, which encompasses the entire 180 degree arc of the right side of the ship
    -the back side, which encompasses a 240 degree arc centered on the back of the ship
Frontal firing arc isn't supported because I can't get anything with a firing arc that crosses 0/360 degree point to function properly (if one you guys knows how to do this, please let me know and I will update the script accordingly)
If you want to make the firing arc of each position more precise, then you will have to manually edit the firing arcs, but the script will still give you the correct amount of arcs
If you want to make the individual AAA Positions appear properly on the UI, then you will also have to manually edit this
You can use the divisibleBy variable to figure out how many individual AAA positions you can store in the aaaPositions variable for a slightly more detailed AAA position UI
    -To do this you also need to edit the range so it prints out the correct number of AAA positions
    -Ex: If my ship has 28 AAA positions, that number can be expressed as 4*7. The first number being how many seperate entries for aaaPositions are manually written and the second is the number that needs to go in the parenthesis next to range
    aaaPositions = [r'{\"x\":-70.0,\"y\":0.0,\"z\":200.0},{\"x\":70.0,\"y\":0.0,\"z\":200.0},{\"x\":-70.0,\"y\":0.0,\"z\":-200.0},{\"x\":70.0,\"y\":0.0,\"z\":-200.0}' for i in range(7)] is what the above example would look like in code
Final note: The script produces a string that starts after the comma separating the mounted guns with the AAA section; this is where you should paste the output, but make sure you keep the {"materialName":[]} that is usually the start of the last line of the model.txt
'''

numAA = int(input("Enter amount of AA guns: "))
gunSingle = [r'\"gun_single\"' for i in range(0,numAA)]
gunSin = ','.join(gunSingle)
# print (gunSin)
# print(len(gunSingle))

aaaMesh = [r'\"AAA' + str(i) + r'\"' for i in range(0,numAA)]
aaa = ','.join(aaaMesh)
# print (aaa)

verticalArc = [r'{\"x\":0.0,\"y\":-85.0}' for i in range(0,numAA)]
vertArc = ','.join(verticalArc)
# print (vertArc)
# print(len(verticalArc))

numLeftAA = int(input("Enter amount of AA guns on left side of ship: "))
leftHorizontalArc = [r'{\"x\":180.0,\"y\":360.0}' for i in range(0,numLeftAA)]
leftHoriArc = ','.join(leftHorizontalArc)
# print (leftHoriArc)
# print(len(leftHorizontalArc))

numRightAA = int(input("Enter amount of AA guns on right side of ship: "))
rightHorizontalArc = [r'{\"x\":0.0,\"y\":180.0}' for i in range(0,numRightAA)]
rightHoriArc = ','.join(rightHorizontalArc)
# print (rightHoriArc)
# print(len(rightHorizontalArc))

numBackAA = int(input("Enter amount of AA guns on back side of ship: "))
backHorizontalArc = [r'{\"x\":60.0,\"y\":300.0}' for i in range(0,numBackAA)]
backHoriArc = ','.join(backHorizontalArc)
# print (backHoriArc)
# print(len(backHorizontalArc))

# divisibleBy = [i for i in range(1,40) if numAAA % i == 0]
# print(divisibleBy)

aaaPositions = [r'{\"x\":0.0,\"y\":0.0,\"z\":0.0}' for i in range(numAA)]
aaaPos = ','.join(aaaPositions)
# print (aaaPos)
# print(len(aaaPositions))

strStart = r'"aaaGuns":["AAA"],"aaaGunsData":["{\"displayMounts\":false,\"particleRef\":['
# print(strStart)
strPartRefaaaPos = r'],\"aaaPositions\":['
# print(strPartRefaaaPos)
strAAAPosHoriArc = r'],\"horizontalArcs\":['
# print(strAAAPosHoriArc)
strHoriArcVertArc = r'],\"verticalArcs\":['
# print(strHoriArcVertArc)
strVertArcBaseNames = r'],\"baseTransformNames\":['
# print(strVertArcBaseNames)
strEnd = r'],\"sizes\":[],\"rate\":[]}"]}'
# print(strEnd)


# Final print statement that produces entire AAA sector of the model.txt
print(strStart+gunSin+strPartRefaaaPos+aaaPos+strAAAPosHoriArc+leftHoriArc+','+rightHoriArc+','+backHoriArc+strHoriArcVertArc+vertArc+strVertArcBaseNames+aaa+strEnd)
