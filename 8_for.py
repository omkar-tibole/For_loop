name="omkar"
for i in name:
    print(i)

color=["red","pink","yello","green"]
for i in color:
    
    print(i[0])


for i in range(5):
    print(i)

a=int(input("Enter value : "))
for i in range(1,11):
    print(i*a)


for i in range(1,6):
    for j in range(1,6):
        print(j,end="")
    print()


for i in range(7,1,-1):
    if i==2:
        break
    for j in range(1,i-1):
        print(j,end="")
    print()

for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end="")
    print()

for i in range(6,1,-1):
    for j in range(1,i):
        print("*",end="")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()


for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end="")
    print()



for i in range(6,1,-1):
    for j in range(i-1,0,-1):
        print(j,end="")
    print()

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()


for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()



