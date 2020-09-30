a=0
b=1
user=int(input('Enter a number:'))
print(a)
print(b)
for i in range(0,user-2):
    c=a+b
    print(c)
    a=b
    b=c
