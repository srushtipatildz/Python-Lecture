#elif statement
x=int(input("enter value"))
if x==0:
    print("Zero")
else:
    print("Positive Integer")
#while loop
print("While loop")
count=0
while count<5:
    print(count)
    count+=1
#for Loop
print("For Loop:")
for i in range(5):
    print(i) 
#pass
print("Pass")
for i in range(5):
    print(i)
    pass
#continue
print("Continue")
for i in range(5):
    if i==2:
        continue
    print(i)
#break
print("Break Statement")
for j in range(5):
    if j==3:
        break
    print(j)

