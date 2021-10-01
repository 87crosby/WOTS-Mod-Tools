numAA = int(input("Enter the amount of AAA mounts on the ship: "))
# x = [r'\"gun_single\"' for i in range(0,numAA)]
# print (*x, sep =',')

gunName = input("Enter the alphabetical prefix of the secondary gun mesh (not the barrel): ")
barrelName = input("Enter the alphabetical of the secondary gun barrel mesh: ")
numSec = int(input("Enter the amount of secondary gun positions: "))
# y = ['"gunName' + str(i) + '"' for i in range(0,numSec)]
# z = ['"barrelName' + str(i) + '"' for i in range(0,numSec)]

# print (*y, sep =', ')
# print (*z, sep =', ')

# a = [r'\"AAA' + str(i) + r'\"' for i in range(0,78)]
# print (*a, sep =',')

# va = [r'{\"x\":0.0,\"y\":-85.0}' for i in range(0,78)]
# print (*va, sep =',')

# fha = [r'{\"x\":-120.0,\"y\":120.0}' for i in range(0,16)]
# print (*fha, sep =',')

# lha = [r'{\"x\":-180.0,\"y\":0.0}' for i in range(16,38)]
# print (*lha, sep =',')

# rha = [r'{\"x\":0.0,\"y\":180.0}' for i in range(38,60)]
# print (*rha, sep =',')

# bha = [r'{\"x\":120.0,\"y\":240.0}' for i in range(60,78)]
# print (*bha, sep =',')

# div = [i for i in range(1,50) if 78 % i == 0]
# print(div)

aaaPos = [r'{\"x\":-70.0,\"y\":0.0,\"z\":920.0},{\"x\":70.0,\"y\":0.0,\"z\":920.0},{\"x\":-95.0,\"y\":0.0,\"z\":200.0},{\"x\":95.0,\"y\":0.0,\"z\":200.0},{\"x\":-95.0,\"y\":0.0,\"z\":-880.0},{\"x\":95.0,\"y\":0.0,\"z\":-880.0}' for i in range(13)]
print (*aaaPos, sep =',')