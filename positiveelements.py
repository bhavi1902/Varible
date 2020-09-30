# print out the positive elements in the list
list_1=[]
list_2=[]
n=int(input("Enter the size of the list:"))
for i in range(0,n):
    prompt=input("Enter the elements in the list:")
    list_1.append(prompt)
print("the user list:",list_1)
for j in list_1:
        if int(j)>0:
            list_2.append(int(j))
print("The list with positive number:",list_2)
