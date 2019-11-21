def AND(a,b):
    if a==1 and b==1:
        return 1
    else :
        return 0
def OR(a, b):
    if a == 1:
        return 1
    if b == 1:
        return 1
    return 0
def XOR(a, b):
    if a != b:
        return 1
    return 0
print("adder:")
a=input()
b=input("+")
c = ""
n=-1
jinwei = 0
while n >= -(len(a)):
    new=XOR(int(a[n]), int(b[n]))
    new = XOR(new,jinwei)
    jinwei = OR(AND(int(a[n]),int(b[n])),OR(AND(int(a[n]),jinwei), AND(int(b[n]),jinwei)))
    n-=1
    c+= str(new)
c+= "1"
print(c[::-1])

