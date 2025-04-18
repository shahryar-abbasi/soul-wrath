import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(150)

i = 0
def demo():
    global i
    i += 1
    print("hello", i)
    # recursive function
    demo()

demo()
