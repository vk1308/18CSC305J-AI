numofbanana = int(input("Enter the number of bananas: "))
totdistance = int(input("Enter the distance you wanna cover: "))
maxload = int(input("Enter max load capacity of your camel: "))
start = numofbanana
lose = 0
for i in range(totdistance):
 if start==0:
 break
 while start>0:
 start = start-maxload
 if start==1:
 lose-=1
 lose+=2
 lose-=1
 start=numofbanana-lose
print(start)
