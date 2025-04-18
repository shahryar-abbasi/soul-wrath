#sum until zero
totalvalue = 0
while True:
    sum = int(input("enter a number ; 0 for total-value"))
    if sum == 0:
        break
    totalvalue+=sum
print(f'your value is{totalvalue}')


i=0
while i<=7:
    i+=1
    print(i)
    if i==4:
        break
print(i)

