x = 13
def changex(x):
    x = x + 1
def f():
    changex(x)
    print(x)
f()
print(x)  