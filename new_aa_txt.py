

numAAAPositions = int(input("How many distinct AAA postions do you want on the ship: "))
numGunsPerPosition = int(input("How many guns do you want at each position: "))



numAA = numAAAPositions * numGunsPerPosition
gunSingle = [r'\"gun_single\"' for i in range(0,numAA)]
gunSin = ','.join(gunSingle)
# print (gunSin)
print(len(gunSingle))

# aaaMesh = [r'\"AAA' + str(i) + r'\"' for i in range(0,numAA)]
# aaa = ','.join(aaaMesh)
# print (aaa)

verticalArc = [r'{\"x\":0.0,\"y\":-85.0}' for i in range(0,numAA)]
vertArc = ','.join(verticalArc)
# print (vertArc)
print(len(verticalArc))

# numLeftAA = int(input("Enter amount of AA guns on left side of ship: "))
# leftHorizontalArc = [r'{\"x\":180.0,\"y\":360.0}' for i in range(0,numLeftAA)]
# leftHoriArc = ','.join(leftHorizontalArc)
# # print (leftHoriArc)
# # print(len(leftHorizontalArc))

# numRightAA = int(input("Enter amount of AA guns on right side of ship: "))
# rightHorizontalArc = [r'{\"x\":0.0,\"y\":180.0}' for i in range(0,numRightAA)]
# rightHoriArc = ','.join(rightHorizontalArc)
# # print (rightHoriArc)
# # print(len(rightHorizontalArc))

# numBackAA = int(input("Enter amount of AA guns on back side of ship: "))
# backHorizontalArc = [r'{\"x\":60.0,\"y\":300.0}' for i in range(0,numBackAA)]
# backHoriArc = ','.join(backHorizontalArc)
# print (backHoriArc)
# print(len(backHorizontalArc))

# divisibleBy = [i for i in range(1,40) if numAAA % i == 0]
# print(divisibleBy)



if(numAAAPositions == 4):
    aaaPositions = [r'{\"x\":-70.0,\"y\":0.0,\"z\":200.0},{\"x\":70.0,\"y\":0.0,\"z\":200.0},{\"x\":-70.0,\"y\":0.0,\"z\":-200.0},{\"x\":70.0,\"y\":0.0,\"z\":-200.0}' for i in range(numGunsPerPosition)]
    aaaPos = ','.join(aaaPositions)
    print(len(aaaPositions))
    horizontalArcs = [r'{\"x\":240.0,\"y\":360.0},{\"x\":0.0,\"y\":120.0},{\"x\":180.0,\"y\":300.0},{\"x\":60.0,\"y\":180.0}' for i in range(numGunsPerPosition)]
    horiArc = ','.join(horizontalArcs)
    print(len(horizontalArcs))

# aaaPositions = [r'{\"x\":0.0,\"y\":0.0,\"z\":0.0}' for i in range(numAA)]

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
print(strStart+gunSin+strPartRefaaaPos+aaaPos+strAAAPosHoriArc+horiArc+strHoriArcVertArc+vertArc+strVertArcBaseNames+strEnd)