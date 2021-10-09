f=open("name.txt","w")
f.write((input("Your name:")))

f=open("name.txt","r")
c=f.read()
print("Your name is",c)

f=open("number.txt","w")
f.write("""17
42
400""")
f=open("number.txt","r")
a1=int(f.readline())
a2=int(f.readline())
s=a1+a2
print(s)

f=open("number.txt","r")
for i in range(3):
    d=f.readline()
    print(d,end='')
