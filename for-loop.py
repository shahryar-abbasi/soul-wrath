list= ["messi","neymar","ronaldo"]
for r in list:
    print(r)
    for y in r:
        print(y)

cities = ("paris", "london", "tokyo")
for city in cities:
    print(city)
    if city == "london":
        break
    for letter in city:
        print(letter)



for n in range(1,11):
    print(n)

for o in range(0,21,2):
    print(o)

for p in range(10,0,-1):
     print(p)

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")

num = 5
for m in range(0,11):
    multiply = num * m
    print(f"{num}*{m}={multiply}")

text=("hello")
for u in text:
    reversed=""
    print(u)
