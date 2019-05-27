class A:
    'This Is Class A'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or j==0 or j==4 or i==3):
                    print("*",end="")
                else:
                    print(end=" ")    
            print()

class B:
    'This Is Class B'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or j==0 or j==4 or i==3 or i==6):
                    print("*",end="")
                else:
                    print(end=" ")    
            print()
class C:
    'This Is Class C'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or j==0 or i==6):
                    print("*",end="")
                else:
                    print(end=" ")    
            print()


class D:
    'This Is Class D'
    def __init__(self):
        for i in range(7):
            if(i==6 or i==0):
                print("**",end="")
            else:
                print(end="  ")
            for j in range(5):
                if(i==0 or j==0 or j==4 or i==6):
                    print("*",end="")
                else:
                    print(end=" ")    
            print()

class E:
    'This Is Class E'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or j==0 or i==3 or i==6):
                    print("*",end="")
                else:
                    print(end=" ")    
            print()

class F:
    'This Is Class F'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or j==0 or i==3):
                    print("*",end="")
                else:
                    print(end=" ")    
            print()
               
class G:
    'This Is Class G'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or j==0 or i==6):
                    print("*",end="")
                elif(i==3 and j==4):
                    print("***",end="")
                elif(i>3 and j==4):
                    print("* *",end="")
                else:
                    print(end=" ")
            if(i==6):
                print(end=' *')
            if(i==0):
                print(end="**")
            print()



class H:
    'This Is Class H'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==3 or j==0 or j==4):
                    print("*",end="")
                else:
                    print(end=" ")
            print()


class I:
    'This Is Class I'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or j==2 or i==6):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

class J:
    'This Is Class J'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or j==2):
                    print("*",end="")
                elif(j==0 and i>3):
                    print(end="*")
                elif(i==6 and j<2):
                    print(end="*")
                else:
                    print(end=" ")
            print()

class K:
    'This Is Class K'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(j==0):
                    print("*",end="")
                elif(j==4):
                    if(i==0 or i==6):
                        print(end="*")
                    else:
                        print(end=" ")
                elif(j==3):
                    if(i==1 or i==5):
                        print(end="*")
                    else:
                        print(end=" ")
                elif(j==2):
                    if(i==2 or i==4):
                        print(end="*")
                    else:
                        print(end=" ")
                elif(j==1):
                    if(i==3 or i==3):
                        print(end="*")
                    else:
                        print(end=" ")
                else:
                    print(end=" ")
            print()


class L:
    'This Is Class L'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(j==0 or i==6):
                    print("*",end="")
                else:
                    print(end=" ")
            print()
class M:
    'This Is Class M'
    def __init__(self):
        for i in range(7):
            for j in range(7):
                if(j==0 or j==6):
                    print("*",end="")
                elif(i==4 and j==3):
                    print(end="*")
                elif(i==1 and (j==1 or j==5)):
                    print(end="*")
                elif(i==2 and (j==2 or j==4)):
                    print(end="*")
                elif(i==3 and (j==3 or j==3)):
                    print(end="*")
                else:
                    print(end=" ")
            print()

            
class N:
    'This Is Class N'
    def __init__(self):
        for i in range(7):
            for j in range(7):
                if(j==0 or j==6):
                    print("*",end="")
                elif(i==j):
                    print(end="*")
                else:
                    print(end=" ")
            print()

class O:
    'This Is Class O'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or j==0 or j==4 or i==6):
                    print("*",end="")
                else:
                    print(end=" ")    
            print()

class P:
    'This Is Class P'
    def __init__(self):
        for i in range(4):
            for j in range(5):
                if(i==0 or j==0 or j==4 or i==3):
                    print("*",end="")
                else:
                    print(end=" ")    
            print()
        for i in range(3):
            for j in range(5):
                if(j==0):
                    print(end="*")
                else:
                    print(end=" ")
            print()
class Q:
    'This Is Class Q'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or j==0 or j==4 or i==6):
                    print("*",end="")
                elif(i>3 and i-2==j):
                    print(end="*")
                else:
                    print(end=" ")
                    
            print()
        print(end="     *")

class R:
    'This Is Class R'
    def __init__(self):
        for i in range(4):
            for j in range(5):
                if(i==0 or j==0 or j==4 or i==3):
                    print("*",end="")
                else:
                    print(end=" ")    
            print()
        for i in range(3):
            for j in range(5):
                if(j==0 or i==j-2):
                    print(end="*")
                else:
                    print(end=" ")
            print()

class S:
    'This Is Class S'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or i==3 or i==6):
                    print("*",end="")
                elif((i<4 and j==0) or (i>3 and j==4)):
                    print(end="*")
                else:
                    print(end=" ")
            print()



class T:
    'This Is Class T'
    def __init__(self):
        for i in range(7):
            for j in range(5):
                if(i==0 or j==2):
                    print("*",end="")
                else:
                    print(end=" ")
            print()

class U:
    'This Is Class U'
    def __init__(self):
        for i in range(5):
            for j in range(5):
                if(i==4 or j==0 or j==4):
                    print("*",end="")
                else:
                    print(end=" ")
            print()
 

class V:
    'This Is Class V'
    def __init__(self):
        for i in range(5):
            for j in range(5):
                if(i==j):
                    print("*",end="")
                else:
                    print(end=" ")
            for j in range(8,2*i,-2):
                print(" ",end="")
            print("*")


class W:
    'This Is Class W'
    def __init__(self):
        for i in range(9):
            for j in range(9):
                if(j==0 or j==8):
                    print("*",end="")
                elif(i==j and i>3):
                    print(end="*")
                elif(i+j==8 and j<4):
                    print(end="*")
                else:
                    print(end=" ")  
            print()

class X:
    'This Is Class X'
    def __init__(self):
        for i in range(7):
            for j in range(7):
                if(i==j):
                    print("*",end="")
                elif(i+j==6):
                    print(end="*")
                else:
                    print(end=" ")
            print()



class Y:
    'This Is Class Y'
    def __init__(self):
        for i in range(7):
            for j in range(7):
                if(i==j and j<4):
                    print("*",end="")
                elif(i+j==6):
                    print(end="*")
                else:
                    print(end=" ")
            print()


class Z:
    'This Is Class Z'
    def __init__(self):
        for i in range(7):
            for j in range(7):
                if(i==0 or i==6):
                    print("*",end="")
                elif(i+j==6):
                    print(end="*")
                else:
                    print(end=" ")
            print()


               
        
st=input("Enter Your Name : ")
print("*****************************")
for i in st:
    x=ord(i)
    if(x>90):
        x=x-32
    if(x==65):
        obj=A()
    if(x==66):
        obj=B()
    if(x==67):
        obj=C()
    if(x==68):
        obj=D()
    if(x==69):
        obj=E()
    if(x==70):
        obj=F()
    if(x==71):
        obj=G()
    if(x==72):
        obj=H()
    if(x==73):
        obj=I()
    if(x==74):
        obj=J()
    if(x==75):
        obj=K()
    if(x==76):
        obj=L()
    if(x==77):
        obj=M()
    if(x==78):
        obj=N()
    if(x==79):
        obj=O()
    if(x==80):
        obj=P()
    if(x==81):
        obj=Q()
    if(x==82):
        obj=R()
    if(x==83):
        obj=S()
    if(x==84):
        obj=T()
    if(x==85):
        obj=U()
    if(x==86):
        obj=V()
    if(x==87):
        obj=W()
    if(x==88):
        obj=X()
    if(x==89):
        obj=Y()
    if(x==90):
        obj=Z()
    print(end="\n\n\n")
print("*****************************")





               
            




               
            
