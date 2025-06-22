# Simple For Loop Program
name="omkar"
for i in name:
    print(i)


# Write a program to print all elements of a list using a for loop.
color=["red","pink","yello","green"]
for i in color:
    print(i[0])



# Write a program to print numbers from 0 to 4 using a for loop and the range() function.
for i in range(5):
    print(i)



# Write a program to input a number and print its multiplication table up to 10.
a=int(input("Enter value : "))
for i in range(1,11):
    print(i*a)



# Write a program to print the following pattern using nested loops:
# 12345
# 12345
# 12345
# 12345
# 12345
for i in range(1,6):
    for j in range(1,6):
        print(j,end="")
    print()

""" 
Write a program to print the following star pattern using nested loops.
 12345
 1234
 123
 12
 1
 """
for i in range(7,1,-1):
    if i==2:
        break
    for j in range(1,i-1):
        print(j,end="")
    print()



""" 
Write a program to print the following pattern using nested loops:
 12345
 1234
 123
 12
 1
 """
for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end="")
    print()



"""
Write a program to print the following star pattern using nested loops:
 *****
 ****
 ***
 **
 *
 """
for i in range(6,1,-1):
    for j in range(1,i):
        print("*",end="")
    print()



""" 
Write a program to print the following pattern using nested loops:
 1
 12
 123
 1234
 12345
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()



"""
Write a program to print the following pattern using nested loops
*
**
***
****
*****
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()



"""
Write a program to print the following pattern using nested loops
12345
1234
123
12
1
"""
for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end="")
    print()



"""
Write a program to print the following pattern using nested loops
54321
4321
321
21
1
"""
for i in range(6,1,-1):
    for j in range(i-1,0,-1):
        print(j,end="")
    print()



"""
Write a program to print the following pattern using nested loops
54321
5432
543
54
5
"""
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()



"""
Write a program to print the following pattern using nested loops
5
54
543
5432
54321
"""
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end="")
    print()



